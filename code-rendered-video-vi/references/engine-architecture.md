# Kiến trúc engine

Lối engine vẽ mọi frame của phim trong trình duyệt bằng WebGL2, như một hàm của thời gian bài nhạc (song time), rồi ghép các shot trên một trang phát chúng cùng với nhạc. File này mô tả engine của bộ starter mà skill kèm theo trong `assets/starter/`: hợp đồng (contract) của nó, các lớp (layer), các công cụ, chi phí khi chạy, và những gì thay đổi khi chuyển nó sang máy khác.

Nạp file này khi: phim đi theo lối engine và bạn đang dựng thư mục phim, viết bộ kit dùng chung hoặc một brief cho builder, kiểm tra cách một shot dùng engine, chẩn đoán một bản chụp (capture) bị trống, chậm hoặc sai, hoặc chuyển phim sang hệ điều hành khác.

Một thư mục phim là một bản sao của starter. Các đường dẫn tính tương đối với nó: một thư mục duy nhất chứa `package.json`, `shots.json`, `copy.json`, `audio/`, `data/`, `src/`, `scripts/` và `analysis/`. Starter được làm từ app của các phim tham chiếu, mà file này gọi là "app tham chiếu"; README của starter liệt kê những gì nó đã thay đổi. Engine được phát triển từ một engine mã nguồn mở theo giấy phép MIT; `src/engine/LICENSE-pdoom-video.txt` đi kèm theo mọi bản sao.

## 1. Hợp đồng

Mỗi frame là một hàm thuần (pure function) của song time. Hỏi cùng một thời điểm hai lần, shot vẽ ra cùng một hình hai lần, bất kể trước đó đã vẽ gì.

| Quy tắc | Trong thực tế |
|---|---|
| Không dùng đồng hồ thực | Không `Date`, không `performance.now`, không timer bên trong scene. Thời gian chỉ đến từ đối tượng frame |
| Không random không có seed | Không `Math.random`. Dùng `hash`, `mulberry32`, `noise1`, `noise2`, `noise3`, `fbm1`, `fbm2` (`src/engine/util.ts`), và các hàm hash của `src/engine/glsl/common.ts` trong shader |
| Không mang state giữa các frame | Hình ở một thời điểm không được phụ thuộc vào những frame nào đã vẽ trước nó. Một mô phỏng được tích phân một lần trong `init()` vào một mảng rồi tra theo thời gian |
| State chỉ được phép kèm preroll | Một scene cần tích phân thì đặt `stateful = true` và hiện thực `reset()`. Sau một lần seek, engine reset nó và mô phỏng lại từ tối đa `prerollMax` giây trước đó. State cần lịch sử dài hơn thế là không được phép |
| Thời gian âm nhạc đến từ dữ liệu | Beat và bar được đọc từ beat grid (lưới nhịp) của dữ liệu audio, không bao giờ tính từ số giây hay từ một con số tempo |
| Thứ gì đổi theo bậc thì đọc tại frame, và chỉ thứ đó | Một giá trị đổi theo bậc và được vẽ nguyên như vậy (một bộ đếm, một từ, một nhãn) được tính từ thời điểm của frame đầu ra (`frameIdx` trong `src/engine/util.ts`, `frameTime` và `frameClock` trong `src/scenes/parts/kit-frame.ts`), để các sub-frame của một bản export có motion blur thống nhất với nhau về nó và nó không bị bóng ma. Thứ gì chuyển động thì tính từ `f.t`. Một quyết định chọn cái gì được vẽ (pha nào, mở hay đóng, nhánh code nào) dùng cùng thời gian với phần vẽ mà nó chọn. Giữa các frame, trong studio, thời gian đã làm tròn chạy trước `f.t` tới nửa frame; một nhánh được chọn từ nó trong khi hình của nó được vẽ tại `f.t` sẽ vẽ sai nhánh trong một khoảnh khắc. Từ thực tế: một dòng chữ đã chìm xuống quay lại trong một khoảnh khắc ở giây 9.995 theo cách này, thấy được khi phát và không thấy trong bất kỳ capture nào tại một frame |

| Các quy tắc mang lại gì | Vì sao |
|---|---|
| Một still (ảnh tĩnh) đại diện cho phim | Capture một khoảnh khắc chính là khoảnh khắc đó của phim, nên việc review bằng still có ý nghĩa |
| Seek hoạt động | Studio có thể nhảy tới bất kỳ shot nào, lặp nó và bước từng frame |
| Capture bằng playback | Công cụ capture và studio chạy cùng các module tại cùng các thời điểm |
| Transition có thể bẻ cong thời gian | Engine có thể giữ một shot ở một frame, đóng băng nó hoặc phát lại một lát của nó (mục 6) |
| Hot swap an toàn | Một module được thay khi studio đang mở sẽ hiện đúng hình ngay lập tức |
| Có thể lấy mẫu sub-frame | Một bản export có thể render các sub-frame của một frame không theo thứ tự thời gian |

Đồng hồ thực chỉ xuất hiện ở một chỗ, vòng lặp playback của studio, nơi nó làm mượt đồng hồ thô của phần tử audio thành song time. Scene không bao giờ thấy nó.

Từ thực tế: ở phim đầu tiên, cùng một frame render trong các lần chạy riêng cho ra các file giống nhau từng byte, và tìm trong thư mục scene các lời gọi đồng hồ và random thì không thấy cái nào. Hãy chạy cả hai phép kiểm tra trên một phim mới trước khi dựng bất kỳ shot thật nào.

## 2. Các lớp

| Lớp | Sở hữu | File trong starter |
|---|---|---|
| Cấu hình dự án | Tiêu đề, file nhạc, bản nhạc nén mà studio phát, frame rate, kích thước của format chính (master) và của các format có tên khác, bước frame, cổng của studio, dấu nhận diện trang | `src/project-config.ts` |
| Dữ liệu audio | Thời lượng, thời điểm beat, thời điểm downbeat, ranh giới shot tính bằng giây, các envelope, onset trống | `data/audio.json`, được đọc bởi `src/engine/audio.ts`; vị trí âm nhạc trong `src/engine/beat-cues.ts`. Được ghi bởi bước phân tích một track, bởi `scripts/make-click-grid.ts`, hoặc bởi `scripts/make-score.ts` với một bản nhạc soạn bằng code |
| Âm thanh viết bằng code | Bản nhạc (score), các hiệu ứng âm thanh của hình (tổng hợp hoặc file thu sẵn đặt theo đỉnh của chúng), voice-over và bản mix, render offline ra WAV, trên lưới riêng của score hoặc đè lên một track đã đo | `data/score.json`, `data/voice.json`, `src/sound/`, `scripts/make-score.ts`, `scripts/voice-sapi.ps1` (`sound-and-voice.md`) |
| Thời điểm của từ | Các từ của bài hát hoặc của voice-over, kèm thời điểm của chúng; các nhóm caption của giọng đọc | `data/lyrics.json`, được `src/engine/lyrics.ts` đọc vào `ctx.lyrics`. Tùy chọn |
| Dữ liệu shot | Danh sách shot tính bằng bar, các section, transition dẫn vào mỗi shot, caption, mọi từ ngữ | `shots.json` và `copy.json`, có kiểu từ `src/film.ts` |
| Timeline | Một entry cho mỗi shot và một entry overlay; module nào phát mỗi entry; transition đặt trên beat grid | `src/timeline.ts` |
| Module scene | Hình của một shot | `src/scenes/<shot id>.ts`, các phần riêng trong `src/scenes/parts/` |
| Hình từ file | Ảnh, logo và ảnh chụp màn hình dưới dạng texture, clip dưới dạng chuỗi ảnh đánh số, và các lần nạp mà một still phải chờ | `src/engine/media.ts`, các file trong `media/` (mục 4) |
| Thẻ storyboard | Hình của mọi shot chưa có module | `src/scenes/storyboard-card.ts` |
| Kit dùng chung | Vùng chữ, camera, đồng hồ theo beat, nền (bầu trời, mặt nước, sương mù), giọng chữ (type voice), chữ chuyển động, preset post, hạt (particle), thiết bị và thẻ trong không gian, các pass trên layer (blur, goo, kính lỏng, difference), rig nhân vật, lớp pixel | `src/scenes/parts/kit-frame.ts`, `kit-camera.ts`, `kit-ground.ts`, `kit-type.ts`, `kit-post.ts`, `kit-particles.ts`, `kit-devices.ts`, `kit-rig.ts`, `kit-pixel.ts` |
| Lõi engine | Renderer, việc nạp, đối tượng frame, preroll, compositing, lấy mẫu sub-frame, đọc ngược pixel | `src/engine/engine.ts`, `scene.ts`, `gl.ts`, `lines.ts`, `util.ts`, `palette.ts`, `type.ts`, `scale.ts`, `glsl/common.ts` |
| Chuỗi post | Diện mạo của frame hoàn chỉnh | `src/engine/post.ts` |
| Pass transition | Điều gì xảy ra với hình quanh một cú cắt | `src/engine/transition.ts` |
| Overlay | Chữ không thuộc riêng shot nào, vẽ đè lên hình hoàn chỉnh; cũng là các nhóm caption của voice-over, ở chân frame | `src/scenes/overlay.ts` |
| Công cụ capture | Still, contact sheet, thời gian frame, đầu dò đồ họa, export, ở bất kỳ format nào của phim | `scripts/render.ts` |
| Trang studio | Playback cùng nhạc, danh sách shot, seek, hot swap, click track của phim không có nhạc, nút chuyển format, `window.seek` | `index.html`, `src/main.ts`, `src/click-track.ts`, `vite.config.ts` |
| Build một file | Trang studio dưới dạng một file HTML phát được từ ổ đĩa, với script, font, dữ liệu, hình và nhạc được đóng gói bên trong | `scripts/build-single.ts` (`bun run single`); `studio-viewer.md`, mục 11 |

Hai cái tên trong starter khác với thuật ngữ của skill này. Danh sách `sections` của dữ liệu audio chứa một mục cho mỗi shot, còn dữ liệu shot gọi một section của phim là `group`; một section được đánh số là một group loại `section`. Studio được khởi động bằng `bun run studio`.

## 3. Hợp đồng scene

Một shot được dựng thành một module scene: một file có default export là một class kế thừa `Scene` (`src/engine/scene.ts`).

```ts
export abstract class Scene {
  stateful = false;
  prerollMax = 6;
  handlesTransition = false;
  handlesPortal = false;
  constructor(protected ctx: SceneCtx) {}
  init(): Promise<void> | void {}
  reset(): void {}
  abstract render(f: Frame, out: THREE.WebGLRenderTarget): PostOverrides | void;
  dispose(): void {}
}
```

