# code-rendered-video: thư mục skill

Thư mục này là một agent skill. `SKILL.md` là điểm vào; phần còn lại được nạp khi cần. Nó được viết ra từ hai bộ phim ("các phim tham chiếu") và chứa mọi thứ một bộ phim mới cần: không có gì trong đó trỏ ra ngoài thư mục.

## Ở đây có gì

| Đường dẫn | Số dòng | Chứa |
|---|---|---|
| `LICENSE` | 27 | MIT |
| `SKILL.md` | 149 | Điểm vào: thuật ngữ, mười quy tắc, mười một giai đoạn cùng các cổng kiểm (gate) của chúng, làn ngắn (short lane) và chế độ tự hành (autonomous mode), nạp reference nào khi nào |
| `references/environment.md` | 247 | Công cụ theo từng route, lệnh cài đặt cho macOS, Windows, Linux, khác biệt giữa các hệ thống, trình duyệt của chủ phim (owner) |
| `references/interview.md` | 217 | Cách hỏi; các vòng câu hỏi bằng tiếng Anh và tiếng Việt, kể cả cho tác phẩm ngắn và chất liệu thật; trang brief |
| `references/route-selection.md` | 135 | Engine, HyperFrames hay kết hợp; các công cụ được nêu tên; những yêu cầu không phải là phim theo phương pháp này |
| `references/hyperframes-route.md` | 186 | Họ skill HyperFrames và cách dùng nó theo quy tắc của owner |
| `references/hyperframes-facts.md` | 772 | Bảng dữ kiện đứng sau hai chương HyperFrames, đọc ở CLI 0.8.81 |
| `references/thinking-and-brainstorm.md` | 269 | Nghiên cứu về thứ có thật và nguồn của nó; từ một chủ đề đến hình ảnh; các phép so sánh; các hướng đi |
| `references/music-and-beat.md` | 365 | Nhạc, beat grid (lưới nhịp), music map (bản đồ nhạc), đồng hồ |
| `references/storyboard.md` | 476 | Storyboard dưới dạng dữ liệu |
| `references/transitions.md` | 333 | Danh mục transition (chuyển cảnh) và quy tắc sử dụng chúng |
| `references/camera.md` | 268 | Danh mục vị trí và chuyển động camera |
| `references/art-styles.md` | 412 | Danh mục look (phong cách hình), công thức theo từng loại phim, màu sắc |
| `references/effects.md` | 509 | Danh mục hiệu ứng bên trong một shot và trên frame hoàn chỉnh |
| `references/type-and-captions.md` | 267 | Chữ trên màn hình |
| `references/engine-architecture.md` | 574 | Engine của route engine |
| `references/studio-viewer.md` | 381 | Trang studio |
| `references/orchestration.md` | 406 | Lead, người viết truyện (story writer), builder, vòng review, model |
| `references/quality-gates.md` | 391 | Các cổng kiểm, checklist, lỗi thường gặp, thế nào là "xong" |
| `references/short-pieces.md` | 411 | Làn ngắn cho tác phẩm từ 5 đến 40 giây, chế độ tự hành, các công thức (showreel, tác phẩm UI, launch, reward reveal, kinetic words, sting, lyric video, game trailer, fast edit, meme piece), loop, nhiều định dạng, tác phẩm phát khi bấm |
| `references/sound-and-voice.md` | 459 | Nhạc nền (score) và hiệu ứng âm thanh viết bằng code, voice-over và thời điểm từng từ, nhóm caption, ducking và độ lớn (loudness) |
| `references/characters-and-story.md` | 307 | Thiết kế, rig và diễn xuất nhân vật bằng code, các chu kỳ (cycle), nhiều nhân vật, file cast, nhân vật trong 3D, câu chuyện kể không lời, lỗi trong still |
| `scripts/check-environment.mjs` | 359 | Kiểm tra một máy cho một route; in ra lệnh cài đặt |
| `scripts/check-environment.sh`, `.ps1` | 65 | Khởi chạy trình kiểm tra khi chưa biết có runtime nào |
| `assets/starter/` |  | Một engine chung, studio, công cụ capture, bộ sinh storyboard và phân tích nhạc, kèm một phim ví dụ nhỏ. `README.md` của nó là sổ tay hướng dẫn cho một thư mục phim |

