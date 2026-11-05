# Starter: engine và studio cho một phim render bằng code

Thư mục này là điểm khởi đầu của một bộ phim trên route engine của skill `code-rendered-video`. Nó chứa một engine WebGL2 vẽ mọi frame như một hàm của thời gian bài hát (song time), một transition pass và một post chain, một kit dùng chung cho các scene, trang studio nơi phim được xem cùng nhạc của nó, và một công cụ capture để chụp still.

Sao chép toàn bộ thư mục sang chỗ riêng của bộ phim, ví dụ `films/<name>/`. Sau đó thêm nhạc, beat grid và danh sách shot. Mọi shot đều phát trong studio dưới dạng một storyboard card ngay từ ngày đầu tiên. Sau đó các builder thay các card bằng module scene, từng cái một.

Nó đi kèm một phim ví dụ nhỏ: một tiêu đề, hai section mỗi section ba shot, một recap và một end card, trên 24 bar với một grid tổng hợp ở 120 BPM. Không có file nhạc. Studio phát một tiếng click tạo từ beat grid, hoặc phát im lặng. Nó cũng đi kèm một score viết bằng code cho phim đó (`data/score.json`) và một voice-over ngắn (`data/voice.json`); `bun run score` render chúng (xem "Âm thanh viết bằng code" bên dưới).

Phương pháp nằm trong các reference của skill: `engine-architecture.md`, `studio-viewer.md`, `storyboard.md`, `music-and-beat.md`, `sound-and-voice.md`, `transitions.md`.

## Các lệnh

Chạy mọi lệnh từ thư mục này. Bạn cần bun, Node.js 20 trở lên, Python 3 (`python3` trên macOS và Linux; `python` hoặc `py -3` trên Windows), và Google Chrome để capture. Phần phân tích nhạc còn cần Python (3.12 hoặc 3.13 là lựa chọn an toàn) với các package trong `analysis/requirements.txt` (xem "Phân tích nhạc" bên dưới).

```sh
bun install                                   # packages
bun run make-grid -- --bpm 120 --bars 24      # a synthetic beat grid in data/audio.json
bun run shots                                 # check the storyboard; write STORYBOARD.md and the shot times
bun run studio                                # the studio at http://localhost:5180 (Ctrl+C stops it)
bun run typecheck
```

`bun run shots` chạy `scripts/build-shot-files.py` với Python 3 đầu tiên mà nó tìm thấy: `python3`, rồi `python`, rồi `py -3` (`scripts/python.ts`; đặt `PYTHON` để chọn một cái). Script cũng có thể chạy trực tiếp: `python3 scripts/build-shot-files.py` trên macOS và Linux, `python scripts/build-shot-files.py` hoặc `py -3 scripts/build-shot-files.py` trên Windows, nơi `python3` thường chỉ là một stub mở Microsoft Store.

Để bàn giao bộ phim dưới dạng một file duy nhất phát được bằng cách nhấp đúp, không cần server:

```sh
bun run single                                # out/single/<title>.html: the page, its script, fonts, data, media/ and the first music file of studioAudio
bun run single -- --audio all                 # every music file of studioAudio; --audio none for none; --audio <file> for one
bun run single -- --format 1:1                # a page that opens in that format
```

Các lần capture chạy từng cái một cho cả repository. Công cụ capture tự khởi động và tự dừng server riêng của nó, nên studio không cần phải đang chạy.

```sh
bun scripts/render.ts stills --t 5,18.2                          # full-size stills in out/stills/
bun scripts/render.ts stills --beats 36,36.5 --only steep-leaves-drop
bun scripts/render.ts sheet --times 5,13.9,18.2,30 --cols 4 --out out/check.png
bun scripts/render.ts sheet --cuts --cols 4                      # frames round every cut
bun scripts/render.ts sheet --frames 300,301,302 --cols 3        # output frame numbers (t = n / fps)
bun scripts/render.ts perf --from 20 --to 25                     # frame time
bun scripts/render.ts gpu                                        # which graphics backend Chrome uses
bun scripts/render.ts stills --format 16:9 --t 5                 # another format of the film: out/stills-16x9/
bun scripts/render.ts stills --page out/single/starter-film.html --t 5   # a still of the single file, from disk
```