| Bước | Được gọi | Nhiệm vụ |
|---|---|---|
| Constructor và các khởi tạo field | Một lần, khi entry được nạp | Tạo pass, layer và batch. Renderer đã tồn tại sẵn |
| `init()` | Một lần, trước lần render đầu tiên. Có thể bất đồng bộ | Nạp tài nguyên, tích phân mô phỏng vào mảng, dựng các cache mà nếu không có sẽ làm frame đầu chậm |
| `render(f, out)` | Cho mọi frame, và cho mọi sub-frame và bước preroll | Ghi đè hoặc xóa toàn bộ `out`, một target half float trong ánh sáng tuyến tính (linear light). Trả về các thiết lập post mà khoảnh khắc đó cần, hoặc không trả gì. Overlay thì ngược lại: nó vẽ đè lên `out` và không được xóa nó |
| `reset()` | Khi seek, với scene stateful, trước preroll | Đưa state về như lúc bắt đầu shot |
| `dispose()` | Khi module bị thay bằng hot swap | Giải phóng texture, target, material và line batch |

Một scene ném lỗi trong `init()` sẽ được liệt kê trong danh sách lỗi của engine, và entry của nó được vẽ thành một frame đỏ sẫm. Một scene ném lỗi trong `render()` được ghi log ra console và vẽ cùng frame đỏ sẫm đó.

| Cờ | Mặc định | Tác dụng |
|---|---|---|
| `stateful` | `false` | Sau một lần seek, engine gọi `reset()`, rồi `render()` với `preroll: true` ở mọi bước frame từ `max(start, t - prerollMax)` cho tới thời điểm được hỏi |
| `prerollMax` | 6 | Lịch sử dài nhất mà engine mô phỏng lại, tính bằng giây |
| `handlesTransition` | `false` | Khi các entry trên timeline chồng lên nhau, engine không crossfade; scene tự composite `f.under` |
| `handlesPortal` | `false` | Scene tự đóng phần của mình trong một `zoom-in` hoặc `pull-out` và nhận `f.portal`; bản thay thế (stand-in) của engine không được phát |

Context, `this.ctx`, chứa những gì không đổi từ frame này sang frame khác: `renderer`, `audio` (dữ liệu audio), `lyrics` (thời điểm của từ, rỗng khi phim không có; khi có voice-over thì là các nhóm caption của nó), `comp` (compositor), `W` và `H` (kích thước logic), `id` và `params` của entry trên timeline, cùng `start` và `end` của nó tính bằng giây.

Đối tượng frame, `f`:

| Field | Ý nghĩa | Đơn vị |
|---|---|---|
| `t` | Song time của lần gọi render này | giây |
| `dt` | Bước danh nghĩa kể từ lần gọi trước: bước frame trong studio và trong capture, khoảng cách giữa các sub-frame khi lấy mẫu sub-frame, 0 sau một lần seek và trên một frame bị giữ. Nó không bao giờ được đo từ đồng hồ | giây |
| `lt` | Thời gian kể từ đầu shot | giây |
| `p` | Tiến độ qua cửa sổ của shot | 0 đến 1 |
| `start`, `end` | Cửa sổ của entry | giây song time |
| `seeked` | True khi thời gian nhảy. Với scene stateful, nó là false ở lần render hiển thị, vì preroll đã dựng lại state | boolean |
| `preroll` | True trong khi engine tua nhanh một scene stateful. Bỏ qua phần việc chỉ phục vụ cho hình | boolean |
| `beat` | Chỉ số beat liên tục của cả track, 0 ở beat đầu tiên | beat |
| `bar` | Chỉ số bar liên tục của cả track, 0 ở downbeat đầu tiên | bar |
| `beatPhase`, `barPhase` | Phần thập phân của `beat` và `bar` | 0 đến 1 |
| `a` | Đặc trưng audio tại `t`. Các envelope `rms`, `low`, `mid`, `high`, `vocal`, `drums`, `bass`, `other`; envelope nào dữ liệu không có thì đọc ra 0. Các xung tắt dần `kick`, `snare`, `hat`, `vonset`, bằng 1 tại một cú đánh mạnh tối đa | 0 đến 1 |
| `under` | Khi entry chồng lên entry trước nó: hình của entry đó. Với overlay: hình hoàn chỉnh, cũng chính là target mà nó vẽ vào, nên không được lấy mẫu nó trong khi vẽ. Ngoài ra là null | texture |
| `tin` | Tiến độ qua đoạn chồng với entry trước. Bằng 1 khi không có | 0 đến 1 |
| `tout` | Tiến độ qua đoạn chồng với entry sau. Bằng 0 khi không có | 0 đến 1 |
| `portal` | Với scene có `handlesPortal`, trong một `zoom-in` dẫn ra khỏi nó hoặc một `pull-out` dẫn vào nó: hình của shot kề bên, được giữ tĩnh. Ngoài ra là null | texture |
| `portalK` | Tiến độ qua transition đó. Khi đi vào, chi tiết phải lấp đầy frame đúng tại 1. Khi đi ra, nó lấp đầy frame tại 0 | 0 đến 1 |

`beat` và `bar` đếm từ đầu track. Một shot cần số beat tính từ lúc nó bắt đầu: kit cung cấp đồng hồ đó (`sceneClock` cho thứ chuyển động, `frameClock` cho thứ đổi theo bậc, trong `src/scenes/parts/kit-frame.ts`).

Hình dạng của một shot trong starter, `src/scenes/<shot id>.ts`, như README của nó đưa ra, có thêm camera 2D của kit:

```ts
import type * as THREE from 'three';
import { Scene, type Frame, type PostOverrides } from '../engine/scene';
import { Layer2D } from '../engine/gl';
import { Ground } from './parts/kit-ground';
import { sceneClock, frameClock } from './parts/kit-frame';
import { camAt, applyCam } from './parts/kit-camera';
import { POST_DARK, TYPE_TINT } from './parts/kit-post';

export default class WaterColdKettle extends Scene {
  private ground = new Ground();
  private layer = new Layer2D();

  render(f: Frame, out: THREE.WebGLRenderTarget): PostOverrides {
    const { renderer, comp, audio } = this.ctx;
    const k = sceneClock(audio, f);   // beats since the shot began: for everything that moves
    const kf = frameClock(audio, f);  // the same at the output frame: for everything that steps
    this.ground.render(renderer, out, { colour: 'ink' });   // overwrites the whole target
    const c = this.layer.ctx;
    this.layer.clear();
    c.save();
    applyCam(c, camAt(k.beats, [/* { at, pose } keys */]));
    // ... draw in world coordinates, from k and kf only
    c.restore();
    comp.draw(renderer, this.layer.upload(), out, { tint: TYPE_TINT });
    return POST_DARK;
  }

  override dispose() { this.ground.dispose(); this.layer.dispose(); }
}
```

Tên file phải đúng chính xác là shot id trong `shots.json`, còn tên class thì tùy ý. `Layer2D.dispose()` giải phóng cùng lúc bản upload của layer và bản sao sRGB của nó.

Từ thực tế: ở phim thứ hai không scene nào đặt `stateful` hay `handlesTransition`, và không scene nào đọc `f.a`. Mọi mô phỏng đều được tích phân trong `init()`, mọi sự kiện đều được đặt theo đồng hồ beat, và bốn scene đặt `handlesPortal`. Hãy coi lối stateful và lối chồng entry là ít được kiểm chứng hơn phần còn lại.

## 4. Các bề mặt vẽ

Scene bố cục theo pixel logic, `W` x `H`, gốc ở góc trên bên trái, trục y hướng xuống. `W` và `H` là kích thước của format mà trang đang hiển thị: format chính của cấu hình dự án, hoặc một format có tên khác được chọn bằng tham số trang `format` (bên dưới, "Các format"). Tham số trang `scale` nhân kích thước vật lý của mọi target; layer, line batch và code shader dùng chung vẫn vẽ theo pixel logic.

| Bề mặt | Tạo bằng | Dùng cho | Cần biết |
|---|---|---|---|
| Layer canvas 2D | `Layer2D` (`src/engine/gl.ts`) | Chữ, hình vẽ phẳng, giao diện, bất cứ thứ gì Canvas2D vẽ tốt | Gọi `clear()`, vẽ, rồi `upload()` một lần mỗi frame. Lần upload gửi canvas dưới dạng byte 8-bit thuần, và một pass nhỏ chép nó vào một texture sRGB 8-bit, được giải mã sang ánh sáng tuyến tính khi lấy mẫu (mục 11). Một layer có thể nhỏ hơn frame, hoặc có backing scale thấp hơn để tạo glow mềm. Mỗi lần upload chép toàn bộ canvas lên card đồ họa và chạy pass đó. `dispose()` giải phóng cả hai texture |
| GPU line batch | `LineBatch` (`src/engine/lines.ts`) | Hàng nghìn đoạn thẳng khử răng cưa mỗi frame: trường đường kẻ, nét gạch bóng (hatching), wireframe, tia lửa, theo pixel hoặc trong không gian với bất kỳ camera nào | Dung lượng cố định khi tạo và đoạn vượt quá sẽ bị bỏ mà không có thông báo. Màu là tuyến tính và có thể vượt 1 để phát sáng. Blend là `add`, `max` hoặc `normal`. Độ rộng tính bằng pixel, hoặc bằng đơn vị thế giới với `worldWidth`. `render()` không xóa target |
| Pass shader toàn màn hình | `FSPass` (`src/engine/gl.ts`) | Nền, trường (field), không gian dò bằng tia (ray), hiệu ứng in ấn, bất cứ thứ gì tính theo từng pixel | Fragment là GLSL ES 3.0, đọc `vUv`, ghi `fragColor`. Noise, hash, hàm khoảng cách, hatching, bảng màu dưới dạng hằng `C_<NAME>` và `FRAG_PX` được chèn sẵn phía trước. Nó ghi đè target trừ khi được yêu cầu blend |
| Scene three.js | Một target riêng của scene, `makeRT(W, H, { samples: 4 })` | Model, đèn và material thật | Target được truyền vào `render()` không có khử răng cưa. Xóa target riêng về alpha 0, render vào đó, rồi composite nó với `premult: false`. Đặt màu theo ánh sáng tuyến tính từ bảng màu |
| Compositor | `this.ctx.comp.draw(renderer, texture, target, options)` | Đặt bất kỳ texture nào lên một target | Các tùy chọn là `mode`, `opacity`, `tint`, `scale`, `offset` và `premult` |
| Hình dưới dạng texture | `ImageTexture` và `drawPicture` (`src/engine/media.ts`) | Một tấm ảnh, logo, ảnh chụp màn hình: trên GPU, trong một hình chữ nhật, trong shader hoặc trên material three.js | Nạp nó trong `init()`. Nó lên GPU theo cùng lối với layer canvas, có mipmap. `drawPicture` khớp nó vào một hình chữ nhật, với góc bo tròn và một cú đẩy chậm (bên dưới) |
| Hình trên layer canvas | `loadBitmap` và `drawImageFit` (`src/engine/media.ts`) trên một `Layer2D` | Một hình bị mask, cắt, xoay hoặc trộn với chữ vẽ | Canvas lo phần vẽ; lần upload của layer lo phần còn lại |
| Các pass của kit | `Blur`, `Liquid`, `Difference` (`src/scenes/parts/kit-post.ts`) | Bản mềm của một layer, goo, kính lỏng phủ lên hình của shot, blend difference | Mỗi cái là một hoặc nhiều pass toàn màn hình vào các target riêng; `Liquid.glass` và `Difference` ghi toàn bộ đầu ra của chúng, và đầu ra đó không được là target mà chúng đọc (`effects.md`, mục 15) |
| Clip | `ImageSequence` (`src/engine/media.ts`) | Footage thật, bản quay màn hình, nhân vật đã tách nền (keyed), dưới dạng ảnh đánh số, mỗi frame một file | Frame được nạp khi cần. Một still hay một frame export chờ frame của nó; studio hiện frame gần nhất đã nạp cho tới khi frame đúng tới |