## Cài đặt như một skill

Một skill là một thư mục có tên trùng với `name` trong `SKILL.md` của nó. Hãy sao chép thư mục này, dưới đúng tên đó, vào thư mục skills của trợ lý.

```sh
# Claude Code, for one user (macOS, Linux)
cp -R code-rendered-video ~/.claude/skills/code-rendered-video
# for one project
mkdir -p .claude/skills && cp -R code-rendered-video .claude/skills/code-rendered-video
```

```powershell
# Claude Code, for one user (Windows)
Copy-Item -Recurse code-rendered-video "$env:USERPROFILE\.claude\skills\code-rendered-video"
```

Sao chép bản sạch: không có `node_modules/`, `out/` hay `analysis/python-env/` bên trong `assets/starter/`. `sh assets/starter/scripts/clean.sh` sẽ xoá chúng. Một bộ phim được làm trong một bản sao của `assets/starter/`, không bao giờ bên trong thư mục skill.

## Lần chạy đầu trên máy mới

1. `node scripts/check-environment.mjs` (hoặc trình khởi chạy `.sh`, `.ps1` khi có thể chưa có Node.js). Thêm `--with audio` để kiểm cho phần phân tích nhạc.
2. Sao chép `assets/starter/` sang một thư mục nháp và làm theo README của nó: `bun install`, `bun run make-grid -- --bpm 120 --bars 24`, `bun run shots`, `bun run typecheck`, `bun run studio`.
3. Tạo môi trường Python trong thư mục đó như README của nó hướng dẫn, và chạy `analysis/analyze-beat-grid.py` trên một bản nhạc bất kỳ.
4. Một still (ảnh tĩnh): `bun scripts/render.ts stills --t 5`, và `bun scripts/render.ts gpu` để xem Chrome dùng backend đồ hoạ nào.

## Những gì đã thử và chưa thử