- Thêm `--angle` để chọn backend đồ hoạ của Chrome: `metal`, `d3d11`, `gl`, `vulkan`, `swiftshader` hoặc `default`. Không có nó, công cụ dùng `metal` trên macOS, `d3d11` trên Windows và `gl` trên Linux. Một câu trả lời `gpu` có chứa SwiftShader nghĩa là render bằng phần mềm, và thời gian frame đo ở đó không có ý nghĩa gì.
- `--format <name>` dùng được ở mọi chế độ: một trong các định dạng trong `src/project-config.ts` (9:16, 1:1, 4:5, 16:9 trong starter). Không có nó thì là bản master.
- Still và sheet nhận thời điểm dưới dạng giây (`--t`, `--times` của sheet, `--from`/`--to`), số frame output (`--frames`) hoặc chỉ số beat (`--beats`). Một thời điểm tính bằng giây hoặc beat được dời về frame output gần nhất, vốn là những thời điểm duy nhất mà một bản export render; `--exact` render đúng như đã cho.
- Still và sheet chờ các ảnh và frame clip vẫn đang tải (`src/engine/media.ts`), nên một still không bao giờ cho thấy một frame chưa tải xong.
- Chế độ `video` có tồn tại nhưng bị từ chối (exit code 2) trừ khi đặt `OWNER_ASKED_FOR_VIDEO=yes`. Chỉ đặt nó khi owner đã yêu cầu một file video trong cuộc hội thoại hiện tại. Thiết lập encoder của nó, cách đạt một kích thước như "dưới 30 MB" hay 720p, và các bước kiểm tra file nằm trong `references/engine-architecture.md` của skill, mục 8.
- Công cụ luôn khởi động server riêng của nó, không có live reload, nên một file được lưu trong lúc capture không thể thay đổi hình. `--url http://localhost:5180` khiến nó dùng studio đang chạy thay vào đó, và chỉ khi marker của trang nêu tên đúng bộ phim này (`title` trong `src/project-config.ts`); đừng lưu file trong khi một lần capture như vậy đang chạy.
- File khoá là `.render.lock` trong thư mục gần nhất phía trên thư mục này có chứa `.git`. Nếu không có, nó là thư mục gần nhất chứa `CLAUDE.md` hoặc `AGENTS.md`, và sau đó là thư mục tạm của hệ thống. Đặt `RENDER_LOCK_DIR` để tự chọn thư mục.
- `sh scripts/clean.sh` xoá các package đã cài, `out/`, cache của build và `analysis/python-env` trước khi thư mục được sao chép hoặc phát hành.

## Thiết lập một phim mới

1. Đặt `src/project-config.ts`: tiêu đề, các file nhạc, frame rate, định dạng master (`width`, `height`, `format`), các định dạng khác mà phim có thể được xem (`formats`), và cổng (port) của studio. Cho mỗi phim trên cùng một máy một port riêng.
2. Đặt bản nhạc vào `audio/`: bản master là `audio/track.wav`, cộng với các bản nén có cùng timing cho studio (`studioAudio`, ví dụ `audio/track.m4a`). Một file có trong danh sách nhưng bị thiếu sẽ được bỏ qua. Công tắc nhạc luôn kết thúc bằng `click` và `silent`.
3. Thay grid tổng hợp bằng một grid đã đo. Bản nhạc thật bị trôi tempo, và một phim cắt trên một grid đều sẽ trượt khỏi nhạc. Các script trong `analysis/` ghi `data/audio.json` từ bản nhạc (bên dưới, và phương pháp trong `references/music-and-beat.md` của skill). Truyền `--sections data/film-sections.json` để giữ ranh giới các shot. Sau đó chạy lại `bun run shots`. Nó phải chạy sau cùng, vì phần phân tích ghi đè file. Một score soạn bằng code (`bun run score`, bên dưới) tự ghi grid của nó thay vào đó, chính xác, không cần đo gì.
4. Viết `shots.json` và `copy.json` (schema ở bên dưới và trong `storyboard.md`). Chạy bộ sinh sau mỗi thay đổi.
5. Đặt look: màu trong `src/engine/palette.ts` (giữ nguyên các key), font trong `src/engine/type.ts` và `public/fonts/`, các vùng của từng định dạng trong `src/scenes/parts/kit-frame.ts` (`ZONE_TABLES`), các nền (ground) và bầu trời (`Sky`), giọng chữ (type voice) và preset post trong `kit-ground.ts`, `kit-type.ts` và `kit-post.ts`; một phim có nhân vật hoặc pixel art còn dùng `kit-rig.ts` và `kit-pixel.ts`; hạt nằm trong `kit-particles.ts`, và thiết bị cùng card trong không gian nằm trong `kit-devices.ts`.
6. Đặt ảnh, logo, ảnh chụp màn hình và frame clip mà phim cho thấy vào `media/` (bên dưới, "Ảnh và clip").
7. Mở studio và cho owner xem animatic. Không ai dựng shot nào trước khi owner duyệt nó.