| Chế độ blend | Cái gì đến được target |
|---|---|
| `normal` | Nguồn đè lên cái đang có: nguồn cộng target nhân với một trừ alpha nguồn |
| `add` | Nguồn cộng target. Alpha của target được giữ |
| `screen` | Nguồn cộng target nhân với một trừ màu nguồn |
| `multiply` | Target nhân màu nguồn. Hãy đưa cho nó một hình trên nền trắng; `premult` tắt cho chế độ này trừ khi được yêu cầu |
| `max` | Giá trị lớn hơn giữa nguồn và target, từng kênh một. Các nét chồng nhau không sáng thêm |
| `replace` | Nguồn, không blend |

Difference không phải là một chế độ blend của compositor, vì blending của WebGL không lấy được giá trị tuyệt đối. `Difference` của kit làm việc đó bằng một pass.

three.js vẽ vật đặc trước và vật trong suốt sau, bất kể thứ tự chúng được thêm vào. Một vật đặc nằm trong một vật trong suốt sẽ bị che trừ khi vật bên trong cũng được đánh dấu là trong suốt và `renderOrder` được đặt.

Thêm hai cái bẫy của three.js, từ một phim thử nghiệm: `PMREMGenerator.fromScene(scene, sigma, near, far)` mặc định cắt ở mặt phẳng xa 100 đơn vị, nên một phòng môi trường lớn hơn sẽ ra màu đen và kim loại chỉ được chiếu bởi đèn điểm (hãy truyền một mặt phẳng xa đủ chứa căn phòng). Và blur cùng depth of field của kit (`Blur` trong `kit-post.ts`) hoạt động trên các layer phẳng; một scene three.js muốn có depth of field phải tự viết pass của nó từ depth buffer, như builder của phim đó đã làm.

### Các format

Một thư mục phim có thể được xem ở nhiều format: 9:16, 1:1, 4:5 và 16:9 trong starter. Format chính là `width`, `height` và `format` của `src/project-config.ts`; các format khác được đặt tên trong `formats`. Format chính là format mà phim được làm và duyệt; các format khác là những góc nhìn của cùng các shot ở kích thước khác.

| Ở đâu | Chọn format thế nào |
|---|---|
| Studio | Tham số trang `format`, ví dụ `?format=16:9`. Nút Format và phím `F` nạp lại trang với format kế tiếp tại cùng thời điểm. Không có tham số thì hiện format chính |
| Công cụ capture | `--format 16:9` ở mọi chế độ. Still vào `out/stills-16x9/`, một sheet có `_16x9` trong tên, một bản export có `-16x9` |
| Build một file | `bun run single -- --format 1:1` tạo ra một trang mở ở format đó; nút Format của nó vẫn chuyển được |
| Code | `OUTPUT` của `src/project-config.ts` là format của trang (tên, rộng, cao); `W` và `H` của `src/engine/gl.ts` đi theo nó. `FORMATS` liệt kê tất cả và `formatSize(name)` cho ra một format |

Format được quyết định khi trang nạp, vì mọi render target lấy kích thước vào lúc đó. Những gì tự đi theo format: canvas, các target, hình của studio, viewport headless, `UNIT` (một pixel của cạnh ngắn 1080 pixel), `camForRect`, và các vùng của `src/scenes/parts/kit-frame.ts`. Mỗi format có bảng vùng riêng ở đó (`ZONE_TABLES`), viết theo pixel của frame tham chiếu riêng của nó; một format không có bảng sẽ lấy bảng của format có hình dạng gần nhất. `FORMAT` và `LANDSCAPE` trong kit cho scene biết nó đang vẽ format nào.

Những gì không tự đi theo: chỗ mà scene đặt mọi thứ. Một scene bố cục từ các vùng, `W`, `H`, `UNIT` và `camForRect` vẫn chạy được, nhưng một bố cục làm cho frame dọc hiếm khi đúng trong frame ngang: ở 9:16 chữ nằm dưới chủ thể, ở 16:9 thì nằm bên cạnh. Bố cục đó là việc của builder, theo từng format, với một still của mỗi khoảnh khắc chính ở mỗi format. Vị trí trong dữ liệu shot được viết theo pixel của format chính: timeline chuyển `focus` của một transition sang format đang hiển thị theo tỷ lệ của frame (một điểm ở một phần ba chiều ngang vẫn ở một phần ba chiều ngang), và `size` của chữ cái theo tỷ lệ cạnh ngắn, như `UNIT` (`src/timeline.ts`). Một focus vào chi tiết mà scene di chuyển ở format khác thì phải được scene dời đi, bằng cách tự đóng phần của nó với `handlesPortal`.

Các format được xem từng cái một, như mọi capture. Không có export song song nhiều format.

### Blending diễn ra trong ánh sáng tuyến tính

Mọi target giữ giá trị tuyến tính, và layer được giải mã sang tuyến tính trước khi blend. Vì vậy blending không hành xử như trong một chương trình vẽ, vốn blend các giá trị đã mã hóa.

| Trường hợp | Điều gì xảy ra | Cần làm gì |
|---|---|---|
| Một tấm nền tối gần như đục trên nền sáng | Vài phần trăm của nền lọt qua là vài phần trăm ánh sáng của nó, khi mã hóa cho màn hình thì thành một màu xám thấy rõ | Làm tấm nền đục hoàn toàn |
| Ánh sáng được cộng vào một target rồi target đó được composite sau | Nếu alpha của các nét cộng chồng lên nhau vượt quá 1, một lần composite `normal` của target đó sẽ làm tối cái nằm bên dưới | Giữ alpha của target trong khoảng 0 đến 1. Line batch làm điều này ở chế độ `add`. Hãy làm tương tự trong material của riêng bạn |
| Các nét cộng cắt nhau | Độ sáng tăng gấp đôi ở mỗi chỗ cắt và vượt ngưỡng bloom ở nơi không nét đơn nào vượt | Dùng `max`, hoặc đặt thứ không được phát sáng vào một batch riêng |
| Một target đã chứa màu nhân độ phủ | Nhân với alpha lần thứ hai làm tối mọi mép mềm | Composite với `premult: false` |

### Hình từ file

Ảnh, logo, ảnh chụp màn hình và clip nằm trong `media/` của thư mục phim. Server của studio phục vụ thư mục đó ở `/media/` giống như phục vụ `audio/` và `data/`, và build một file đóng gói nó. Đường dẫn trong scene được viết tương đối với thư mục phim, ví dụ `media/logo.png`.

| Phần | Làm gì |
|---|---|
| `loadBitmap(path, maxSize)` | Tải file và giải mã một lần thành `ImageBitmap`, được trình duyệt chuyển sang sRGB bất kể file mang color profile nào. `maxSize` (mặc định 4096) thu nhỏ hình lớn hơn với chất lượng cao, để một tấm ảnh máy ảnh không chiếm đầy bộ nhớ đồ họa |
| `ImageTexture` | `await this.logo.load('media/logo.png')` trong `init()`, mà engine sẽ await. `texture` là một texture sRGB 8-bit có mipmap, đỉnh của hình ở v = 1; `width`, `height` và `aspect` là kích thước của nó theo pixel. `set(picture)` upload một hình đã được giải mã sẵn, chẳng hạn một frame clip |
| `drawPicture(renderer, texture, [w, h], out, rect, style)` | Vẽ texture vào một hình chữ nhật theo pixel logic, đè lên những gì có trong `out`. `fit` là `cover` (mặc định: lấp đầy hình chữ nhật và phần thừa bị cắt bỏ), `contain` hoặc `stretch`; `align` định vị nó; `zoom` cùng `focus` đẩy vào một điểm của hình; `radius` bo tròn các góc; `opacity` và `tint` hoạt động như với compositor. Mép mềm một pixel vật lý |
| `drawImageFit(ctx, picture, rect, placement)` | Phép khớp tương tự trên một canvas context. Clip context trước cho mọi mask |
| `placePicture(w, h, rect, placement)` | Phép tính mà cả hai dùng: hình nằm ở đâu và phần nào của nó hiện ra |
| `ImageSequence({ pattern, count, fps })` | Một clip dưới dạng file đánh số: `media/run/%04d.jpg` đọc `0001.jpg` trở đi. `frameAt(s)` cho hình của frame tại giây thứ `s` của clip, giữ frame đầu trước đó và frame cuối sau đó; `textureAt(s)` cho nó dưới dạng texture, chỉ upload khi frame thay đổi. Các frame phía trước được nạp sớm (`ahead`, mặc định 12) và các frame ở xa được giải phóng (`keep`, 48). `index(s)` là số thứ tự frame, cho một nhãn nói frame nào đang hiện |
| `track`, `mediaPending`, `mediaSettled` | Mọi lần nạp đều được theo dõi. `Engine.renderSettled(t)` vẽ frame, chờ khi còn lần nạp đang treo, rồi vẽ lại cùng thời điểm như một lần seek. `window.__render.still`, `window.seek` và luồng export đều đi qua nó, nên một still hay một frame export hiện đúng frame clip của thời điểm của nó, không bao giờ là một frame vẫn đang nạp |

Cách xử lý sRGB là cách của các layer 2D: hình được upload dưới dạng byte 8-bit thuần (`plainTexture`) và chép vào một target sRGB 8-bit trong ánh sáng tuyến tính bởi `copyToSRGB` trong `src/engine/gl.ts`, cũng là pass mà `Layer2D` dùng. Một hình không bao giờ được upload thẳng vào texture sRGB, lối chậm của Chrome trên Windows (mục 11). Alpha giữ dạng straight, như với layer, nên một logo có mép mềm không bị viền tối khi composite.

Clip bắt đầu ở đâu là lựa chọn của scene: `this.clip.frameAt(f.t - f.start)` cho nó bắt đầu cùng shot; một clip cần rơi đúng một beat thì bắt đầu tại `sceneTime(audio, f, beats)`. Một clip 30 frame/giây trong phim 60 frame/giây hiện mỗi frame của nó trong hai frame đầu ra. Khi lấy mẫu sub-frame, một shutter vắt qua hai frame clip sẽ trộn chúng, như một máy quay thật.