| Phần | Trạng thái |
|---|---|
| Phương pháp | Đã dùng trên hai phim, một phim ngang dài 135 giây, một phim dọc dài 172 giây với 54 shot |
| Trình kiểm tra môi trường | Đã chạy trên macOS 26 trên Apple silicon với Node.js 24 và Bun 1.3. Trên Windows 11 với Node.js 24, ngày 2026-09-28, mọi dòng đều khớp với máy sau hai bản sửa: winget, một app alias mà `stat` không lần theo được, đã không được tìm thấy; lệnh Python trỏ tới Python mới nhất (3.14) thay vì bản mới nhất trong khoảng 3.10 đến 3.13. Chưa chạy trên Linux |
| Starter | Trên macOS: cài đặt, type check, bộ sinh, một sheet các capture và trang studio đều đạt. Ngày 2026-09-28 phần phân tích nhạc đã chạy từ starter trên một bản nhạc thật dài 172 giây, và bộ sinh đã được sửa để đếm bar 0 từ downbeat (phách mạnh) đầu tiên |
| Bản sửa upload sRGB trong starter | Được viết từ mô tả của bản sửa đã làm trên máy Windows của owner, không phải từ code của nó. Trên Windows 11 các still của nó khớp với bản tham chiếu macOS, và code của nó làm đúng những gì engine design patterns làm (các dòng bên dưới) |
| Các pin Python | `analysis/requirements.txt` được resolve trên macOS. Trên Windows 11 với Python 3.13, ngày 2026-09-28, mọi pin đều cài được. Chưa thử trên Linux |
| Phân tích nhạc trên Windows | Trên Windows 11, ngày 2026-09-28, trên bản nhạc 172 giây của phim tham chiếu thứ hai: phân tích kick đếm dư một beat ở đoạn drop nơi tiếng bass che mất tiếng kick, đúng như `music-and-beat.md`, mục 5, mô tả; script phase-lock sau đó cho ra 375 beat trùng với grid đo trên macOS, tới từng mili giây |
| Thời gian frame trên Windows | Windows 11, Chrome trên Direct3D 11, RTX 4090, ngày 2026-09-28: `perf --from 16 --to 21` trên các storyboard card cho trung vị 14.7 ms và phân vị 95 là 19.6 ms, đã tính cả readback; frame đầu tiên mất 1.06 s. Không có số liệu cùng khoảng trên macOS để so sánh |
| Các chương HyperFrames | Được viết từ các file skill của nó và các lần chạy chỉ-đọc của CLI 0.8.81. Chưa có phim nào được làm trên route đó |
| Các chương thêm vào ngày 2026-09-28 cho tác phẩm ngắn, âm thanh và giọng đọc, nhân vật và câu chuyện, nghiên cứu một sản phẩm thật, và ranh giới của phương pháp | Được viết từ phương pháp và từ một bộ sưu tập khoảng bốn trăm prompt cho những tác phẩm như vậy. Chưa thử trên phim nào. Dữ liệu shot của một tác phẩm ngắn (một nhóm `title`, các shot dài một bar vào bằng `cut`, không caption) đã được chạy qua bộ sinh trong một bản sao của starter trên Windows |
| Âm thanh viết bằng code | `bun run score` (score và hiệu ứng âm thanh) và giọng đọc cục bộ trên Windows (`bun run voice:sapi`) đã chạy trên Windows 11 ngày 2026-09-28. Ba lần chạy cho cùng một output; grid bằng với grid tổng hợp đi kèm. Chưa được nghe thử |
| Rig nhân vật (`src/scenes/parts/kit-rig.ts`) | Lead đã xem ba still của một scene demo trên Windows 11 ngày 2026-09-28: chân đặt trên đường mặt đất, một tư thế đi, một cú nhảy. Trong cú nhảy, chân bị một caption plate che, nên chưa được đánh giá |
| Pixel kit (`src/scenes/parts/kit-pixel.ts`) và `scaleCam` | Chỉ mới type check |
| Định dạng, hình ảnh và single file | Trên Windows 11 trong Chrome, ngày 2026-09-28: chuyển định dạng ở bốn định dạng, lớp hình ảnh và chuỗi ảnh (image sequence), và bản build single-file, với still capture từ ổ đĩa giống hệt still của studio từng byte. Thiết lập export và các bước kiểm tra một file đã export mới chỉ được viết, chưa chạy. Storyboard card vừa khít cả bốn định dạng, đã xem qua still |
| Âm thanh, vòng 2 | Trên Windows 11, ngày 2026-09-28: dàn nhạc, các lớp nền ambience, các preset hiệu ứng, file ghi âm đặt theo đỉnh (peak) của chúng, một score trên một bản nhạc đã đo, và caption của giọng đọc vẽ ở chân khung hình, cái cuối đã xem qua still. Có tính tất định (deterministic). Chưa nghe thử; các file WAV demo nằm trong một playground |
| Hiệu ứng, vòng 2 | Trên Windows 11 trong Chrome, ngày 2026-09-28: hạt (particles), thiết bị (devices), card trong không gian, chữ chuyển động, các look của post chain, tám loại transition mới. Chỉ có still: chưa phát thử, chưa đo thời gian frame, chưa thử Safari |
| Look, vòng 2 | Trên Windows 11 trong Chrome, ngày 2026-09-28: sky kit, lớp pixel ở 8x, một hành trình xuyên qua các thang tỉ lệ qua bốn thế giới, cú nhảy và bước đi của rig. Đã xem qua still |
| Server riêng của công cụ capture làm mặc định, `--url` cho studio, `timeOfFrame` | Trên Windows 11, ngày 2026-09-28: một still bằng `--frames 300` qua server riêng rơi đúng 5.000 s; `--url` tới một studio không chạy thì dừng kèm lỗi của nó; typecheck đạt. Bộ sinh giờ ghi LF, và output của nó trên Windows giống hệt các file đi kèm từng byte |
| Upload sRGB trên Windows, theo code của nó | Đã so sánh ngày 2026-09-28 với engine design patterns, vốn đã chạy được trên máy này: cùng kiểu upload RGBA8 thuần, cùng cách giải mã sang ánh sáng tuyến tính (linear light), cùng target sRGB. Starter lật các hàng trong shader thay vì khi upload. Chrome ở đó dùng Direct3D 11 trên card đồ hoạ |
| Hình trên Windows so với macOS | Trên Windows 11 trong Chrome, ngày 2026-09-28, lead đã capture phim ví dụ ở 5 s và 18.2 s: độ sáng, hướng và các cạnh khớp với still tham chiếu trên macOS. Chỗ xuống dòng của card khác, vì card đã được sửa từ đó |
| Ba phim thử, với skill đã được cài | Trên Windows 11, ngày 2026-09-28, ba prompt từ bộ sưu tập, mỗi cái được dựng bởi một builder Opus và được owner xem trong studio (không export video). Một tác phẩm kinetic type trong làn ngắn: được chấp nhận sau khi owner phát hiện một dòng chữ hiện ra trong một frame ở 9.9 s, do một hình vẽ được chọn theo thời gian của frame nhưng lại được vẽ ở thời gian của studio. Một cỗ máy 45 giây mà mỗi nốt nhạc là một va chạm, 16:9, trên một score do lead viết bằng code: được chấp nhận sau một vòng; 22 trong 332 cú va nằm ngoài khung hình ở lần kiểm đầu; thời gian frame của nó chưa được đo. Một phim dọc 60 giây về đệ quy theo mười một giai đoạn: dựng tới section mẫu, rồi bị owner dừng lại, vì đã cho thấy những gì cần thấy; transition pull-out của nó bị hỏng và đã được sửa trong engine |
| Những gì các lần thử đã thay đổi | Engine: portal pull-out, viền màu (fringing) khi zoom-in, các công tắc post `tone` và `dither`. Starter: `bun run shots` trên mọi hệ thống, file dữ liệu được scene import, `sheet` với `--frames` và `--exact`, transition và chuyển động camera lặp lại thành cảnh báo kèm `"repeat": true`, nhãn card cho các đoạn nằm trong một bar, `settle` và thêm các easing, `screenPoint` và `inFrame`. Mỗi cái được kiểm bằng typecheck và still trong một bản sao của starter; still của phim ví dụ ở 5 s giống hệt từng byte trước và sau. Các chương: phần kiểm tra chuyển động (`quality-gates.md`), những gì được phép đọc thời gian của frame (`engine-architecture.md`, mục 1), hình ảnh từ score (`sound-and-voice.md`, mục 5.4), các đối tượng kit dùng chung và việc sửa engine trong lúc làm phim (`orchestration.md`) |
| Skill nói chung | Đã chạy từ phỏng vấn đến studio trên các phim thử ở trên. Chưa thử trên một phim về sản phẩm thật có bước nghiên cứu, hay trên route HyperFrames |

## Còn bỏ ngỏ

1. Chạy trình kiểm tra và starter trên Linux và sửa những gì khác biệt (các bước ở trên).
2. Làm một phim về một sản phẩm thật có bước nghiên cứu, và một phim trên route HyperFrames, rồi chỉnh các chương đó theo những gì các lần chạy cho thấy.
3. `STORYBOARD.md` được sinh ra vẫn gọi một đoạn nằm trong một bar theo cách cũ ("2.25 to 3"), trong khi card giờ ghi "FROM BAR 2.25, 0.75 BARS"; đổi nó thì sẽ đổi tài liệu của phim ví dụ.


## Giấy phép

MIT, trong `LICENSE`. Engine trong starter được phát triển từ pdoom-video của Giacomo Magnanini, cũng theo MIT; hãy giữ thông báo bản quyền của nó (`assets/starter/src/engine/LICENSE-pdoom-video.txt`). Các font theo SIL Open Font License, với văn bản giấy phép nằm cạnh chúng.

## Nguồn gốc

Phương pháp này ban đầu được viết bằng tiếng Việt, dưới dạng một playbook, trong repository của các phim tham chiếu. Thư mục này thay thế nó cho các agent.