### Phân tích nhạc

Bốn script trong `analysis/` cần librosa và các thư viện đi kèm. Tạo môi trường một lần cho mỗi máy, bên trong thư mục này; một môi trường tạo trên máy này không chạy được trên máy khác.

```sh
python3 -m venv analysis/python-env                                        # Windows: py -3.13 -m venv analysis\python-env
analysis/python-env/bin/python -m pip install -r analysis/requirements.txt  # Windows: analysis\python-env\Scripts\python.exe
```

`requirements.txt` chứa các phiên bản mà các phim tham chiếu đã được đo với chúng, trên macOS. Nếu một phiên bản đã pin không có wheel cho hệ thống hoặc Python khác, hãy cài bộ không pin thay vào đó: `librosa soundfile numpy scipy matplotlib`.

```sh
P=analysis/python-env/bin/python
$P analysis/analyze-beat-grid.py audio/track.wav data/audio.json --sections data/film-sections.json
$P analysis/plot-beat-grid-qa.py audio/track.wav data/audio.json out/grid-qa     # images to look at
bun run shots                                                                    # always last
```

| Script | Làm gì |
|---|---|
| `analysis/analyze-beat-grid.py` | Beat bằng cách bám theo tiếng kick, bar, các đặc trưng năng lượng; ghi file mà app đọc |
| `analysis/track-beats-by-phase-lock.py` | Một grid cho bản nhạc mà tiếng kick không thể bám theo suốt cả bài; output của nó được đưa trở lại bằng `--beats-from` |
| `analysis/plot-beat-grid-qa.py` | Năng lượng theo từng bar và dạng sóng phóng to với grid đè lên trên, để kiểm bằng mắt |
| `analysis/edit-track-by-bars.py` | Cắt bản nhạc theo một danh sách khoảng bar và mang grid theo |

### Âm thanh viết bằng code

Thay vì một bản nhạc, phần nhạc có thể là một score viết dưới dạng dữ liệu, với hiệu ứng âm thanh trên các sự kiện của hình và một voice-over kèm caption. Phương pháp nằm trong `references/sound-and-voice.md` của skill.

```sh
bun run voice:sapi            # Windows only: speak data/voice.json with a local voice; audio/voice/*.wav, data/voice-words.json
bun run score -- --check      # check data/score.json (and the voice) without writing
bun run score                 # audio/score.wav, the exact grid in data/audio.json, captions in data/lyrics.json
bun run shots
```

| File | Chứa |
|---|---|
| `data/score.json` | Tempo, bus, nhạc cụ, pattern, các section theo bar, cue của hiệu ứng âm thanh, và file giọng đọc. Do lead chỉnh sửa |
| `data/voice.json` | Các cụm câu của voice-over, mỗi cụm kèm bar và beat mà từ đầu tiên của nó rơi vào; `\|` và `/` trong văn bản dùng để ngắt caption. Do lead chỉnh sửa |
| `data/voice-words.json` | Được ghi bởi bước giọng đọc: thời điểm của từng từ bên trong mỗi file cụm câu |
| `data/lyrics.json` | Được ghi bởi `bun run score`: các nhóm caption theo song time, được app đọc dưới dạng `ctx.lyrics` |