**Tách frame của một video.** Một clip được chuyển thành ảnh đánh số một lần, bằng ffmpeg. Giải mã video là một lần chạy nặng: chỉ chạy khi chủ phim (owner) đồng ý, như một lần export, và giữ đoạn ngắn. Các lệnh, chạy từ thư mục phim:

```sh
# 3 seconds from 12.0 s of the source, 30 frames a second, 1280 px wide, JPEG of good quality
ffmpeg -ss 12.0 -t 3.0 -i source.mp4 -vf "fps=30,scale=1280:-2:flags=lanczos:in_color_matrix=bt709" -q:v 3 media/run/%04d.jpg
# with transparency (a keyed character from a ProRes 4444 or a WebM with alpha): PNG
ffmpeg -i character.mov -vf "fps=30,scale=720:-2:flags=lanczos" media/char/%04d.png
```

Số lượng (count) của chuỗi là số file được ghi ra. `in_color_matrix=bt709` chuyển màu của video HD sang RGB bằng ma trận của video HD; để mặc định, ffmpeg có thể dùng ma trận cũ hơn và làm lệch màu đỏ và xanh lá một chút. JPEG ở `-q:v 3` tốn khoảng 100 đến 200 kilobyte mỗi frame ở 1280 pixel, nên ba giây ở 30 frame là 10 đến 20 megabyte. Giữ clip ngắn và nhỏ, càng phải vậy với build một file, vốn đóng gói mọi file của `media/`. Chưa lệnh nào trong số này được chạy cho skill.

**Một phần tử video được giải mã khi seek (chưa dựng).** Cách khác để hiện một clip là một phần tử `<video>`: với mỗi frame, đặt `currentTime` vào giữa frame clip cần lấy, chờ sự kiện `seeked` và `requestVideoFrameCallback` của nó, rồi upload phần tử đó dưới dạng texture. Nó không cần tách frame và giữ file nhỏ, nhưng không chính xác. Một lần seek rơi vào frame mà bộ giải mã chọn, có thể khác nhau giữa các trình duyệt và giữa giải mã phần cứng với phần mềm; một file có keyframe thưa được giải mã từ keyframe gần nhất ở mỗi lần seek, rất chậm; Safari khắt khe hơn về việc seek trong một file nó chưa nạp hết. Mã hóa clip với mọi frame đều là keyframe (`-g 1`) giúp nó gần chính xác hơn và làm nó lớn hơn nhiều. Nó chưa được dựng, vì chuỗi ảnh đơn giản và chính xác và mọi frame nó hiện đều kiểm tra được bằng still. Chỉ dựng nó khi clip quá dài để tách frame, và kiểm tra nó bằng still tại các thời điểm ranh giới giữa các frame clip.

## 5. Timeline

`makeTimeline` (`src/timeline.ts`) được gọi một lần, sau khi dữ liệu audio đã nạp, và trả về các entry mà engine phát.

1. Danh sách shot được viết theo bar. Một script build kiểm tra nó và ghi thời điểm bắt đầu và kết thúc của mỗi shot tính bằng giây vào dữ liệu audio, dựa trên beat grid (`scripts/build-shot-files.py`, hoặc `bun run shots`). Các shot nối tiếp nhau không có khoảng trống hay chồng lấn.
2. Mỗi mục của danh sách đó trở thành một entry. Id của nó là shot id viết thường. Entry đầu tiên được kéo dài ngược về thời điểm 0 và entry cuối được kéo tới hết track.
3. Module scene được tìm theo tên file: `src/scenes/<shot id>.ts`. Khi file tồn tại, entry phát nó. Khi không, entry phát thẻ storyboard, thẻ này đọc mô tả của shot từ dữ liệu shot theo id của entry, in nó ra, và đánh dấu các beat của shot khi chúng trôi qua. Cả phim có thể phát cùng nhạc trước khi dựng bất kỳ shot nào.
4. Transition dẫn vào shot, nếu dữ liệu shot có chỉ định, được đặt trên beat grid và lưu vào entry (mục 6).
5. Một entry overlay được thêm vào, chạy suốt chiều dài của phim.

| Field của entry | Ý nghĩa |
|---|---|
| `id` | Shot id. Cũng là cái mà `--only` của công cụ capture chỉ định |
| `file` | Module phát entry. Nhiều entry có thể dùng chung một module; hot swap tìm chúng theo field này |
| `load` | Bộ nạp lười (lazy loader) của module. Một module bị thiếu hoặc hỏng không bao giờ làm hỏng bản build |
| `start`, `end` | Cửa sổ, tính bằng giây song time |
| `post` | Thiết lập post cho entry. Các thiết lập mà chính scene trả về sẽ thắng chúng |
| `params` | Các giá trị tự do được truyền cho scene dưới dạng `ctx.params` |
| `maxSamples` | Giới hạn trên cho việc lấy mẫu sub-frame thích ứng khi entry đang trên màn hình. Chỉ cho export |
| `overlay` | Đánh dấu một entry overlay |
| `into` | Transition dẫn vào entry |

Một entry overlay được vẽ sau mọi entry khác và sau pass transition, đè lên hình hoàn chỉnh. Nó không tham gia vào transition: pass không bao giờ bẻ cong nó. Chuỗi post chạy sau nó, nên shake, zoom, flash, đảo màu và viền màu (colour fringing) tác động lên chữ overlay cùng với phần còn lại của frame. Một overlay có thể trả về thiết lập post; chúng được áp dụng sau cùng.

Khi hai entry không phải overlay chồng lên nhau về thời gian, engine crossfade từ entry trước sang entry sau qua đoạn chồng, trừ khi scene sau đặt `handlesTransition`. Timeline của starter không tạo entry chồng nhau nào: các cú cắt của nó là hard cut trên một beat, và mọi thứ quanh một cú cắt là việc của pass transition.

Chỉ các file nằm trực tiếp trong `src/scenes/` mới là module scene. Các file mà scene dùng chung hoặc được tách ra thì nằm trong `src/scenes/parts/`. Một helper đặt trực tiếp trong `src/scenes/` bị tính là được timeline import, và lưu nó sẽ nạp lại toàn bộ trang studio.

## 6. Pass transition

Mục này là cơ chế. Các loại transition, và khi nào dùng loại nào, nằm trong `transitions.md`.

Một transition thuộc về shot mà nó dẫn vào. Dữ liệu shot cho biết loại của nó, một lead (đoạn dẫn trước) và một tail (đoạn đuôi) tính bằng beat, và tùy chọn một điểm focus theo pixel logic của format chính (được chuyển sang format khác theo tỷ lệ, mục 4, "Các format"), một hướng, một màu lấp đầy (`colour`, một khóa bảng màu, cho `dip`, `cover` và `flood`), cùng các chữ cái và kích thước cho loại đi xuyên qua một chữ cái. Timeline biến chúng thành ba thời điểm song time: cú cắt là lúc bắt đầu shot, lead bắt đầu `lead` beat trước cú cắt, tail kết thúc `tail` beat sau nó, tất cả đọc từ beat grid.

| Phần | Cách hoạt động |
|---|---|
| Cửa sổ | Với bất kỳ thời điểm nào từ đầu lead tới cuối tail, khi cả hai shot đều đã nạp, engine đi theo lối transition thay vì lối thường |
| Hai hình | Shot đang ra được vẽ vào một target và shot đang vào được vẽ vào một target khác. Các loại hiển thị cả hai shot vẽ cả hai ở mọi frame của cửa sổ; các loại khác chỉ vẽ shot đang phát |
| Frame bị giữ | Sau cú cắt, shot đang ra được giữ ở frame cuối của nó, một bước frame trước cú cắt. Trước cú cắt, shot đang vào được giữ ở frame đầu của nó. Một scene chỉ bao giờ được hỏi một thời điểm nằm trong cửa sổ riêng của nó |
| Tiến độ | Pass nhận số beat tính từ cú cắt, tiến độ qua lead, qua tail và qua cả cửa sổ, việc cú cắt đã qua hay chưa, số thứ tự frame, focus và hướng |
| Bẻ cong thời gian | Một shot là hàm của thời gian, nên engine có thể hỏi shot đang ra bất kỳ thời điểm nào của riêng nó. Một loại phát lại những khoảnh khắc đầu của lead theo các lát giảm một nửa sau mỗi beat. Các loại dẫn vào một cú drop đóng băng shot đang ra trong một phần tư beat cuối trước cú cắt |
| Pass | Một shader toàn màn hình đọc hai hình và ghi frame hoàn chỉnh. Nó không giữ state giữa các frame |
| Màu lấp đầy | `dip`, `cover` và `flood` lấp đầy frame bằng màu bảng màu của `colour` trong dữ liệu shot (mặc định là ink cho dip, signal cho các loại khác). Timeline truyền nó tiếp; một khóa không biết sẽ quay về mặc định |
| Thiết lập post | Bên trên những gì shot đang phát yêu cầu, transition nhân zoom, cộng thêm vào shake và viền màu, lấy flash lớn hơn, và đặt đảo màu. Bốn loại không gì khác ngoài một thay đổi như vậy và không chạy pass |
| Portal | Với `zoom-in`, trong lead, một scene đang ra có `handlesPortal` nhận frame đầu của shot kế tiếp dưới dạng `f.portal`. Với `pull-out`, trong tail, một scene đang vào có `handlesPortal` nhận frame cuối của shot trước. `f.portalK` chạy từ 0 đến 1. Scene hiện texture đó lên chi tiết và điều khiển camera của nó; hình của nó là frame và pass không chạy |
| Bản thay thế (stand-in) | Cho tới khi một scene đặt `handlesPortal`, pass zoom giữa hai hình hoàn chỉnh. Một transition được đánh dấu là stand-in khi một trong hai shot vẫn còn là thẻ storyboard. Khi đó, một hành trình camera giữa hai shot được phát thành một cú whip, và một cú khớp hình dạng (match of shapes) thành một cú punch nhỏ. Giữa hai shot đã dựng, engine không làm gì cho hai loại đó: cú cắt là của chúng |

Cách một shot Canvas2D hiện portal, như một builder đã làm trong một phim thử nghiệm: frame của shot kề bên là một texture của toàn frame, nên ánh xạ nó sao cho chi tiết của shot kề rơi đúng vào chi tiết của shot này. Với `s` là tỷ lệ giữa hai kích thước của chi tiết trên màn hình và `(tx, ty)` là độ dời, trước tiên xóa target về màu nền, rồi `comp.draw(renderer, f.portal, out, { mode: 'replace', scale: [1 / s, 1 / s], offset: [-(vx - 0.5) / s, -(vy - 0.5) / s], premult: false })`, trong đó `(vx, vy)` là tâm của frame đã ánh xạ theo tọa độ texture (y hướng lên). Rồi vẽ layer riêng của shot này đè lên với một lỗ ở chỗ portal hiện ra. Tại cú cắt, phép ánh xạ là đồng nhất, nên việc chuyển giao là chính xác.

Ba hệ quả cho lead:

- Frame bị giữ không được cache. Shot bị giữ được vẽ lại ở mọi frame của cửa sổ, với `dt` bằng 0 và `seeked` là true, nên một transition hiển thị cả hai shot tốn bằng hai shot trong suốt thời gian nó kéo dài. Một scene stateful sẽ bị reset và preroll ở mỗi frame đó.
- Builder phải biết lead của transition của shot kế tiếp và tail của shot mình. Những beat cuối của một shot phát dưới lead, và những beat đầu đến dưới tail. Những gì quan trọng trong shot phải vừa giữa hai đoạn đó.
- Một capture chỉ phát transition khi các shot ở cả hai bên cú cắt đều đã nạp. Khi `--only` chỉ định một trong hai, cú cắt hiện ra trơn.

## 7. Chuỗi post

Chuỗi post (`src/engine/post.ts`) lấy frame đã composite trong ánh sáng tuyến tính và ghi ra frame 8-bit được hiển thị. Các thiết lập được dựng lại ở mọi frame, nên không có gì mang sang từ frame trước.

| Thiết lập | Làm gì | Mặc định của engine | Nền tối | Nền sáng |
|---|---|---|---|---|
| `exposure` | Nhân frame trước tone shoulder | 1 | | |
| `bloom` | Cường độ glow quanh các giá trị sáng | 0.55 | 0.7 | 0 |
| `bloomThreshold` | Độ sáng tuyến tính mà quanh đó bloom bắt đầu | 0.85 | 1.0 | 4 |
| `bloomKnee` | Độ mềm của điểm bắt đầu đó: bloom bắt đầu ở ngưỡng trừ knee | 0.5 | 0.2 | 0.2 |
| `bloomRadius` | Độ lan của glow, 0 đến 1 | 0.75 | 0.75 | 0.75 |
| `halation` | Quầng đỏ cam quanh vùng sáng, như trên phim nhựa | 0.25 | 0.25 | 0 |
| `ca` | Viền màu, tính bằng pixel ở mép frame | 1.2 | 0.4 | 0.25 |
| `grain` | Hạt phim (film grain), mạnh nhất ở vùng trung tính | 0.055 | 0.045 | 0.05 |
| `vignette` | Tối dần về các góc, 0 đến 1 | 0.35 | 0.4 | 0.18 |
| `fade` | Mờ dần về đen, 0 đến 1 | 0 | | |
| `flash` | Cộng màu bảng màu `fg` vào toàn frame | 0 | | |
| `shake` | Dịch chuyển frame, tính bằng pixel | `[0, 0]` | | |
| `zoom` | Phóng to frame quanh tâm của nó | 1 | | |
| `invert` | Biến tối thành sáng và sáng thành tối, 0 đến 1 | 0 | | |
| `hue` | Xoay mọi màu quanh bánh xe màu, tính bằng radian; xám vẫn là xám | 0 | | |
| `kaleido` | Số khu vực đối xứng gương quanh tâm, 0 là tắt; `kaleidoTurn` xoay chúng | 0 | | |
| `fisheye` | -1 đến 0.9: trên 0 thì giữa frame phồng lên, dưới 0 thì co lại | 0 | | |
| `bulge` | -1 đến 0.9: một thấu kính bên trong `bulgeRadius` quanh `bulgeAt` (mặc định 240 px và tâm frame) | 0 | | |
| `mosaic` | Kích thước ô tính bằng pixel, 0 là tắt | 0 | | |
| `glitch` | 0 đến 1: các dải của frame bị xé ngang, thay đổi mỗi hai frame | 0 | | |
| `crt` | 0 đến 1: kính cong, scanline, mặt nạ phosphor, góc tối | 0 | | |
| `tone` | 1: tone shoulder; 0: tắt, để màu phẳng ra đúng như bảng màu cho (shoulder làm tối một nền giấy sáng đi vài mức) | 1 | | |
| `dither` | 1: một lớp dither một mức thay đổi mỗi frame, chống banding; 0: tắt. Với `grain` 0 và `dither` 0, hai frame bị giữ giống hệt nhau | 1 | | |

Một màu phẳng phải ra đúng như bảng màu cho (màu thương hiệu, một phần khớp với bản thiết kế): composite layer với `mode: 'replace'` và không tint, rồi trả về `{ tone: 0, dither: 0, grain: 0, bloom: 0, halation: 0, ca: 0, vignette: 0 }`, bảy thiết lập bật theo mặc định (README của starter, phần Adding a scene module). Đây là công cụ cho khi tác phẩm cần, không phải mặc định: hầu hết phim muốn có lớp hoàn thiện.

Hai preset là `POST_DARK` và `POST_LIGHT` trong `src/scenes/parts/kit-post.ts`. Ô trống nghĩa là preset giữ mặc định của engine. Pixel art trả về `POST_PIXEL` từ `src/scenes/parts/kit-pixel.ts`, cái này tắt lớp hoàn thiện.

Thứ tự bên trong chuỗi là cố định: zoom và shake, kaleidoscope, fisheye, bulge, độ cong CRT, mosaic và xé glitch (những cái này dời chỗ mà một pixel nhìn vào, và bloom dời theo chúng), viền màu cùng phần tách của glitch, cộng bloom và halation, exposure, xoay hue, tone shoulder, đảo màu, flash, vignette, fade, scanline, mặt nạ và góc của CRT, mã hóa cho màn hình, grain, dither. Tone shoulder giữ nguyên các giá trị dưới 0.72, uốn các giá trị sáng hơn về phía 1, và kéo các giá trị rất sáng về phía trắng.

Các thiết lập được gộp theo thứ tự này, cái sau thắng: mặc định của engine, `post` của entry trên timeline, những gì scene trả về từ `render()`, thay đổi mà một transition tạo ra, những gì overlay trả về. Một scene ghi đè theo từng frame bằng cách trả về một object chỉ chứa những thiết lập mà khoảnh khắc của nó cần:

```ts
return { ...POST_DARK, bloom: 0.85, shake: [shx, shy], zoom: 1 + 0.03 * hit(k.beats, NAME, 0.3) };
```

### Chữ nằm dưới ngưỡng bloom

Bloom đo một pixel theo kênh lớn nhất của nó và bắt đầu ở `bloomThreshold` trừ `bloomKnee`, tức là 0.8 với preset tối. Chữ và đường viền phải nằm dưới giá trị đó. Chỉ thứ gì cố ý phát sáng mới được vẽ trên 1 trong ánh sáng tuyến tính. Một màu chữ sáng tự nó có thể vượt 0.8, nên kit cung cấp một tint, `TYPE_TINT`, để composite các layer chữ trên nền tối. Trên nền sáng, preset đặt ngưỡng ở 4 và cường độ ở 0: không có gì phát sáng.

Từ thực tế: ở phim đầu tiên, chữ sáng ra với glow màu cam trong những still đầu. Cách sửa là ngưỡng 1.0 và một tint làm giảm layer chữ. Cả hai được đưa vào kit, không phải vào từng shot.

## 8. Công cụ capture

`scripts/render.ts` điều khiển app trong một trình duyệt headless qua trang export của nó (`?export=1`) và giao diện mà trang đó công bố dưới tên `window.__render`. Nó được chạy bằng `bun`, từ thư mục phim.

```sh
bun scripts/render.ts stills --t 1.5,23,40.2 [--only id1,id2] [--out dir]
bun scripts/render.ts stills --beats 116,117.5,119 --only <shot id>
bun scripts/render.ts sheet --from 20 --to 35 [--n 12] [--cols 4] [--only ids] [--out file.png]
bun scripts/render.ts sheet --cuts --cols 4
bun scripts/render.ts perf --from 20 --to 25 [--only ids]
bun scripts/render.ts gpu
bun scripts/render.ts stills --format 16:9 --t 5,18.2                      # another format of the film
bun scripts/render.ts stills --page out/single/<title>.html --t 5         # the single-file build, from disk
```

| Chế độ | Cho ra |
|---|---|
| `stills` | Một ảnh cho mỗi thời điểm được hỏi, ở kích thước đầy đủ, đặt tên theo thời điểm của nó |
| `sheet` | Một contact sheet: thumbnail 480 pixel ở cạnh dài, mỗi cái có nhãn thời điểm. Các thời điểm được rải đều giữa `--from` và `--to`, hoặc liệt kê bằng `--times`, hoặc lấy quanh mọi cú cắt bằng `--cuts` (hai frame trước mỗi cú cắt và hai frame sau) |
| `perf` | Thời gian frame qua một đoạn: số frame, trung bình, trung vị, phân vị 95, tối đa |
| `gpu` | Tên renderer đồ họa mà trình duyệt headless dùng |
| `video` | Export ra file video. Bị từ chối trừ khi owner yêu cầu (xem bên dưới) |

| Tùy chọn | Chế độ | Ý nghĩa |
|---|---|---|
| `--t` | stills | Thời điểm tính bằng giây, cách nhau bằng dấu phẩy |
| `--frames` | stills, sheet | Số thứ tự frame đầu ra. Frame n ở thời điểm n chia cho frame rate |
| `--beats` | stills, sheet | Chỉ số beat của cả track, 0 ở beat đầu tiên. Cho phép phân số |
| `--exact` | stills, sheet | Render đúng thời điểm như đã cho, không dời nó về một frame |
| `--only` | tất cả | Id của các shot cần nạp. Overlay luôn được nạp. Shot không được nạp sẽ vẽ màu đỏ sẫm |
| `--out` | stills, sheet, video | Thư mục cho still, file cho sheet hoặc video. Mặc định nằm trong `out/` |
| `--from`, `--to` | sheet, perf, video | Đoạn thời gian, tính bằng giây |
| `--n`, `--cols` | sheet | Số thumbnail, và số thumbnail trên một hàng |
| `--scale` | tất cả | Render ở bội số nguyên của kích thước đã cấu hình |
| `--format` | tất cả | Một trong các format của `src/project-config.ts`; bỏ trống thì là format chính. Một tên không biết sẽ dừng công cụ trước khi trình duyệt khởi động |
| `--page` | tất cả | Capture bản build một file này từ ổ đĩa thay vì từ server. Trang được mở dưới dạng file; không server nào được khởi động |
| `--url` | tất cả | Dùng server ở địa chỉ này, ví dụ studio, thay vì một server riêng. Báo lỗi nếu phim này không trả lời ở đó |
| `--angle` | tất cả | Backend đồ họa của Chrome: `metal`, `d3d11`, `gl`, `vulkan`, `swiftshader` hoặc `default`. Không có nó thì công cụ chọn theo hệ thống (mục 11) |
| `--headed` | tất cả | Hiện cửa sổ trình duyệt |
| `--samples`, `--shutter`, `--min-samples`, `--max-samples`, `--tol` | stills, perf, video | Lấy mẫu sub-frame: mỗi frame là trung bình của nhiều sub-frame rải trên một phần của bước frame, làm tải nhân lên theo số lượng của chúng. `--samples auto` chọn 4, 12, 36, 108 hoặc 324 mỗi frame và không chạy được scene stateful |

**Export video.** Chế độ này có tồn tại: các frame được stream vào một encoder, và nhạc được thêm vào. Công cụ thoát với mã 2 trừ khi biến môi trường `OWNER_ASKED_FOR_VIDEO` là `yes`. Lead chỉ đặt biến đó khi owner đã yêu cầu một file video trong cuộc hội thoại hiện tại. Công cụ không từ chối lấy mẫu sub-frame ở các chế độ khác; hãy coi nó là một phần của export và để ở một mẫu khi review.

**Hình được chờ.** `still` và luồng export vẽ mỗi frame qua `renderSettled`, cái này chờ các ảnh và frame clip vẫn đang nạp rồi vẽ lại frame (mục 4). `sheet` chờ theo cùng cách. `perf` thì không: nó đo phần vẽ, và một frame clip chưa nạp xong được vẽ từ frame gần nhất.

**Lock.** Các capture chạy từng cái một cho cả repository, bất kể ai khởi động chúng. Lock là một thư mục, `.render.lock`, chứa process id của chủ sở hữu nó. Lần chạy thứ hai sẽ chờ và thử lại mỗi nửa giây. Một lock mà chủ của nó không còn chạy sẽ bị xóa. Một lần chạy đã chờ 15 phút sẽ bỏ cuộc. Lock được nhả khi lần chạy kết thúc hoặc bị ngắt. Công cụ tìm thư mục cho lock bằng cách đi ngược lên từ thư mục phim (`lockHome` trong `scripts/render.ts`): thư mục được chỉ định bởi biến môi trường `RENDER_LOCK_DIR` khi nó được đặt, nếu không thì thư mục gần nhất phía trên có chứa `.git`, nếu không thì thư mục gần nhất có chứa `CLAUDE.md` hoặc `AGENTS.md`, nếu không nữa thì thư mục tạm của hệ thống. Mọi phim dưới một repository dùng chung lock, dù thư mục của nó nằm sâu đến đâu.

**Server.** Mặc định, công cụ khởi động một server phát triển riêng trên một cổng chọn trong khoảng 5300 đến 5799, dưới dạng một tiến trình `node` chạy Vite, với live reload bị tắt (`RENDER_NO_HMR=1`) để một file được lưu trong lúc capture không thể nạp lại trang, và dừng nó khi lần chạy kết thúc hoặc bị ngắt. Trình duyệt được đóng trong cùng bước đó. Với `--url`, nó dùng server ở địa chỉ đó thay thế, ví dụ studio, chỉ khi trang mang dấu nhận diện của phim này: một phần tử `meta` tên `render-app` có giá trị là `appMarker()` của `src/project-config.ts`, chứa tiêu đề của phim. Nếu phim này không trả lời ở đó, công cụ dừng với một lỗi nêu tên phim đang trả lời. Studio bật live reload, nên đừng lưu file khi một capture đang chạy trên nó.

**Thời điểm được bắt về frame.** Trong `stills`, mọi thời điểm được dời về frame đầu ra gần nhất, vì đó là những thời điểm duy nhất phim được phát trong một bản export, và một thời điểm nằm giữa hai frame có thể in một giá trị đổi theo bậc hai lần. Khi thời điểm được hỏi là beat đầu tiên của một shot và frame gần nhất rơi vào shot trước, frame kế tiếp được lấy. `--frames` theo định nghĩa là chính xác. `sheet` bắt thời điểm theo cùng cách. Với `--exact`, cả hai render thời điểm như đã cho: studio phát giữa các frame, nên một lỗi chỉ hiện ra ngoài lưới được tìm thấy theo cách này (`quality-gates.md`, phép kiểm tra chuyển động). `sheet` luôn render một mẫu.

**Thời gian frame bao gồm những gì.** `perf` đo, cho mọi frame của đoạn, việc render frame, việc chờ card đồ họa hoàn tất, và việc đọc pixel hoàn chỉnh ngược về bộ nhớ, như một bản export sẽ làm. Nó không bao gồm việc vẽ ra màn hình. Riêng việc đọc đã tốn vài mili giây, nên con số là cận trên của những gì studio phải trả. Hãy đo một shot gần như trống trên cùng máy để biết phần cố định.

Công cụ in lỗi scene và các lỗi console, lỗi trang và request thất bại của trình duyệt sau mỗi lần chạy. Đọc chúng trước khi xem ảnh.

### Thiết lập export, kích thước, và các phép kiểm tra một file video

Chưa có gì trong phần này được chạy cho skill: quy tắc của owner cấm export trừ khi owner yêu cầu một file video trong cuộc hội thoại hiện tại. Nó mô tả những gì `video` làm và những gì cần chạy khi owner đã yêu cầu.

| Thiết lập của `video` | Giá trị | Cờ để thay đổi |
|---|---|---|
| Frame | RGBA thô từ trang, `PROJECT.fps`, kích thước của format nhân `--scale`, được encoder lật cho đứng thẳng | `--format`, `--scale`, `--from`, `--to` |
| Encoder | H.264 (`libx264`), `-preset slow`, `-crf 16`, `-tune grain`, `-x264-params aq-mode=3`, `yuv420p` | `--crf`, `--preset`, `--x264`, `--threads` |
| Màu | Chuyển đổi bằng ma trận BT.709 sang dải giới hạn (limited range), và gắn thẻ là BT.709 (`-colorspace`, `-color_primaries`, `-color_trc`, `-color_range tv`) | không có |
| Âm thanh | `audioFile` của cấu hình dự án từ `--from` trong suốt chiều dài của đoạn, AAC ở 320 kbit/s, `-shortest` | `--noaudio` |
| File | `-movflags +faststart`, `out/<title>.mp4` (thêm `-<format>` cho format khác format chính) | `--out` |
| Motion blur | Các sub-frame được lấy trung bình trong trang trước khi mã hóa | `--samples`, `--shutter` |

CRF 16 với tuning grain là một bản master: gần như trong suốt (không thấy khác biệt) và lớn, thường 20 đến 60 megabyte mỗi phút ở 1080 x 1920 và 60 frame/giây, lớn hơn nhiều với một phim nhiều hạt, rối. Một yêu cầu "dưới 30 MB", 720p, hay một kích thước mà nền tảng chấp nhận được đáp ứng bằng một lần mã hóa thứ hai từ bản master đó, không phải bằng render lại:

```sh
# a size target: bitrate = size in bits / duration, less the sound, with a few per cent of margin
#   30 MB over 45 s with 128 kbit/s of sound: 30*8*1000/45 * 0.96 - 128 = about 4990 kbit/s
ffmpeg -y -i out/film.mp4 -c:v libx264 -preset slow -b:v 4990k -pass 1 -an -f null NUL      # /dev/null on macOS and Linux
ffmpeg -y -i out/film.mp4 -c:v libx264 -preset slow -b:v 4990k -pass 2 -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -c:a aac -b:a 128k -movflags +faststart out/film-30mb.mp4
# 720p from a 1080p master (1280 x 720 for 16:9, 720 x 1280 for 9:16), by quality instead of size
ffmpeg -y -i out/film.mp4 -vf "scale=1280:720:flags=lanczos" -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -c:a aac -b:a 160k -movflags +faststart out/film-720p.mp4
```

Hai pass đạt kích thước trong vòng vài phần trăm; một pass chỉ với `-b:v` có thể trượt. Một kích thước buộc bitrate thấp sẽ lộ ra trước tiên ở hạt và các nét mảnh: hạ `grain` trong thiết lập post cho phiên bản đó thay vì để encoder làm nhòe nó. Mọi lần mã hóa đều là một lần chạy nặng và cần owner đồng ý như chính lần export.

Các phép kiểm tra trên một file đã export. Mỗi cái đọc toàn bộ file, nên chạy chúng một lần, sau khi export, từng cái một:

| Kiểm tra | Lệnh | Đạt |
|---|---|---|
| Số frame và frame rate | `ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames,r_frame_rate,avg_frame_rate,width,height -of default=nw=1 out/film.mp4` | `nb_read_frames` bằng `round(to * fps) - round(from * fps)`; cả hai rate đều là `fps` của phim; kích thước là của format nhân `--scale` |
| Thời lượng chính xác, hình và tiếng | `ffprobe -v error -show_entries stream=codec_type,duration:format=duration -of default=nw=1 out/film.mp4` | Luồng video kéo dài bằng số frame chia cho `fps`. Tiếng không dài hơn hình (công cụ truyền `-shortest`) và không ngắn hơn quá một frame |
| Timestamp đều | `ffprobe -v error -select_streams v:0 -show_entries packet=pts_time -of csv=p=0 out/film.mp4 \| sort -n \| awk 'NR>1{d=$1-p; if (d<0.99/F \|\| d>1.01/F) n++} {p=$1} END{print n+0}' F=60` | In ra 0: mọi bước giữa hai frame là một frame. Thay 60 bằng `fps` của phim |
| Pop một frame | `ffmpeg -i out/film.mp4 -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=out/diff.txt" -an -f null -` | Trong `out/diff.txt`, một frame có độ khác biệt so với frame trước lớn hơn ba lần so với cả hai frame lân cận, ở một frame không phải cú cắt, là một pop: một frame được vẽ từ state sai. Chụp still của nó và của các frame hai bên |

Một pop tìm thấy theo cách này được sửa trong scene, rồi kiểm tra bằng still của ba frame đó, không phải bằng một lần export khác.

## 9. Trang studio

| Tính năng | Cách làm |
|---|---|
| Playback | Trang phát bản nhạc nén và hỏi engine frame tại song time của phần tử audio |
| Danh sách shot | Mọi shot theo thứ tự, nhóm theo section, kèm thời điểm bắt đầu và việc nó đã dựng hay vẫn là thẻ. Một cú click nhảy tới shot. Trang đếm số shot đã dựng |
| Phím | Space phát và dừng. `[` và `]` bước giữa các shot. Phím mũi tên dời một giây, năm giây khi giữ shift. `,` và `.` dời một frame. `L` lặp shot. `M` chuyển giữa các phiên bản của nhạc, rồi tới tiếng click của beat grid, rồi im lặng |
| Hiển thị số liệu | Song time, bar, beat, và frame rate khi đang phát |
| Tham số trang | `t` bắt đầu tại một thời điểm tính bằng giây. `only` nạp các shot được chỉ định. `scale` nhân kích thước đầu ra. `format` hiện một format khác của phim (mục 4, "Các format"). `export` biến trang thành trang export |
| Chuyển format | Nút Format và phím `F` nạp lại trang ở format kế tiếp, tại cùng thời điểm |
| `window.seek(t)` | Vẽ frame của song time `t` và resolve khi nó đã lên canvas với mọi hình đã nạp. Trong studio nó cũng tạm dừng player ở đó. Trên trang export nó là `window.__render.still(t)` không có giá trị trả về. `window.duration` là chiều dài của phim. Đây là hàm mà các yêu cầu hỏi "một hàm `seek(t)`" muốn nói tới; công cụ capture dùng `window.__render`, vốn có nhiều thành phần hơn |
| Hot swap | Một module scene được lưu sẽ được import lại và mọi entry phát nó được dựng lại từ nó. Trang giữ nguyên vị trí. Một file được lưu trong `src/scenes/parts/` đến được các scene import nó |
| Lỗi | Các scene nạp thất bại được liệt kê ở đầu trang |