Các nhạc cụ không chỉ có bộ trống và synth: dây (strings), kèn đồng (brass), piano, electric piano, sáo, chuông, một loại đàn tranh giống guzheng, wobble bass, một giọng 8-bit, các lớp nền gió, mưa, phòng, sông và dế, và các preset hiệu ứng cho game và giao diện (coin, fanfare, level-up, siren, engine, crunch, pop, boing, toggle, success, error, notify, key). Một nhạc cụ `sample` phát một file WAV do owner chỉ định, đặt theo đỉnh (peak) đã đo của nó. Một score có `track` đặt hiệu ứng, một lớp nền hoặc một giọng đọc lên trên một bản nhạc hoàn chỉnh mà grid đã được đo vào `data/audio.json`, duck bản nhạc và đặt cả bản mix về một mục tiêu loudness; nó giữ nguyên grid. `cueModules` biến các sự kiện của một mô phỏng thành cue. Overlay vẽ các nhóm caption của giọng đọc ở chân khung hình.

Công tắc nhạc của studio có thêm `score` khi `audio/score.wav` tồn tại. Khi score là nhạc của phim, đặt `audioFile` trong `src/project-config.ts` trỏ tới nó. `--no-grid` chỉ ghi file WAV và giữ nguyên grid và caption. Hai lần chạy trên cùng các file cho ra cùng các byte. Một giọng đọc không chạy cục bộ (edge-tts, giọng trả phí) sẽ gửi kịch bản ra ngoài hoặc tốn tiền: hãy hỏi owner trước.

### Hai file dữ liệu

| File | Chứa |
|---|---|
| `shots.json` | `transitions` (loại transition ứng với nhãn và mô tả, và mọi loại phải tồn tại trong `src/engine/transition.ts`), `groups` (các section của phim: `title`, `section`, `recap`, `end`), `shots` (id, group, bar, bars, tone, title, `in`, see, move, camera, look, và tuỳ chọn `repeat`), `captions` (group, kind, bar, bars, how, place, why) |
| `copy.json` | `labels` và `accents` cho mỗi loại caption, câu chữ của các card `title` và `closing`, và `sections`: một mục cho mỗi group section, nối theo `group`, với `n` và `name` bằng với của group và một object `lines` chứa một câu cho mỗi loại caption, mỗi chuỗi là một dòng trên màn hình |

Bộ sinh kiểm cả hai file trước khi ghi bất cứ thứ gì. Nếu một bước kiểm thất bại, nó in một dòng cho mỗi lỗi và không ghi gì cả. Một số phát hiện là cảnh báo, được in ra mà không dừng lần chạy: hai shot liên tiếp vào bằng cùng một transition (khác `cut`, `travel` và `match`), hoặc có `camera` là cùng một đoạn văn bản, và một danh sách shot dài hơn audio. Sự lặp lại thường là một sơ suất, nhưng nó có thể là hình thức của một bộ phim (một con búp bê lồng nhau mở ra theo cùng một cách ở mỗi tầng): `"repeat": true` trên một shot tuyên bố rằng việc nó lặp lại shot trước đó là có chủ đích, và tắt hai cảnh báo đó cho cặp ấy. Nó ghi ra ba file:

- `STORYBOARD.md`
- `data/film-sections.json`, ranh giới các shot theo bar
- `sections` của `data/audio.json`, thời điểm các shot tính bằng giây mà app đọc

Không bao giờ chỉnh sửa một file được sinh ra. Bộ đếm hiển thị `NN/TT`, và tổng số lấy từ số lượng group section.

### Ảnh và clip

`media/` chứa các hình ảnh mà một bộ phim cho thấy. Studio phục vụ nó tại `/media/`, và `bun run single` đóng gói nó. `src/engine/media.ts` tải chúng; mọi lần tải đều được theo dõi, nên still và bản export sẽ chờ chúng.