Một trang đang tạm dừng không vẽ gì cho tới khi thời gian thay đổi, hoặc cho tới khi một hình mà nó đang chờ đã tới. Studio cần server phát triển (`bun run studio`, trên `studioPort` của `src/project-config.ts`, 5180 trong starter). Dừng server khi xem xong. Build một file (`bun run single`) là cùng trang đó mà không cần server, để bàn giao phim (`studio-viewer.md`, mục 11).

## 10. Ngân sách hiệu năng

Studio phát theo thời gian thực, nên bước frame là trần: 16.7 mili giây ở 60 frame/giây, cho shot, overlay, chuỗi post và trình duyệt cộng lại. Mục tiêu giao cho builder là 8 mili giây hoặc ít hơn, theo số `perf` báo.

Từ thực tế: trên máy mà các phim được làm (Apple M4 Max, Chrome, 1080 x 1920, một mẫu), các shot đo được trung bình 7.3 đến 12 mili giây. Một shot gần như trống đo được khoảng 7.3, phần lớn là việc đọc pixel, nên chi phí riêng của một shot là phần chênh lệch: từ một phần nhỏ của mili giây tới vài mili giây. Frame rate khi phát thật trong studio chưa được đo trên máy của owner.

| Cái gì tốn nhất | Đo được hoặc quan sát được | Cách khắc phục |
|---|---|---|
| Canvas2D `shadowBlur` và blur của canvas | Một shot giảm từ 13.1 xuống 9.4 mili giây khi bỏ bóng đổ | Vẽ hình mềm một lần, hoặc trong shader |
| Phần tĩnh được vẽ lại ở mọi frame | Một shot đo được 11.8 mili giây trước khi các phần tĩnh của nó được cache | Vẽ chúng một lần vào một canvas riêng rồi chép canvas đó |
| Chữ lớn chuyển động dưới camera trên một layer toàn frame | Các shot vượt mục tiêu đều có điểm chung này | Cache các dòng chữ dưới dạng bitmap |
| Định dạng số theo locale, nhiều lần mỗi frame | Một shot tăng lên 11 mili giây | Một hàm định dạng đơn giản |
| Một shader nặng ở độ phân giải đầy đủ | Một trường sóng tốn 3.5 mili giây ở độ phân giải đầy đủ và trông y hệt ở một nửa | Một target nhỏ hơn, composite phóng lên |
| Tài nguyên được dựng khi dùng lần đầu | Các frame đầu 48, 90 và 178 mili giây | Dựng chúng trong `init()` |
| Một transition hiển thị cả hai shot | Hai shot được vẽ cho mọi frame của cửa sổ | Giữ lead và tail ngắn |
| Upload layer theo lối chậm | Xem mục 11, Windows | Đo trên chính máy đó |
| Lấy mẫu sub-frame và scale đầu ra | Tải nhân lên theo số sub-frame, hoặc theo bình phương của scale | Chỉ cho export |

Studio không có motion blur. Thứ gì cần nhòe thì được shot vẽ thành vệt nhòe.

## 11. Tính di động (portability)

| Hệ điều hành | Backend đồ họa của trình duyệt | Cờ khởi chạy |
|---|---|---|
| macOS | Metal | `--use-angle=metal` |
| Windows | Direct3D 11 | `--use-angle=d3d11` |
| Linux | OpenGL, hoặc Vulkan | `--use-angle=gl`, `--use-angle=vulkan` |
| Bất kỳ, không có card đồ họa | Render bằng phần mềm | `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader` |
| Bất kỳ | Backend đầu tiên khởi động được | `--use-angle=default` |

Công cụ capture chọn cờ theo hệ thống (`angleArgs` trong `scripts/render.ts`): `metal` trên macOS, `d3d11` trên Windows, `gl` trên Linux. `--angle` chỉ định một backend khác, và `--angle swiftshader` truyền ba cờ của render phần mềm. App tham chiếu truyền `--use-angle=metal` trên mọi hệ thống. Trên một máy mới, hãy chạy chế độ `gpu` trước và đọc cái tên nó in ra. Một tên có chứa SwiftShader nghĩa là render phần mềm, và mọi thời gian frame đo ở đó đều vô nghĩa đối với playback. Dưới Windows Subsystem for Linux, hãy giả định là render phần mềm cho tới khi đầu dò nói khác. Công cụ khởi chạy Google Chrome đã cài (`channel: 'chrome'`), vốn phải có sẵn.

| Khoảng trống | Hệ quả | Quy tắc |
|---|---|---|
| Công cụ capture dùng Chrome; owner có thể xem bằng Safari | Một shot có thể đúng trong mọi capture mà trống trơn với owner | Hỏi owner xem bằng trình duyệt nào trước khi dựng shot đầu tiên |
| Canvas `filter` không có trong bản Safari mà owner dùng | Đặt nó không có tác dụng gì. Engine chỉ vá thuộc tính ở nơi nó tồn tại | Scene không dùng `ctx.filter` |
| Canvas `letterSpacing` có từ Safari 18.4 | Thiếu nó thì chữ bị dàn sát hơn, không có lỗi | Bố cục không được phụ thuộc vào nó để vừa |
| WebKit mà công cụ tự động hóa trình duyệt cài không phải là Safari | Nó gần Safari trên macOS nhất, và khác nhiều nhất ở phần phát media | Kiểm tra phim trên WebKit không thay thế được việc owner tự xem |
| Target full float không có ở mọi nơi | Engine chỉ dùng chúng cho lấy mẫu sub-frame. Target của shot là half float | Giữ target riêng của shot ở half float, đúng như `makeRT` cho |

Từ thực tế: một shot hai lần bị báo là trống trong khi capture vẫn ổn. Nguyên nhân là thiếu canvas `filter`: engine vá thuộc tính mà không kiểm tra nó có tồn tại không, và mọi layer có scale khác 1 đều ném lỗi khi `clear()`. Lỗi đó nằm sẵn trong đầu ra của server phát triển từ đầu, kèm id của scene. Một stack có các frame `@[native code]` là WebKit.

**Upload canvas chậm trên Windows.** App tham chiếu upload mỗi canvas `Layer2D` thẳng vào một texture sRGB ở mọi frame. Trong Chrome trên Windows, lần upload đó có thể đi theo lối chậm; trình theo dõi issue của trình duyệt gắn nó với backend Direct3D 11. Starter upload canvas dưới dạng byte 8-bit thuần, không chuyển đổi màu và không lật, và một pass nhỏ (`LAYER_COPY_FRAG` trong `src/engine/gl.ts`) đọc nó từng texel, chuyển giá trị sang ánh sáng tuyến tính, lật các hàng và ghi vào một target sRGB 8-bit mà scene lấy mẫu như trước. Giao diện của `Layer2D` không đổi. Một frame chậm trên máy này không phải là bằng chứng về máy khác, nên hãy đo trên chính máy đang xét, và so sánh với một backend khác trước khi thay đổi code.

Từ thực tế: trên macOS với Metal, upload sRGB một frame đầy đủ đo được 0.5 mili giây, bằng với upload thuần. Trên máy Windows của owner thì nó chậm, và một cách sửa cùng ý tưởng đã được làm ở đó. Pass chép của starter được viết từ mô tả đó; nó không được lấy từ máy Windows, và chưa được so sánh với nó hay đo trên Windows. Cho tới khi làm điều đó, hãy kiểm tra nó ở lần chạy Windows đầu tiên: so sánh một still của cùng khoảnh khắc trên macOS và trên Windows. Phép chép phải chuyển giá trị sang ánh sáng tuyến tính, nếu không mọi layer sẽ ra quá sáng, hình không được lộn ngược, và mép mềm trên một layer trong suốt không được có viền. Rồi đo thời gian frame của một shot có layer toàn frame trên cả hai.

**Nhạc và các thư mục dữ liệu.** App tham chiếu truy cập `audio/` và `data/` qua các symbolic link trong `public/`. Link bị mất khi chép qua một ổ đĩa định dạng exFAT hoặc FAT và qua một file nén không giữ link, cần Developer Mode hoặc một shell quyền cao để tạo trên Windows, và có thể bị git checkout thành các file văn bản nhỏ; một link bị mất làm server trả lời request lấy dữ liệu bằng chính trang đó. Starter không có link. Plugin `filmFolders` trong `vite.config.ts` phục vụ hai thư mục của thư mục phim ở `/audio/` và `/data/`, trả lời các byte range để phần tử audio có thể seek, và trả 404 cho file thiếu (204 cho file mà trang yêu cầu ở dạng tùy chọn, như lyrics). App chỉ dừng với `no audio analysis data found` khi `data/audio.json` thực sự không có.

## 12. Bắt đầu một phim mới trên engine này

Mỗi phim có thư mục riêng với bản sao engine riêng. Một phim đã giao được đóng băng cùng engine đã vẽ nó.

| Làm | Cái gì | Ghi chú |
|---|---|---|
| Sao chép | Toàn bộ `assets/starter/`, tới chỗ riêng của phim | Chạy `sh scripts/clean.sh` trong một thư mục phim trước khi nó được sao chép hay gửi đi: nó xóa các package đã cài, `out/`, cache build và `analysis/python-env`. Rồi `bun install` ở chỗ mới |
| Giữ nguyên | `src/engine/` cùng file giấy phép của nó, `vite.config.ts`, `package.json`, cả hai file `tsconfig`, `public/fonts/stroke/`, `src/scenes/parts/kit-camera.ts`, `src/click-track.ts`, `scripts/make-click-grid.ts`, `scripts/build-single.ts` | Engine nạp font nét (stroke font) khi khởi động, nên file đó phải có. `vite.config.ts` mang hot swap của scene, dấu nhận diện trang, việc phục vụ `audio/`, `data/` và `media/`, `server.forwardConsole`, và các thiết lập của build một file |
| Kiểm tra | `scripts/render.ts` | Không có gì trong đó nêu tên một phim, độ sâu thư mục hay một hệ thống: lock được tìm bằng cách đi ngược lên, backend đồ họa được chọn theo hệ thống, còn cổng và dấu nhận diện lấy từ cấu hình dự án. Chỉ cần kiểm tra rằng việc từ chối export video vẫn còn |
| Cấu hình | `src/project-config.ts` | `title`, `audioFile`, `studioAudio`, `fps`, `width`, `height` và `format` (format chính), `formats` (các format khác mà phim có thể được xem), `studioPort`. Không chỗ nào khác trong app khai báo kích thước hay rate. Tiêu đề nêu tên phim trong dấu nhận diện trang. Cho mỗi phim trên một máy một cổng riêng |
| Cấu hình | `src/engine/palette.ts` | Bản thân engine đọc `bg`, `fg`, `ink`, `paper`, `signal` và `blush`. Giữ các khóa đó và đổi màu của chúng. Kit đọc nhiều hơn |
| Cấu hình | Danh sách font ở đầu `src/engine/type.ts`, và `public/fonts/` | Các file font tĩnh kèm giấy phép của chúng. Transition đi xuyên qua một chữ cái dùng giọng display. Kiểm tra rằng mọi font có đủ các ký tự của ngôn ngữ phim |
| Cấu hình | `src/scenes/parts/kit-frame.ts` | Các vùng chữ của từng format, trong `ZONE_TABLES`, mỗi cái theo pixel của frame tham chiếu riêng và được co giãn theo kích thước của format. Tinh chỉnh chúng cho nền tảng mà phim được chiếu. Các đồng hồ giả định bốn beat một bar |
| Thu thập | `media/` | Ảnh, logo, ảnh chụp màn hình và frame clip mà phim hiển thị (mục 4). Ghi lại nguồn gốc của từng cái và theo giấy phép nào |
| Cấu hình | `src/scenes/parts/kit-post.ts`, `kit-ground.ts`, `kit-type.ts` | Hai preset post, các nền, các giọng chữ: phần treatment chuyển thành code |
| Tạo ra | `data/audio.json` | Trước hết là một lưới tổng hợp (`bun run make-grid -- --bpm 120 --bars 24`), rồi một lưới đo từ nhạc bằng các script trong `analysis/`, hoặc lưới chính xác của một score soạn bằng code (`bun run score`, `sound-and-voice.md`). Ranh giới shot được script build ghi từ danh sách shot, script này chạy cuối cùng vì bước phân tích và score ghi lại file |
| Viết | `shots.json`, `copy.json` | Danh sách shot và các từ ngữ. `bun run shots` kiểm tra cả hai, và chỉ khi mọi phép kiểm tra đạt mới ghi `STORYBOARD.md`, `data/film-sections.json` và thời điểm shot trong `data/audio.json`. Các kiểu trong `src/film.ts` chỉ thay đổi khi schema thay đổi |
| Điều chỉnh khi cần | `src/timeline.ts`, `src/scenes/storyboard-card.ts`, `src/scenes/overlay.ts`, `src/main.ts`, `index.html` | Cả năm đều đọc dữ liệu shot hoặc cấu hình dự án, và không cái nào nêu tên một phim. Các nhãn của studio bằng tiếng Anh; hãy dịch chúng cho owner đọc ngôn ngữ khác |
| Viết | `src/scenes/<shot id>.ts` | Các shot, do builder viết. Lead không viết chúng |

```
<film folder>/            a copy of assets/starter/
  package.json  bun.lock  vite.config.ts  tsconfig.json  tsconfig.scripts.json  index.html
  shots.json              the shot list, in bars
  copy.json               every word on screen
  STORYBOARD.md           generated from shots.json and copy.json
  audio/                  the music, and compressed copies for the studio; audio/score.wav and audio/voice/ when the sound is written in code
  media/                  photos, logos, screenshots, clips as numbered pictures (optional)
  data/audio.json         beat grid, shot boundaries, onsets
  data/score.json  data/voice.json   the score and the voice-over as data (optional)
  data/film-sections.json generated: shot boundaries in bars, for a new analysis of the music
  analysis/               the music analysis in Python; analysis/python-env/ is made on each machine
  scripts/render.ts  build-single.ts  make-click-grid.ts  build-shot-files.py  clean.sh  make-score.ts  voice-sapi.ps1
  public/fonts/
  src/project-config.ts  film.ts  timeline.ts  main.ts  click-track.ts
  src/engine/
  src/sound/              the score, the instruments, the mix, the voice (sound-and-voice.md)
  src/scenes/<shot id>.ts  storyboard-card.ts  overlay.ts
  src/scenes/parts/kit-*.ts
  out/                    captures and the single-file build; not kept, not copied
```

Chứng minh con đường hoạt động trước khi dựng bất kỳ shot thật nào: cùng một frame hai lần cho ra cùng một file, một hình nhấp nháy đúng beat ở đầu và ở cuối track, một câu có mọi dấu của ngôn ngữ render đúng ở mọi giọng chữ, kích thước và rate thay đổi ở một chỗ, studio phát cả phim dưới dạng thẻ, và, khi phim sẽ được bàn giao dưới dạng một file, `bun run single` build được và một still chụp từ file đó với `--page` bằng với cùng still chụp từ studio.

## 13. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Một frame đỏ sẫm | Shot không được nạp (`--only` chỉ định các shot khác), hoặc scene của nó ném lỗi | Đọc lỗi scene mà công cụ in ra. Chỉ định shot trong `--only` |
| Một shot đã dựng vẫn phát dưới dạng thẻ | Tên file không phải shot id, file nằm trong `parts/`, hoặc nó không có default class | Đặt tên file đúng chính xác như id trong dữ liệu shot |
| Một capture hiện cú cắt trơn ở chỗ lẽ ra có transition | Chỉ một bên của cú cắt được nạp | Chỉ định cả hai shot trong `--only` |
| Một bộ đếm in hai giá trị cùng lúc | Thời điểm nằm giữa hai frame, hoặc một giá trị đổi theo bậc được đọc từ thời điểm mẫu | Để still bắt về frame. Đọc giá trị đổi theo bậc từ đồng hồ frame |
| Chữ phát sáng | Kênh sáng nhất của nó vượt điểm bắt đầu bloom | Composite chữ với tint của kit. Giữ ngưỡng của preset tối |
| Một thứ phát sáng ở chỗ các nét cắt nhau, và không ở chỗ nào khác | Blending cộng dồn lại | Blend `max`, hoặc một batch riêng |
| Một tấm nền tối trông xám trên nền sáng | Tấm nền để lọt một phần nền, và blending diễn ra trong ánh sáng tuyến tính | Một tấm nền đục hoàn toàn |
| Một layer làm tối hình bên dưới nó | Alpha của target của nó vượt 1 | Giữ alpha trong khoảng 0 đến 1 khi cộng ánh sáng |
| Một phần hình bị thiếu ở frame dày đặc nhất | Line batch đã đầy; các đoạn vượt dung lượng bị bỏ lặng lẽ | Đặt dung lượng đủ cho frame dày đặc nhất và capture frame đó |
| Một model có mép răng cưa | Nó được render vào target truyền cho `render()` | Một target riêng với `samples: 4` |
| Frame đầu của một shot bị giật | Một shader, texture hoặc canvas được dựng khi dùng lần đầu | Dựng nó trong `init()` |
| Sự kiện trôi trễ dần về cuối phim | Thời gian được tính từ một con số tempo | Đọc thời điểm beat từ beat grid |
| Owner thấy một shot trống, capture vẫn ổn | Một tính năng canvas mà trình duyệt của owner không có | Đọc đầu ra của server phát triển. Tránh tính năng đó |
| Lưu một file helper làm nạp lại toàn bộ studio | Helper nằm trực tiếp trong `src/scenes/` | Chuyển nó sang `src/scenes/parts/` |
| App dừng với `no audio analysis data found` | `data/audio.json` chưa tồn tại | Tạo một lưới, hoặc đo một lưới, rồi chạy `scripts/build-shot-files.py` |
| App dừng với `data/audio.json has no sections` | Lưới được tạo hoặc đo lại sau khi thời điểm shot đã được ghi | Chạy `scripts/build-shot-files.py` |
| Một capture khởi động lâu | Một capture khác đang giữ lock | Chờ. Không bao giờ khởi động trình duyệt thứ hai để lách |
| Công cụ dừng và báo rằng phim này không trả lời ở `--url` | Địa chỉ đó phục vụ một phim khác, hoặc không gì cả. Công cụ chỉ chấp nhận trang có dấu nhận diện nêu tên phim này | Bỏ `--url`, để công cụ tự khởi động server, hoặc đưa địa chỉ studio của phim này |
| Một capture thất bại giữa chừng khi file đang được lưu | Capture được truyền `--url` và chạy trên studio của phim này, vốn bật live reload | Bỏ `--url`, hoặc đừng lưu file trong lúc capture |
| Layer trông quá sáng, lộn ngược hoặc có viền chỉ trên một máy | Pass chép của `Layer2D` hành xử khác trên backend đồ họa đó. Nó chưa được kiểm tra trên Windows | So sánh một still của cùng khoảnh khắc với still từ máy khác (mục 11). Thử một `--angle` khác |
| Frame chậm chỉ trên một máy | Render phần mềm, hoặc upload canvas chậm | Chạy `gpu`. Đo một shot gần như trống và một shot có layer toàn frame ở đó |
| `adaptive sampling needs stateless scenes` | Một scene stateful dưới `--samples auto` | Một số mẫu cố định, hoặc không dùng state |
| Công cụ thoát với mã 2 | Export video được yêu cầu mà không có sự đồng ý của owner | Giao trang studio. Hỏi owner |
| Một ảnh hoặc frame clip bị thiếu trong still, hoặc clip hiện sai frame | Hình được vẽ từ một bề mặt riêng mà engine không biết là đang nạp, hoặc được nạp bằng phần tử `Image` thay vì các helper của `src/engine/media.ts` | Nạp qua `loadBitmap`, `ImageTexture` hoặc `ImageSequence`, những cái có theo dõi việc nạp |
| Một ảnh lấp lánh khi được vẽ nhỏ hơn nhiều so với kích thước của nó | Không có mipmap | `ImageTexture` tạo chúng; trên layer canvas, đặt `maxSize` gần với kích thước được vẽ |
| Một hình trông bạc màu hoặc quá tối so với cùng file trong trình xem ảnh | Nó được upload thủ công thành texture sRGB, hoặc giá trị tuyến tính của nó bị chuyển đổi hai lần | Dùng `ImageTexture` hoặc một layer canvas; cả hai đi theo lối duy nhất của `copyToSRGB` |
| Chữ rơi ra ngoài frame hoặc nằm dưới các nút của nền tảng chỉ ở một format | Các vùng của format đó chưa được tinh chỉnh, hoặc scene đặt chữ ở vị trí pixel cố định | Tinh chỉnh `ZONE_TABLES` cho format đó; bố cục chữ từ các vùng |
| Studio hiện format chính khi một format khác được yêu cầu | Tên trong `?format=` không thuộc `FORMATS`; console cho biết những tên nào tồn tại | Dùng một tên có trong danh sách, hoặc thêm format vào `formats` |
| Trang một file trống khi mở | Script thất bại trước khi trang sẵn sàng: hãy đọc console của trình duyệt. Một file mà trang yêu cầu nhưng không được đóng gói sẽ trả 404 | Build lại sau khi thêm file; mở trang một lần qua công cụ capture với `--page` để xem lỗi của nó |