| Helper | Dùng cho |
|---|---|
| `ImageTexture` | Một ảnh, logo hoặc ảnh chụp màn hình dưới dạng texture: `await this.logo.load('media/logo.png')` trong `init()` |
| `drawPicture(renderer, texture, [w, h], out, rect, { fit, zoom, focus, radius, opacity })` | Vẽ texture đó vào một hình chữ nhật: `cover`, `contain` hoặc `stretch`, một cú đẩy chậm (slow push), góc bo tròn |
| `loadBitmap(path)`, `drawImageFit(ctx, picture, rect, { fit })` | Tương tự trên một lớp canvas, nơi nó có thể được cắt (clip) và trộn với chữ |
| `ImageSequence({ pattern: 'media/run/%04d.jpg', count, fps })` | Một clip dưới dạng các ảnh đánh số: `frameAt(seconds)` cho canvas, `textureAt(seconds)` cho GPU |

Một clip được trích từ video một lần, bằng ffmpeg, chỉ khi có lời đồng ý của owner (đó là một lần chạy nặng). Lệnh nằm trong `references/engine-architecture.md` của skill, mục 4.

## Thêm một module scene

Một shot được dựng thành `src/scenes/<shot id>.ts`, và tên file phải đúng chính xác id trong `shots.json`. Default export của nó là một class kế thừa `Scene`. Khi file tồn tại, studio phát nó thay cho card. Tải lại trang sau lần lưu đầu tiên, vì việc phát bản đã dựng hay card được quyết định khi trang tải. Sau đó, các lần lưu được thay nóng vào mà không cần tải lại.

```ts
import type * as THREE from 'three';
import { Scene, type Frame, type PostOverrides } from '../engine/scene';
import { Layer2D } from '../engine/gl';
import { Ground } from './parts/kit-ground';
import { sceneClock, frameClock } from './parts/kit-frame';
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
    // ... draw in logical px, from k and kf only
    comp.draw(renderer, this.layer.upload(), out, { tint: TYPE_TINT });
    return POST_DARK;
  }

  override dispose() { this.ground.dispose(); this.layer.dispose(); }
}
```

Một phim dùng màu phẳng chính xác: ví dụ ở trên cố ý làm sáng lên và làm tối đi màu sắc. `Ground` phủ một texture giấy lên các nền sáng, `TYPE_TINT` làm tối lớp xuống 86%, và `POST_DARK` thêm bloom, halation, viền màu (colour fringe), grain và vignette trên vùng vai tone (tone shoulder). Để có màu ra đúng chính xác như `src/engine/palette.ts` cho, hãy tự lấp đầy toàn bộ lớp (màu nền trước tiên), composite nó bằng `comp.draw(renderer, this.layer.upload(), out, { mode: 'replace' })` và không tint, và trả về từ `render()`:

```ts
return { tone: 0, dither: 0, grain: 0, bloom: 0, halation: 0, ca: 0, vignette: 0 };
```

Mỗi thứ này đều bật trong các mặc định của `src/engine/post.ts` (`DEFAULT_POST`), mà các override của scene được đặt chồng lên, nên mỗi cái phải được đặt về 0. `exposure` giữ ở 1; các look tắt theo mặc định (`hue`, `kaleido`, `fisheye`, `bulge`, `mosaic`, `glitch`, `crt`, `invert`, `fade`, `flash`) vẫn tắt. Một transition vẫn có thể đặt một số trong chúng cho các frame của riêng nó, và overlay vẫn vẽ bộ đếm và caption plate lên trên shot. Đã kiểm trên Windows: signal, paper và ink ra đúng `#FF2E74`, `#F3EBDD` và `#100E14`.

Một scene đọc một file dữ liệu của phim (`data/*.json`) theo một trong hai cách. Import nó, và nó trở thành một phần code của scene, trong studio và trong bản build single-file: `import score from '../../data/score.json';`. Hoặc fetch nó trong `init()`, khi nó lớn hoặc không bắt buộc: `const r = await fetch('data/strikes.json'); this.strikes = await r.json();`. Studio phục vụ `data/` tại `/data/`, và `bun run single` đóng gói mọi `data/*.json` và trả lời lệnh fetch từ bản đã đóng gói. Một file được import sẽ được thay nóng khi nó được lưu, giống như scene; một file được fetch chỉ được đọc lại khi trang tải.

Quy tắc cho scene:

- Không `Date`, không `performance.now`, không `Math.random`. Dùng các helper có seed trong `src/engine/util.ts`.
- Beat đến từ grid, không bao giờ từ một con số tempo.
- Các helper dùng chung đặt trong `src/scenes/parts/`. Một helper đặt trực tiếp trong `src/scenes/` sẽ tải lại toàn bộ studio khi nó được lưu.
- Đừng dùng `ctx.filter` của canvas, vì Safari không có nó. Đừng dựa vào `letterSpacing` để làm cho bố cục vừa khít.

## Phím trong studio

| Phím | Hành động |
|---|---|
| Space, hoặc một cú nhấp lên hình | Phát hoặc tạm dừng |
| `[` và `]` | Shot trước, shot kế tiếp |
| Phím mũi tên | Lùi hoặc tiến một giây. Giữ Shift thì thành năm giây |
| `,` và `.` | Lùi hoặc tiến một frame |
| `L` | Lặp shot |
| `M` | Nguồn nhạc kế tiếp |
| `F`, hoặc nút Format | Trang ở định dạng kế tiếp, tại cùng thời điểm |

Các tham số của trang là `?t=<seconds>`, `?only=<ids>`, `?scale=<1..4>` và `?format=<name>`. Trang công bố `window.seek(t)`: nó vẽ frame ở song time `t` (tạm dừng ở đó) và resolve khi mọi hình ảnh của frame đó đã tải xong; `window.duration` là độ dài của bộ phim.

Lỗi từ trình duyệt được chuyển tiếp tới terminal của studio (`server.forwardConsole`). Một scene bị lỗi sẽ hiện một frame đỏ sẫm, và phần còn lại của phim vẫn tiếp tục phát.

## Những gì khác so với app tham chiếu

| Thay đổi | Lý do |
|---|---|
| `Layer2D` upload canvas của nó dưới dạng RGBA8 thuần, và một pass nhỏ sao chép nó vào một texture sRGB trong ánh sáng tuyến tính. API giữ nguyên | Việc upload canvas sRGB đi vào một đường chậm trong Chrome trên Windows (Direct3D 11) |
| `filter` của canvas chỉ được vá và đặt lại ở những nơi trình duyệt có nó | Safari không có canvas filter |
| `audio/` và `data/` được phục vụ bởi middleware trong `vite.config.ts`, có hỗ trợ byte range, và một file bị thiếu trả về 404. Các request mà Vite đánh dấu là module (`?import`, `?raw`, `?url`) được chuyển qua cho Vite, nên một scene có thể import một file dữ liệu. Không có symbolic link | Link bị mất trên exFAT, trong file zip và trên Windows. Trước đây, một link bị thiếu sẽ trả về chính trang đó như là dữ liệu |
| Tiêu đề trang và marker `render-app` lấy từ project config, và marker nêu tên bộ phim | Công cụ capture không bao giờ gắn vào studio của một phim khác |
| Port của studio nằm trong project config; công cụ capture chỉ dùng studio khi `--url` nêu tên nó | Mỗi phim một địa chỉ, và các lần capture không bị một file vừa lưu làm xáo trộn |
| Backend của Chrome được chọn theo nền tảng (`--angle` ghi đè nó). File khoá được tìm bằng cách đi ngược lên tới gốc repository | Công cụ chạy trên macOS, Windows và Linux, và ở bất cứ đâu thư mục phim nằm |
| `groups[].kind` `section` thay cho `pattern`, `copy.sections[].lines` thay cho `patterns[]` với các key câu cố định, và `labels` cùng `accents` thay cho `problemLabel` và `whenLabel` | Thuật ngữ trung lập và các loại caption mang tên bất kỳ |
| Bộ sinh nối copy với group theo `group`, kiểm mọi trường với một thông báo dễ hiểu, và chỉ ghi sau khi mọi bước kiểm đã đạt | Đây là những lỗi tìm thấy khi review bộ sinh tham chiếu |
| Phím chọn nhạc không phân biệt hoa thường, và thanh tua (scrub bar) trả lại focus sau khi tua | Đây là những lỗi thường gặp của app tham chiếu: khi bật Caps Lock các phím không làm gì cả, và sau khi tua các phím mũi tên lại di chuyển thanh tua |

## Bản đồ file

```
README.md                  this file
package.json  bun.lock     packages; scripts studio, typecheck, render, single, make-grid, shots, score, voice:sapi
vite.config.ts             studio server: scene hot swap, page title and marker, audio/, data/ and media/ middleware; the single-file build's settings
tsconfig.json              the app;  tsconfig.scripts.json: scripts/ and vite.config.ts
index.html                 the studio page (no film named in it)
shots.json  copy.json      the storyboard as data (edited by the lead)
STORYBOARD.md              generated
audio/                     the music (none in the starter)
media/                     photos, logos, screenshots, clips as numbered pictures (none in the starter)
data/audio.json            beat grid and shot times (synthetic in the starter)
data/film-sections.json    generated: shot boundaries in bars
data/score.json            the score written in code: instruments, patterns, sections, cues (edited by the lead)
data/voice.json            the voice-over as phrases placed on the grid (edited by the lead)
public/fonts/              fonts and their licences (OFL; Hershey stroke font)
scripts/render.ts          capture tool: stills, sheet, perf, gpu (video refused without the owner's word); --format, --page
scripts/build-single.ts    the film as one HTML file that plays from disk (bun run single)
scripts/make-click-grid.ts synthetic beat grid
scripts/make-score.ts      renders data/score.json to a WAV and writes its exact grid and the voice's captions
scripts/voice-sapi.ps1     Windows: speaks data/voice.json with a local voice and writes the word times
scripts/build-shot-files.py  checks the storyboard and writes the generated files
scripts/python.ts          runs a Python script with the first Python 3 found (bun run shots)
scripts/clean.sh           removes installed packages, out/, build caches and analysis/python-env
analysis/                  music analysis in Python: beat grid, phase-lock grid, grid images, cutting by bars
analysis/requirements.txt  the analysis packages, as pinned on macOS
src/project-config.ts      title, music, fps, the master format and the other formats, studio port, page marker
src/film.ts                types of the shot list and the copy, lookups
src/timeline.ts            shots to timeline entries; card for a shot without a module; overlay entry
src/main.ts                studio player, format switch, window.seek, export hook (window.__render)
src/click-track.ts         the click of the beat grid, for a film without a music file
src/engine/                engine, transition pass, post chain, layers, pictures and clips (media.ts), type, audio data, word timings, util
src/sound/                 the score: instruments (instruments, orchestra, ambience, effects), mix (reverb, delay, ducking, limiter, loudness, WAV), grids, voice and captions, an example of cues from a simulation
src/engine/LICENSE-pdoom-video.txt   MIT licence of the engine this one is derived from
src/scenes/storyboard-card.ts        plays every shot that has no module
src/scenes/overlay.ts                counter and captions over every shot
src/scenes/parts/kit-*.ts            shared kit: frame and clocks, camera, ground, type and type in motion, post presets and passes on layers, particles, devices, rig, pixel
src/scenes/<shot id>.ts              scene modules, written by builders
out/                       captures and the single-file build (not kept)
```

## Giấy phép

Một số file được phát triển từ [pdoom-video](https://github.com/mexicat/pdoom-video) của Giacomo Magnanini, theo MIT License. Mỗi file như vậy đều ghi rõ điều đó trong phần header, và văn bản giấy phép nằm trong `src/engine/LICENSE-pdoom-video.txt`. Giữ cả hai khi bạn sao chép thư mục. Các font theo SIL Open Font License, và văn bản giấy phép của chúng nằm cạnh chúng trong `public/fonts/`.
