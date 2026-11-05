# Dữ kiện về HyperFrames

Những gì họ skill HyperFrames và command line của nó tự nói về chính mình, đọc ngày 2026-09-28 từ các file skill và từ các lần chạy chỉ-đọc CLI 0.8.81 trên macOS. `route-selection.md` và `hyperframes-route.md` ra quyết định dựa trên các dữ kiện này; file này chỉ ghi lại chúng.

Nạp file này khi: bạn cần một cái tên, một lệnh, một mục trong catalogue hay một giới hạn được nêu của HyperFrames, hoặc một chương khác trích dẫn một mục của file này.

HyperFrames thay đổi nhanh. Trước khi dựa vào một dữ kiện ở đây, hãy so `npx hyperframes --version` với 0.8.81 và đọc file skill đã cài được nêu trong dòng đó. Khi chúng mâu thuẫn, file đã cài thắng.

`SK` dưới đây là thư mục chứa các skill của trợ lý, ví dụ `~/.claude/skills`.

## Các dữ kiện này được xác lập thế nào

| Nguồn | Nội dung |
| --- | --- |
| File skill | Mọi `SKILL.md` của 13 skill được nêu tên đều được đọc toàn bộ; đọc các index tham chiếu; các catalogue lớn được đếm bằng script |
| CLI, chạy thật | `npx --yes hyperframes --version`, `--help`, `doctor`, và `--help` của 40 lệnh con. Chạy từ thư mục scratch của phiên với `HYPERFRAMES_NO_TELEMETRY=1 HYPERFRAMES_SKIP_SKILLS=1` |
| Không chạy | `render`, `preview`, `play`, `present`, `init`, `add`, `catalog`, `capture`, `publish`, `auth`, `cloud`, `lambda`, `cloudrun`, `skills check/update`, `telemetry status`, `lint`, `check`, `snapshot`, `beats`, `tts`, `transcribe` |

Tác dụng phụ cần biết: chính CLI đã cập nhật `lastUpdateCheck` trong `~/.hyperframes/config.json` khi chạy `doctor`.

Ký hiệu dùng trong file này: **[stated]** = được viết trong file skill hoặc do CLI in ra. **[inferred]** = kết luận của tôi từ bằng chứng đó.

---

## 1. HyperFrames là gì

- "HyperFrames renders video from HTML" (HyperFrames render video từ HTML): một composition là một file HTML mà DOM khai báo thời gian bằng các thuộc tính `data-*`, runtime animation có thể seek được, và việc phát media do framework nắm giữ. [stated, `SK/hyperframes/SKILL.md`, `SK/hyperframes-core/SKILL.md`]
- Gói npm `hyperframes`, của HeyGen. Registry và các skill nằm tại `github.com/heygen-com/hyperframes`. Tagline của CLI: "Create and render HTML video compositions". [stated]

Mô hình soạn [stated, `SK/hyperframes-core/references/data-attributes.md`, `minimal-composition.md`, `tracks-and-clips.md`]:

| Thành phần | Quy tắc |
| --- | --- |
| Root | Một phần tử có `data-composition-id`, `data-width`, `data-height`; `data-duration` là độ dài render tính bằng giây, đọc một lần lúc compile; `data-fps` tuỳ chọn |
| Clip | Bất kỳ phần tử nào có `data-start` là một clip. `data-duration` bắt buộc trên `div` và host của sub-composition. Cửa sổ hiển thị là nửa mở `[start, start+duration)` |
| `class="clip"` | Chỉ là quy ước. Runtime không bao giờ đọc nó; nó cho hộp full-frame, gợi ý chỉnh sửa trong Studio, lint cảnh báo nếu thiếu |
| `data-track-index` | Chỉ là làn hiển thị trong Studio. Render không bao giờ đọc nó. Thứ tự lớp là CSS `z-index` |
| Thời gian tương đối | `data-start="intro + 2"` nghĩa là 2 s sau khi clip `intro` kết thúc. Bắt buộc có dấu cách quanh toán tử. Tham chiếu không giải được sẽ âm thầm thành 0 |
| Timeline | Đúng một `gsap.timeline({ paused: true })` cho mỗi composition, đăng ký tại `window.__timelines["<id>"]`, key = `data-composition-id` của root |
| Sub-composition | File riêng nạp qua `data-composition-src`, root bọc trong `<template>`, `<style>` và `<script>` nằm bên trong template. Runtime tự lồng các timeline con |
| Media | `<video>` / `<audio>` được tìm bằng truy vấn phẳng trên document, framework seek và decode. `<audio>` cần một `id`, nếu không sẽ không bao giờ được mix. `data-media-start`, `data-volume`, `data-playback-rate` (0.1..10), các làn `data-automation` |
| Biến | `data-composition-variables` trên `<html>`, đọc bằng `window.__hyperframes.getVariables()`, bị ghi đè bởi `render --variables` |

Frame được tạo ra thế nào [stated, `SK/hyperframes-cli/references/preview-render.md`, `doctor-browser.md`, `render --help`]:
- Headless Chrome (`chrome-headless-shell` được ghim phiên bản) nạp composition; runtime seek nó từng frame một; frame được chụp, rồi FFmpeg encode.
- Các đường chụp: `beginframe`, `screenshot`, và `--experimental-fast-capture` (Chrome `drawElementImage`, "default on where it can engage (macOS + hardware-GPU browser)" — mặc định bật ở nơi dùng được: macOS + trình duyệt có GPU phần cứng).
- `--workers auto`: "Each worker launches a separate Chrome process (~256 MB RAM)" (mỗi worker chạy một tiến trình Chrome riêng, ~256 MB RAM).
- Hiệu ứng âm thanh chạy trong một `OfflineAudioContext` bên trong cùng trình duyệt headless đó; preview và render dùng chung một bản cài đặt đồ thị Web Audio. [`SK/hyperframes-audio/SKILL.md`]
- Chrome được ghim phiên bản "because pixel output drifts across Chrome versions" (vì pixel đầu ra trôi giữa các phiên bản Chrome). `render --docker` là đường tái lập được.

Quy tắc tất định (determinism) [stated, `SK/hyperframes-core/references/determinism-rules.md`]:
- "same input time → same pixels" (cùng thời điểm đầu vào → cùng pixel).
- Cấm dùng cho trạng thái hình ảnh: `Date.now()`, `performance.now()`, `Math.random()` không có seed, fetch mạng lúc render, trạng thái hover/scroll/pointer/focus, `repeat: -1` (dùng số lần hữu hạn với `floor`).
- Không bao giờ tween `display`, `visibility` hay `autoAlpha` trên một phần tử clip. Mã lint `gsap_animates_clip_element`.
- Không dùng CSS `transition` trên phần tử có animation.
- Không có allowlist cố định các thuộc tính animate được; lint áp một denylist.

---

## 2. Yêu cầu

### Những gì file skill và CLI nêu

| Hạng mục | Yêu cầu | Nguồn |
| --- | --- | --- |
| Node.js | 22 trở lên | `SK/hyperframes-cli/SKILL.md` |
| FFmpeg, FFprobe | Bắt buộc, có trên PATH | như trên |
| Trình duyệt | Chrome đi kèm được ghim phiên bản, tải về bằng `npx hyperframes browser ensure`, cache dưới `~/.cache/puppeteer/` | `doctor-browser.md`, `doctor` chạy thật |
| Docker | Chỉ cho `render --docker` | `doctor-browser.md` |
| Block WebGPU + html-in-canvas | Brave hoặc Chrome canary qua `PRODUCER_HEADLESS_SHELL_PATH` | `SK/hyperframes-animation/adapters/typegpu.md` |
| Python | Chỉ cho Kokoro TTS cục bộ tuỳ chọn, MusicGen, `extract-audio-data.py` | `SK/media-use/audio/references/requirements.md` |
| `@hyperframes/core` trong project | Cần cho `carve.mjs` (`npm i -D @hyperframes/core`) | `SK/hyperframes-audio/SKILL.md` |

Cài và gọi: `npx hyperframes <command>`. Một project được scaffold ghim `hyperframes@<version>` trong các script của `package.json`; kiểm tra bằng `npx hyperframes@latest upgrade --project . --check`. Skill: `npx hyperframes skills`, hoặc không cần CLI thì `npx skills add heygen-com/hyperframes --all`.

### Hỗ trợ hệ điều hành

Không file skill nào đưa ra ma trận hỗ trợ. Bằng chứng tìm được:
- macOS: `brew install ffmpeg`; fast capture mặc định bật trên macOS; VideoToolbox được nêu cho `--gpu`.
- Linux: "`screenshot` + `software gpu` on Linux is the slow path" (đây là đường chậm trên Linux); VAAPI được nêu; kiểm tra `/dev/shm` bên trong container.
- Windows: help text của `render --frames-cache-dir` nhắc đến "Windows C: exhaustion during long renders" (ổ C: của Windows bị đầy khi render dài); NVENC và QSV được nêu; telemetry nhận diện `wsl`.
- [inferred] Cả ba đều là mục tiêu. Không có gì trong các file nói hệ nào là hạng nhất.

### `doctor` trên máy dùng để đọc các dữ kiện (output chạy thật, CLI 0.8.81)

| Kiểm tra | Kết quả |
| --- | --- |
| Version | 0.8.81 (mới nhất) |
| Node.js | v24.13.1 (darwin arm64) |
| CPU / Memory / Disk | 16 nhân Apple M4 Max / tổng 48 GB / trống 593 GB |
| Frames cache, Archive extractor, Settings lock, Environment | ok |
| FFmpeg / FFprobe | 8.1.2 tại `/opt/homebrew/bin/` |
| Chrome | `chrome-headless-shell` mac_arm 154.0.8037.57 |
| Docker / Docker running | 29.4.0, đang chạy |
| onnxruntime-node, @google/genai | chưa cài, "installs on first use" (cài ở lần dùng đầu) |
| whisper-cpp | **không tìm thấy** (tuỳ chọn, chép lời) |
| TTS (Kokoro) | **chưa cài** (tuỳ chọn, giọng cục bộ) |
| BGM (MusicGen) | **chưa cài** (tuỳ chọn, nhạc cục bộ) |

Chỗ mâu thuẫn: `SK/hyperframes-cli/references/doctor-browser.md` liệt kê mười mục kiểm tra và bỏ sót Frames cache, Archive extractor, Settings lock, whisper-cpp, Kokoro, MusicGen, onnxruntime-node, @google/genai. CLI chạy thật thì in ra chúng. Skill nói `doctor --json` luôn thoát với mã 0; hãy kiểm tra theo trường `ok` trong payload.

### Tài khoản, đăng nhập, dịch vụ trả phí

| Hành động | Cần tài khoản? | Nguồn |
| --- | --- | --- |
| `render` cục bộ | Không [stated] | `SK/ak-hyperframes/SKILL.md`: key HeyGen là tuỳ chọn, "local rendering works without it" (render cục bộ chạy được không cần nó) |
| `lint`, `check`, `snapshot`, `preview`, `play` | Không [inferred] | Vòng dev chín bước trong `SK/hyperframes-cli/SKILL.md` không có bước auth; `auth` chỉ được nhắc cho cloud, publish và media HeyGen |
| `catalog --query` | Không. "Search is entirely local: there is no hosted tier, no account, and the query text is never sent anywhere" (tìm kiếm hoàn toàn cục bộ: không có bản hosted, không tài khoản, và chuỗi truy vấn không bao giờ được gửi đi đâu) | `SK/hyperframes-cli/SKILL.md` |
| `add <item>` | Không cần tài khoản, nhưng lần nào cũng cần mạng | `SK/hyperframes-registry/SKILL.md` |
| `publish` | Có. Publish khi chưa đăng nhập trả về một "authentication-required claim URL" (URL nhận cần xác thực). Host tại hyperframes.dev | `preview-render.md` |
| `cloud render` | Credential HeyGen; "you pay per credit" (trả tiền theo credit); giới hạn upload 200 MB | `SK/hyperframes-cli/references/cloud.md` |
| `lambda`, `cloudrun` | Tài khoản AWS / GCP của riêng bạn | `lambda.md`, `cloudrun.md` |
| Giọng, BGM, SFX, ảnh, icon của HeyGen | CLI `heygen` >= v0.3.0 với `heygen auth login --oauth`. Hạn mức miễn phí cho HeyGen TTS được nêu là 10 phút/tháng | `SK/media-use/references/setup-providers.md`, `requirements.md` |
| Phương án dự phòng offline | Kokoro TTS, MusicGen BGM, thư viện SFX đi kèm | `requirements.md`, `sfx.md` |
| `figma` | `FIGMA_TOKEN` | `SK/hyperframes-cli/SKILL.md` |
| `snapshot --describe` | `GEMINI_API_KEY`, mặc định chạy khi có key | `snapshot --help` |

Hành vi workflow cần biết: các workflow chạy `npx hyperframes auth status` ở bước Setup và, ở chế độ cộng tác, chờ người dùng đăng nhập hoặc chọn offline. [`SK/faceless-explainer/SKILL.md` Step 0]

### Telemetry và các lệnh gọi ra ngoài

- Telemetry sử dụng ẩn danh, **mặc định bật**. Trên máy đã kiểm tra, `~/.hyperframes/config.json` có `telemetryEnabled: true`.
- Cách tắt: `npx hyperframes telemetry disable`, `HYPERFRAMES_NO_TELEMETRY=1`, `DO_NOT_TRACK=1`.
- Sự kiện mang `sandbox_runtime` và `agent_runtime` (nhận diện `claude_code` dựa vào sự tồn tại của biến môi trường). [`upgrade-info-misc.md`]
- `media-use` gửi sự kiện tới PostHog; khi đăng nhập HeyGen thì "usage is linked to your account email" (việc sử dụng được gắn với email tài khoản của bạn). [`SK/media-use/references/meta.md`]
- Skill CLI bảo agent gửi `npx hyperframes feedback --rating <0-10>` sau mỗi lần render đã được xác minh, tới "a public channel" (một kênh công khai). [`SK/hyperframes-cli/SKILL.md`]
- `init` kiểm tra skill với GitHub ở mỗi lần chạy; `--skip-skills` đang "temporarily ignored" (tạm thời bị bỏ qua); tắt bằng `HYPERFRAMES_SKIP_SKILLS=1`.
- Đường font mặc định: một Google font không đi kèm sẽ được tải từ Google Fonts lúc build. [`SK/hyperframes-creative/references/typography.md`]

---

## 3. Bản đồ CLI

Tất cả lấy từ `--help` chạy thật, CLI 0.8.81, trừ khi có đánh dấu.

### Thiết lập
| Lệnh | Làm gì |
| --- | --- |
| `init [NAME]` | Scaffold một project. Cờ: `--example`, `--resolution`, `--video`, `--audio`, `--tailwind`, `--non-interactive`, `--skill` |
| `capture [URL]` | Chụp một website thành các component HyperFrames chỉnh sửa được; screenshot, token, asset |
| `skills check` / `skills update [names]` / `skills` trơn | Kiểm tra, làm mới, hoặc cài bộ skill |
| `doctor` | Kiểm tra phụ thuộc hệ thống và môi trường |
| `browser ensure\|path\|clear` | Quản lý Chrome dùng để render |
| `upgrade [--check] [--project]` | Kiểm tra phiên bản CLI; nâng các script đã ghim của một project |
| `auth login\|status\|logout\|refresh` | Credential HeyGen |
| `telemetry enable\|disable\|status` | Quản lý telemetry ẩn danh |
| `docs [TOPIC]` | Tài liệu tại chỗ: `data-attributes`, `examples`, `rendering`, `gsap`, `troubleshooting`, `compositions` |
| `figma asset\|tokens\|component` | Nhập từ Figma qua REST |

### Soạn
| Lệnh | Làm gì |
| --- | --- |
| `catalog [--query] [--type] [--tag] [--on-device]` | Tìm hoặc duyệt block và component trong registry |
| `add <NAME>` | Cài một block, một component, hoặc mọi block có một tag |
| `timeline [DIR]` | In track và clip. Lệnh con `move`, `trim`, `split`, `delete`, `set`, `duplicate`, `ids`, `apply`, `undo` |
| `history show\|undo\|restore\|peek\|pin\|begin\|end` | Các thay đổi đã ghi lại của project |
| `compositions` | Liệt kê mọi composition trong một project |
| `info` | Metadata của project |
| `media-treatment` | Khám phá, áp, xoá các look tất định trên một `<img>` hoặc `<video>` |
| `media-use resolve\|doctor\|stats\|adopt\|candidates\|reuse\|from\|params\|analyze` | Giải và thao tác trên media của project |

### Kiểm tra
| Lệnh | Làm gì |
| --- | --- |
| `lint` | Kiểm tra tĩnh `index.html` và `compositions/` |
| `check` | Lint, runtime, layout, motion, độ tương phản WCAG trong một phiên trình duyệt. Cổng kiểm cuối cùng. Mặc định 9 mẫu |
| `snapshot [--at] [--frames] [--zoom] [--angle] [--against]` | Ảnh PNG tĩnh tại các thời điểm chọn; mặc định 5 frame; ghi vào `snapshots/` |
| `keyframes [--shot] [--ghost] [--angle]` | Liệt kê keyframe và chẩn đoán onion-skin |
| `compare <paths>` | Các biến thể tại một mốc thời gian trên một sheet có nhãn, tối đa 16 |
| `grade-compare --for` | Các bản grade màu ứng viên trên một frame tham chiếu |
| `validate`, `inspect`, `layout` | Alias đã lỗi thời của các phần của `check` [stated trong skill] |

### Preview
| Lệnh | Làm gì |
| --- | --- |
| `preview [--background] [--port 3002]` | Khởi động Studio. Còn có `--status`, `--stop`, `--list`, `--kill-all`, `--selection`, `--context` |
| `play [--port 3003]` | Player trình duyệt gọn nhẹ, không có editor |
| `present [--port 3004]` | Bộ slide ở chế độ người trình bày, đồng bộ với khán giả |

### Tiền xử lý âm thanh và media
| Lệnh | Làm gì |
| --- | --- |
| `beats [DIR]` | Dò beat trong track nhạc (headless Chrome), ghi `beats/<audio>.json` |
| `tts [INPUT]` | Giọng nói cục bộ, chỉ với Kokoro-82M |
| `transcribe <INPUT>` | Mốc thời gian theo từng từ; engine `parakeet`, `whisper`; nhập `.json`, `.srt`, `.vtt` |
| `normalize-audio --reference --target` | Khớp độ lớn của một clip với clip khác theo LUFS tích hợp |
| `remove-background [INPUT]` | WebM trong suốt, ProRes 4444 hoặc PNG qua model cục bộ |

### Render
| Lệnh | Làm gì |
| --- | --- |
| `render` | Định dạng `mp4`, `webm`, `mov`, `gif`, `png-sequence`, `hls`. Chất lượng `draft`, `looks` (mặc định, CRF 16), `delivery`. `--batch`, `--variables`, `--docker`, `--workers`, `--low-memory-mode`, `--resume` |
| `benchmark` | Render với 5 cấu hình preset, so tốc độ và dung lượng |
| `cloud render\|list\|get\|delete` | Render do HeyGen host |
| `lambda ...`, `cloudrun ...` | Render phân tán tự quản trên AWS hoặc GCP |

### Publish và báo cáo
| Lệnh | Làm gì |
| --- | --- |
| `publish [--public] [--update] [--space]` | Upload mã nguồn lên một URL host ổn định, mặc định riêng tư |
| `feedback --rating` | Phản hồi ẩn danh; `--search-miss` báo một lỗ hổng trong catalogue; `--file-issue` publish một bản repro |
| `events` | Sự kiện telemetry về việc dùng skill. Skill nói agent không nên tự tay gọi nó |

Các chỗ mâu thuẫn giữa văn bản skill và CLI chạy thật:
- `render --fps`: bảng trong skill nói `24, 30, 60`; CLI chấp nhận từ 1 đến 240 và số hữu tỉ như `30000/1001`.
- `timeline`: skill mô tả một công cụ chỉ in ra; CLI có lệnh con chỉnh sửa.
- `history`: có trong CLI, không được mô tả trong skill nào đã cài.
- `play`, `figma`, `events`, `media-use` trả lời `--help` nhưng không có trong danh sách `--help` cấp cao nhất.
- `SK/faceless-explainer/SKILL.md` render với `--quality high`; skill CLI gọi `high` là tên cũ của `delivery`.
- `SK/hyperframes-cli/references/init-and-scaffold.md` liệt kê bộ skill có chứa `-media`; skill hiện tại tên là `media-use`.

---

## 4. Bản đồ họ skill

### Cài cùng với họ skill

| Skill | Phụ trách | Nạp khi | Không được dùng cho |
| --- | --- | --- | --- |
| `hyperframes` (26 file) | Điểm vào: trạng thái project, phỏng vấn ý định, định tuyến, các hợp đồng brief / storyboard / review / production / dispatch / frame-worker | Mọi yêu cầu video mới; tiếp tục một project | Viết HTML composition; nó không bao giờ phụ trách việc thực thi |
| `hyperframes-core` (11) | Hợp đồng composition: `data-*`, clip, track, sub-composition, biến, tính tất định, công thức chỉnh sửa cho người làm | Trước khi viết bất kỳ HTML composition nào; cắt, trim, sắp xếp lại | Kỹ thuật motion, định hướng sáng tạo, mix |
| `hyperframes-cli` (11) | Vòng dev và hợp đồng của mọi lệnh | Chạy hoặc chẩn đoán bất kỳ lệnh nào | Chọn media hay motion |
| `hyperframes-animation` (122) | Quy tắc, blueprint, transition, kỹ thuật, adapter runtime, script bản đồ animation | Mọi việc về motion | Hợp đồng composition; quyết định thương hiệu |
| `hyperframes-creative` (79) | Design spec, preset frame, bảng màu, typography, phong cách hình ảnh, lời dẫn, chỉ đạo beat, audio-reactive, công thức storyboard | Look, nhịp, kịch bản | Công thức animation; không được ghi đè quy tắc của core |
| `hyperframes-keyframes` (3) | Keyframe an toàn khi seek, chuyển động camera, chẩn đoán `hyperframes keyframes` | Punch-in, Ken Burns, reframe, chiều sâu 3D, chuyển tiếp match hoặc whip | "broad scene strategy, brand design, media sourcing, captions, or general video planning" (chiến lược cảnh tổng thể, thiết kế thương hiệu, tìm media, phụ đề, hay lập kế hoạch video chung); cắt nguồn |
| `hyperframes-registry` (12) | Tìm, cài, nối block và component; đóng góp mục mới | Trước khi tự tay dựng bất kỳ look có tên nào | Ví dụ (dùng `init --example` thay thế) |
| `hyperframes-studio` (1) | Quy ước bố cục timeline và vùng an toàn | Dựng một project mà người khác mở trong Studio | Cách thực hiện một chỉnh sửa riêng lẻ |
| `hyperframes-audio` (7) | Mix âm thanh đã đặt: fade, automation, carve, chuỗi hiệu ứng, bus submix | Âm thanh đã nằm trên timeline cần được mix | Tìm nguồn hoặc tạo âm thanh; thời gian clip |
| `media-use` (90) | Giải, tạo, thao tác, ghi nhớ media: BGM, SFX, ảnh, icon, logo, giọng, grade, LUT; TTS, chép lời, phụ đề; media treatment | Mọi nhu cầu về asset, âm thanh, giọng, phụ đề hay look của footage | Mix track đã đặt; phát lại |
| `faceless-explainer` (24) | Workflow: từ văn bản thành video giải thích có lời dẫn với hình ảnh tự tạo | Chủ đề, bài viết hoặc ghi chú, không có sản phẩm và không có site | Video dựng từ một website; mọi thứ chưa rõ quay về `/hyperframes` |

### Được skill điểm vào nêu tên, **không cài mặc định**

Trên máy đã kiểm tra, các skill này không có.

| Skill | Điều kiện định tuyến (từ `SK/hyperframes/references/routes/<name>.md`) |
| --- | --- |
| `general-video` | Mọi video tuỳ biến; cũng thực thi mọi brief `flow: companion` |
| `product-launch-video` | Promo, ra mắt, tour site từ một URL; dùng `capture` |
| `pr-to-video` | Giải thích một PR GitHub, đọc qua `gh` |
| `motion-graphics` | Đơn vị ngắn không lời dẫn, thường dưới 10 s; MP4 hoặc WebM/MOV có alpha |
| `music-to-video` | Video khớp beat dẫn bởi `audiomap.json` |
| `slideshow` | Bộ slide điều hướng được với `SlideshowController`; "not an MP4" (không phải MP4) |
| `embedded-captions` | Phụ đề trên footage có sẵn, catalogue nhận diện phụ đề |
| `talking-head-recut` | Card overlay được thiết kế trên footage có sẵn |
| `remotion-to-hyperframes` | Chuyển mã nguồn Remotion có sẵn |
| `figma` | Nhập asset, token, component, frame storyboard |
| `animate-text` (bên ngoài, `pixel-point/animate-text`) | 24 hiệu ứng chữ có tên; cố ý không vendor vào |

Chúng được cài lười (khi cần) bằng `npx hyperframes skills update <name>`. Lệnh đó không được chạy, nên nội dung của chúng chưa biết.

---

## 5. Luồng riêng của skill điểm vào

Nguồn: `SK/hyperframes/SKILL.md` và `SK/hyperframes/references/`.

### Bước 1: bắt đầu từ trạng thái project (khớp đầu tiên thắng)

| Trạng thái | Hành động |
| --- | --- |
| Yêu cầu chuyển Remotion rõ ràng | Định tuyến thẳng, bỏ qua lớp ý định |
| Một thao tác cụ thể trên project có sẵn | Chỉ làm việc đó, nạp `/hyperframes-cli` |
| Một chỉnh sửa cụ thể | Thực hiện chỉnh sửa; dùng `npx hyperframes timeline --json` thay vì đọc HTML |
| Có `BRIEF.md` | Đọc `workflow` và `flow`, thực thi, không hỏi gì |
| Có `hyperframes.json` hoặc `STORYBOARD.md` | Tiếp tục; tối đa một câu hỏi định tuyến |
| Tạo mới | Chạy lớp ý định, rồi định tuyến một lần |

### Bước 2: bảng định tuyến, theo sản phẩm được yêu cầu (theo thứ tự ưu tiên)

`remotion-to-hyperframes` → `slideshow` → `embedded-captions` → `talking-head-recut` → `music-to-video` → `motion-graphics` → `pr-to-video` → `product-launch-video` → `faceless-explainer` → `general-video`.

Những quy tắc đáng mang theo:
- "A music file selects `/music-to-video` only when its beat grid drives the piece. Music used as a bed does not override the subject-matched route." (Một file nhạc chỉ chọn `/music-to-video` khi lưới beat của nó dẫn dắt tác phẩm. Nhạc dùng làm nền không ghi đè route khớp theo chủ đề.)
- "Specialized narrative workflows support up to about 3 minutes and are strongest around 30–90s." (Các workflow kể chuyện chuyên biệt hỗ trợ tới khoảng 3 phút và mạnh nhất ở khoảng 30–90 s.)

### Lớp ý định: tám bước (`references/intent-interview.md`)

1. Bộ nhớ trước câu hỏi: `prefs.mjs get` và `recipe.mjs list` từ `media-use`.
2. Phân loại đầu vào: yêu cầu đã định hình hay chưa định hình.
3. Chọn route, đọc `routes/<workflow>.md`.
4. Vòng pitch, chỉ cho yêu cầu chưa định hình: năm concept trên năm hướng, ít nhất hai cái có xác suất ước tính dưới 0.10 (`references/pitch-round.md`).
5. Các trường bắt buộc của route: mỗi trường một câu hỏi, phương án khuyến nghị đứng đầu.
6. Hai câu hỏi về dạng chạy, tách riêng: có storyboard hay không, và automation hay companion.
7. Đề nghị năng lực tuỳ chọn từ `references/capability-menu.md`; design spec là một câu hỏi ba trạng thái.
8. Bàn giao: một lần kiểm tra tích hợp, các trường được nêu và được suy ra hiển thị tách riêng, "Revision is not confirmation" (sửa không phải là xác nhận).

### Nó hỏi người dùng những gì

| Trường | Chính sách (`references/brief-contract.md` § 2) |
| --- | --- |
| `message` | Được suy ra và nhắc lại thành một câu |
| `destination` | Chỉ hỏi khi chưa biết và nó làm đổi tỉ lệ khung |
| `aspect` | Được suy ra: feed `1080x1080`, TikTok/Reels/Shorts `1080x1920`, YouTube/web `1920x1080` |
| `length`, `angle` | Khuyến nghị kèm lý do |
| `language`, `audience` | Được suy ra, nêu rõ |
| `narration` | Tuỳ theo route |
| `storyboard`, `flow` | Hỏi cuối cùng |

Chế độ được suy ra, không bao giờ hỏi: `companion` hoặc `automation + storyboard: yes` → cộng tác; `automation + storyboard: no` → tự chủ. "Rendering remains user-gated in both modes." (Ở cả hai chế độ, render vẫn phải chờ người dùng cho phép.)

### Các file trạng thái giữ trong một project

| File | Vai trò | Định nghĩa trong |
| --- | --- | --- |
| `hyperframes.json` | Cấu hình project: URL registry, đường cài, skill sở hữu, `media.autoProxy` | `SK/hyperframes-registry/references/install-locations.md` |
| `package.json` | Các script `hyperframes@<version>` đã ghim | `SK/hyperframes/SKILL.md` |
| `BRIEF.md` | Ý định đã xác nhận; artifact định tuyến duy nhất; được ghi ngay sau `init` | `references/brief-format.md` |
| `STORYBOARD.md` | Kế hoạch: frontmatter cộng các mục `## Frame N`, trạng thái `outline` → `built` → `animated` | `references/storyboard-format.md` |
| `SCRIPT.md` | Lời dẫn đã chốt, tuỳ chọn | `references/script-format.md` |
| `frame.md` | Design spec, luôn viết thường | `SK/hyperframes-creative/references/design-spec.md` |
| `storyboard.html` | Tờ phác thảo tĩnh người dùng xem duyệt; các ô `id="frame-NN"` | `SK/hyperframes-creative/references/storyboard-recipe.md` |
| `index.html`, `compositions/frames/NN-*.html` | Bộ phim | `references/production-loop.md` |
| `audio_meta.json`, `caption_groups.json` | Giọng, thời gian từng từ, BGM, SFX; nhóm phụ đề | `SK/media-use/references/audio.md`, `SK/faceless-explainer/SKILL.md` |
| `.hyperframes/frame-packets/`, `.hyperframes/caption-skin.html`, `.hyperframes/anim-map` | Gói việc cho worker, skin phụ đề, bản đồ animation | `references/frame-worker-core.md` |
| `.media/manifest.jsonl`, `.media/preferences.json`, `.media/recipes/` | Sổ media, sở thích đã nhớ, công thức đã đóng băng | `SK/media-use/references/memory.md` |
| `capture/`, `snapshots/`, `renders/`, `beats/` | Output capture, ảnh tĩnh, bản render, file beat | Tham chiếu CLI |

File cấp cá nhân nằm ngoài project: `~/.hyperframes/`, `~/.media/`, `~/.heygen/credentials`, `~/.cache/hyperframes/`, `~/.cache/puppeteer/`.

---

## 6. Các catalogue nó đã có sẵn

### 6.1 Transition giữa các cảnh

File: `SK/hyperframes-animation/transitions/overview.md` (lựa chọn), `catalog.md` (quy tắc cứng, định tuyến), `css-*.md` (code), `TRANSITION-REGISTRY.md` (tập con cho máy đọc).

Transition CSS, 32 tên trong 13 file (đã đếm):

| File nhóm | Tên |
| --- | --- |
| `css-push.md` | Push Slide, Vertical Push, Elastic Push, Squeeze |
| `css-radial.md` | Circle Iris, Diamond Iris, Diagonal Split |
| `css-3d.md` | 3D Card Flip |
| `css-scale.md` | Zoom Through, Zoom Out |
| `css-dissolve.md` | Crossfade, Blur Crossfade, Focus Pull, Color Dip |
| `css-cover.md` | Staggered Color Blocks, Horizontal Blinds, Vertical Blinds |
| `css-light.md` | Light Leak, Overexposure Burn, Film Burn |
| `css-distortion.md` | Glitch, Chromatic Aberration, Ripple, VHS Tape |
| `css-mechanical.md` | Shutter, Clock Wipe |
| `css-grid.md` | Grid Dissolve |
| `css-other.md` | Gravity Drop, Morph Circle |
| `css-blur.md` | Blur Through, Directional Blur |
| `css-destruction.md` | Page Burn |

Được tuyên bố là không làm được bằng CSS: star iris, tilt-shift, lens flare, hinge/door.

Transition shader (WebGL, gói `@hyperframes/shader-transitions`, API `HyperShader.init`). Các block registry, 14 cái, từ `SK/hyperframes-registry/references/discovery.md`:

| Block | Ý nghĩa |
| --- | --- |
| `chromatic-radial-split` | Tách sắc sai theo hướng toả tròn |
| `cinematic-zoom` | Zoom blur kịch tính |
| `cross-warp-morph` | Morph với biến dạng đan chéo |
| `domain-warp-dissolve` | Biến dạng miền bằng noise fractal |
| `flash-through-white` | Crossfade qua chớp trắng |
| `glitch` | Hiệu ứng lỗi kỹ thuật số |
| `gravitational-lens` | Biến dạng thấu kính hấp dẫn |
| `light-leak` | Light leak kiểu điện ảnh |
| `ridged-burn` | Cháy nhiễu loạn dạng gờ |
| `ripple-waves` | Biến dạng gợn sóng đồng tâm |
| `sdf-iris` | Mở iris bằng signed distance field |
| `swirl-vortex` | Biến dạng xoáy lốc |
| `thermal-distortion` | Biến dạng hơi nóng |
| `whip-pan` | Whip-pan camera nhanh |

"Use ≤2 per video." (Dùng ≤2 cái mỗi video.) Tên block không phải là tên shader.

Công cụ hỗ trợ chọn trong `overview.md`: Năng lượng → loại chính (calm, medium, high), Cảm xúc → loại (9 cảm xúc), Vị trí trong mạch kể (6), cường độ blur, preset `snappy`, `smooth`, `gentle`, `dramatic`, `instant`, `luxe`.

Registry của injector, 5 tên hợp lệ làm `transition_in`: `crossfade`, `blur-crossfade`, `push-slide` (LEFT/RIGHT/UP/DOWN), `zoom-through`, `squeeze`. Mặc định: năng lượng cao `zoom-through`, êm `blur-crossfade`, tối đa 2.0 s. Cùng năm cái đó trong `SK/faceless-explainer/scripts/lib/transitions.json`.

Các cut trong cùng frame, do worker dựng, không phải giá trị `transition_in` hợp lệ (`SK/faceless-explainer/references/cut-catalog.md`): Zoom-Through, Inverse Zoom-Through, Cut the Curve, Waterfall Cut.

Mâu thuẫn nhỏ: `overview.md` xếp 3D flip vào Scale/zoom và Shutter cùng Clock Wipe vào Reveal/mask; `catalog.md` cho chúng nhóm riêng.

### 6.2 Quy tắc motion

Index: `SK/hyperframes-animation/rules-index.md`. Nội dung: `SK/hyperframes-animation/rules/<name>.md`. 48 file, 49 mục index (một quy tắc được liệt kê hai lần), tất cả dựa trên GSAP.

| Nhóm | Quy tắc | Ý nghĩa |
| --- | --- | --- |
| Chữ | `hacker-flip-3d` | Lật 3D từng ký tự với thay glyph tất định |
| | `vertical-spring-ticker` | Cuộn dọc kiểu máy đánh bạc trong một cột có mask |
| | `counting-dynamic-scale` | Đếm tăng với tỉ lệ lớn dần theo giá trị (cũng nằm trong Dữ liệu) |
| | `discrete-text-sequence` | Thay cả trạng thái chữ tại các ngưỡng thời gian |
| | `asr-keyword-glow` | Từ khoá phát sáng khớp với mốc thời gian từng từ |
| | `3d-text-depth-layers` | Các lớp chữ lệch nhau làm khối đùn giả |
| | `context-sensitive-cursor` | Con trỏ gõ chữ đổi màu theo từng đoạn |
| | `dynamic-content-sequencing` | Cửa sổ cụm từ tính từ kịch bản |
| | `kinetic-beat-slam` | Cụm từ đập vào theo một mảng beat dùng chung |
| | `gradient-text-sweep` | Gradient được tween xuyên qua nét chữ |
| | `chromatic-glitch` | Glitch tách RGB hoặc cắt lát trên thời gian lượng tử hoá đã băm |
| Dữ liệu | `stat-bars-and-fills` | Thanh tăng trưởng, thanh hoặc vòng tiến độ, wipe đánh giá sao |
| | `chart-scrub-readout` | Đầu phát quét qua biểu đồ đã vẽ, tooltip bước qua dữ liệu |
| Camera | `coordinate-target-zoom` | Zoom tới phần tử lệch tâm, wrapper lồng nhau, `T = -offset` |
| | `camera-cursor-tracking` | Viewport khoá theo con trỏ gõ chữ đang di chuyển |
| | `multi-phase-camera` | Các pha lùi ra, lấy nét, đẩy vào cộng trôi nhẹ |
| | `viewport-change` | Camera một wrapper `.world` duy nhất, `T = -offset × S` |
| | `3d-camera-flight` | Bay phối cảnh xuyên qua một thế giới DOM bố trí 3D |
| | `depth-of-field-blur` | Rack focus bằng `filter: blur()` được tween |
| Bố cục | `avatar-cloud-network` | Avatar trên một vòng với đường SVG nối về tâm |
| | `3d-page-scroll` | Trang web như một card 3D nghiêng đang cuộn |
| | `center-outward-expansion` | Cụm ở tâm giãn ra các vị trí cuối |
| | `split-tilt-cards` | Hai card với `rotationY` ngược nhau |
| | `orbit-3d-entry` | Lật vào từ 3D rồi ổn định thành quỹ đạo |
| | `ai-tracking-box` | Khung ngoặc nhận diện bám theo mục tiêu |
| | `depth-scatter-assemble` | Phần tử tản ra hoặc tụ lại từ một đám mây 3D |
| | `anchored-layout-expand` | Container ghim cạnh lớn dần theo một trục, chỉ dùng transform |
| SVG | `svg-icon-enrichment` | Animate các phần SVG bên trong một icon |
| | `svg-path-draw` | Nét tự vẽ bằng dash offset |
| Ambient (nền) | `sine-wave-loop` | Vòng lặp "thở" hữu hạn |
| | `ambient-glow-bloom` | Quầng sáng toả tròn mềm phía sau phần tử chính, độ mờ đỉnh ≤ ~0.45 |
| Transition và motion | `reactive-displacement` | Phần tử vào đẩy phần tử đang ra |
| | `press-release-spring` | Bấm nút và hồi lò xo |
| | `physics-press-reaction` | Nén khi click trên mục tiêu và con trỏ cùng lúc |
| | `cursor-click-ripple` | Con trỏ di chuyển, bấm, gợn sóng lan ra |
| | `cursor-drag` | Nắm, di chuyển kèm bóng mờ, thả và hít vào chỗ |
| | `multi-cursor-choreography` | 2 đến 4 con trỏ có nhãn trên một canvas |
| | `control-target-sync` | Control và mục tiêu gắn với nó đổi trong cùng một beat |
| | `scale-swap-transition` | Morph giữa hai phần tử tại cùng một tâm |
| | `card-morph-anchor` | Container morph kích thước, bo góc, bề mặt giữa các shot |
| | `theme-crossfade-morph` | Toàn bộ theme đổi skin dưới một điểm neo cố định |
| | `spring-pop-entrance` | Pop xuất hiện chuẩn, `back.out` |
| | `motion-blur-streak` | Blur vận tốc có hướng giả |
| | `waterfall-entry` | Thác xuất hiện so le |
| | `particle-burst` | Nổ confetti hoặc chấm tất định, **giới hạn ~40 hạt** |
| | `nudge-curve` | Trượt nhóm chậm-nhanh-chậm |
| Công thức | `gsap-effects` | Mẫu dùng ngay: typewriter, audio visualizer |
| | `css-marker-patterns` | Các chế độ marker: highlight, circle, burst, scribble, sketchout |

### 6.3 Blueprint cảnh

Index: `SK/hyperframes-animation/blueprints-index.md`. Nội dung: `blueprints/<id>.md`. 22 cái, "reverse-engineered from 178 golden product-launch clips" (dịch ngược từ 178 clip ra mắt sản phẩm mẫu mực). Vai trò: Hook, Problem, Product_Intro, Key_Feature, Benefits, Social_Proof, CTA, Brand_Outro.

| Blueprint | Thời lượng | Ý nghĩa |
| --- | --- | --- |
| `kinetic-type-beats` | 3.0–12.9 s | Chữ đậm, chuyển động chính là các chữ thay đổi; ngựa thồ, 6 vai trò |
| `typewriter-reveal` | 3.6–7 s | Một caret gõ và sửa một dòng, rồi chốt bằng thương hiệu |
| `spatial-pan-stations` | 7–10 s | Các trạm trên một canvas quá khổ, một camera pan giữa chúng |
| `camera-journey` | 5.6–11.1 s | Hành trình camera nhiều chặng; dạng con A khứ hồi hành động, B bay 3D không con trỏ |
| `zoom-out-workspace-reveal` | 6.8–11 s | Chi tiết cận, một cú zoom-out chậm dần hé lộ toàn cảnh |
| `constellation-hub` | 5–8 s | Các nút vây quanh tâm, rồi hội tụ về lõi |
| `grid-card-assemble` | 3.0–10.5 s | Các mục tự xếp thành lưới hoặc danh sách |
| `logo-assemble-lockup` | 4.4–11 s | Một biểu tượng hình thành và chốt thành lockup |
| `cursor-ui-demo` | 4.0–12.9 s | Con trỏ điều khiển một UI dựng lại |
| `device-surface-showcase` | 5–11.3 s | Mockup thiết bị giữ làm nhân vật chính trong khi màn hình luân phiên |
| `prompt-type-submit-generate` | 5.2–12 s | Prompt được gõ vào, máy trả lời |
| `agent-progress-theater` | 4.2–11.6 s | Loader và trạng thái, rồi một checklist tự đánh dấu |
| `panel-edit-live-sync` | 5.3–11.9 s | Control trong inspector và bề mặt gắn với nó cập nhật cùng lúc |
| `transcript-scroll-artifact-reveal` | 5–11.8 s | Đi qua một bề mặt dài, rồi hé lộ artifact |
| `dataviz-countup` | 4–12 s | Đếm tăng, biểu đồ, lưới số liệu làm nhân vật chính |
| `titlecard-reveal` | 3–5 s | Một tiêu đề điềm tĩnh với một chuyển động tiết chế |
| `comparison-split` | 4–6 s | Hai mục với độ nghiêng mở sách đối xứng |
| `overwhelm-surround` | 6–9 s | Tích tụ dần đến khi bị vây kín |
| `ticker-takeover` | 5–7 s | Từ đang luân phiên bị thay bởi một phần tử chính lao vào |
| `fixed-anchor-cycle` | 6.6–11.1 s | Một phần tử được ghim, xung quanh luân phiên |
| `video-text-pivot` | 6–8 s | Video trượt sang bên cho một số liệu, rồi kinetic text |
| `cta-morph-press` | 4–6 s | Biểu tượng co lại thành CTA, con trỏ click |

13 ví dụ chạy được: `SK/hyperframes-animation/examples/*.html`.

### 6.4 Kỹ thuật

File: `SK/hyperframes-animation/techniques.md`. 13 cái:

1. SVG Path Drawing. 2. Canvas 2D Procedural Art. 3. CSS 3D Transforms. 4. Per-Word Kinetic Typography. 5. Lottie Animation. 6. Video Compositing. 7. Character-by-Character Typing. 8. Variable Font Axis Animation. 9. GSAP MotionPathPlugin. 10. Velocity-Matched Transitions. 11. Audio-Reactive Animation. 12. Clip-Path Reveal Masks. 13. WebGL Fragment Shader Art.

Cộng thêm `SK/hyperframes-animation/references/motion-blur.md` và 24 id hiệu ứng `animate-text` bên ngoài được liệt kê trong `adapters/animate-text.md`.

### 6.5 Adapter runtime

Thư mục: `SK/hyperframes-animation/adapters/`. Skill đếm bảy runtime.

| Runtime | File | Hook | Ghi chú |
| --- | --- | --- | --- |
| GSAP | `gsap.md`, `gsap-easing-and-stagger.md`, `gsap-timeline-and-labels.md`, `gsap-transforms-and-perf.md` | `window.__timelines` | "default for 95% of motion work" (mặc định cho 95% việc motion) |
| Lottie / dotLottie | `lottie.md` | `window.__hfLottie` | `autoplay: false` |
| Three.js / WebGL | `three.md` | sự kiện `hf-seek`, `window.__hfThreeTime` | Không tự suy ra thời lượng; bắt buộc có `data-duration` ở root |
| Anime.js v4 | `animejs.md` | `window.__hfAnime` | Không tự phát hiện trên v4 |
| CSS keyframes | `css-animations.md` | `animation-name` đã tính | Thời lượng và số lần hữu hạn |
| WAAPI | `waapi.md` | `document.getAnimations()` | `fill: "both"` |
| TypeGPU / WebGPU | `typegpu.md` | `hf-seek` với `waitUntil`, `window.__hfTypegpuTime` | `data-requires-webgpu` |
| (mẫu) HTML-in-canvas | `html-in-canvas-patterns.md` | `drawElementImage` | 10 hiệu ứng; "1-3 hero beats per video" (1-3 beat chính mỗi video) |
| (bên ngoài) animate-text | `animate-text.md` | skill riêng | 24 id hiệu ứng |

Các hiệu ứng HTML-in-canvas được nêu tên: 3D Rotation with Bloom, Magnetic Cursor Distortion, Shatter, Liquid Surface, Portal, Noise Dissolve, Holographic, Scan Lines + CRT, Frosted Glass Blur, Pixel Sort.

### 6.6 Registry

File: `SK/hyperframes-registry/SKILL.md`, `references/discovery.md`. Hai loại mục: block (sub-composition có kích thước, thời lượng, timeline riêng) và component (đoạn mã dán vào một host).

Số lượng được tuyên bố, ba con số khác nhau:

| Tuyên bố | Ở đâu |
| --- | --- |
| "roughly 400 hosted items" (khoảng 400 mục được host) | Mô tả của `SK/hyperframes-registry/SKILL.md` |
| "~400 blocks and components" (~400 block và component) | `SK/faceless-explainer/SKILL.md` Step 4 |
| "97 of the registry's 180 blocks" (97 trong 180 block của registry) | `SK/hyperframes-registry/references/discovery.md` |
| "50+ installable scene compositions" (50+ composition cảnh cài được) | `SK/hyperframes/references/capability-menu.md` |

Chưa đếm số thật; xem Câu hỏi mở.

Các nhóm block trong `discovery.md` (số ghi ở heading, số dòng thực sự liệt kê):

| Nhóm | Số ở heading | Đã liệt kê | Ví dụ |
| --- | --- | --- | --- |
| Transition shader | 14 | 14 | xem 6.1 |
| Gallery transition | 13 | 13 | `transitions-push`, `transitions-dissolve`; chỉ để tham khảo |
| Liquid Glass | 7 | 5 | `ios26-liquid-glass`, `macos-tahoe-liquid-glass`, `vfx-liquid-glass` |
| VFX | 6 | 6 | `vfx-iphone-device`, `vfx-liquid-background`, `vfx-magnetic`, `vfx-portal`, `vfx-shatter`, `vfx-text-cursor` |
| Showcase | 6 | 6 | `app-showcase`, `apple-money-count`, `nyc-paris-flight` |
| Bản đồ + trực quan hoá dữ liệu | 8 | 9 tên | `us-map`, `world-map`, `data-chart`, `flowchart` |
| Overlay mạng xã hội | 7 | 7 | `x-post`, `yt-lower-third`, `macos-notification` |
| Thương hiệu + UI 3D | 2 | 2 | `logo-outro`, `ui-3d-reveal` |
| Đoạn code | 24 | 1 | `code-snippet-apple-terminal-pro`; họ chrome thứ hai không được nêu tên |
| Animation code | 9 | 8 | `code-typing`, `code-diff`, `code-morph`, `code-3d-extrude`, `code-particle-assemble` |

Component được liệt kê: `grain-overlay`, `shimmer-sweep`, `morph-text`, `grid-pixelate-wipe`, `parallax-zoom`, `parallax-unzoom`. Cũng được nêu tên ở chỗ khác: `motion-blur`, `shutter-slam`.

Các ví dụ của init (tập đóng, `init-and-scaffold.md`): `blank`, `warm-grain`, `play-mode`, `swiss-grid`, `vignelli`, `decision-tree`, `kinetic-type`, `product-promo`, `nyt-graph`.

Tìm kiếm: chỉ truy vấn bằng tiếng Anh. Tầng mặc định xếp hạng theo từ chung; `--on-device` xếp hạng theo nghĩa sau một lần tải ~33 MB có sự đồng ý.

### 6.7 Design system, bảng màu, typography

| Catalogue | Số lượng | Đường dẫn | Tên |
| --- | --- | --- | --- |
| Preset frame | 13 | `SK/hyperframes-creative/frame-presets/<name>/FRAME.md` cộng `frame-showcase.html`, `caption-skin.html` | `biennale-yellow`, `blockframe`, `blue-professional`, `bold-poster`, `broadside`, `capsule`, `cartesian`, `cobalt-grid`, `code-editorial`, `coral`, `creative-mode`, `daisy-days`, `editorial-forest` |
| Phong cách hình ảnh | 8 | `SK/hyperframes-creative/references/visual-styles.md` | Swiss Pulse, Velvet Standard, Deconstructed, Maximalist Type, Data Drift, Soft Signal, Folk Frequency, Shadow Cut |
| Bảng màu | 9 file, mỗi file 8 dòng | `SK/hyperframes-creative/palettes/*.md` | `bold-energetic`, `clean-corporate`, `dark-premium`, `jewel-rich`, `monochrome`, `nature-earth`, `neon-electric`, `pastel-soft`, `warm-editorial` |
| Font đi kèm | 18 họ font | `SK/hyperframes-creative/references/typography.md` | Inter, Roboto, Open Sans, Lato, Nunito, Montserrat, Poppins, Outfit, Oswald, League Gothic, Archivo Black, Playfair Display, EB Garamond, Space Mono, IBM Plex Mono, JetBrains Mono, Source Code Pro, Noto Sans JP |
| Hướng dẫn khác | | `references/house-style.md`, `video-composition.md`, `motion-principles.md`, `beat-direction.md`, `narration.md`, `story-spine.md`, `data-in-motion.md`, `design-picker.md` | |

Mọi preset frame đều ghi "Motion out of scope" (motion nằm ngoài phạm vi) và mô tả 1920×1080 là chính, kèm 9:16 và 1:1.

Dữ kiện typography: cỡ chữ video là body ≥ 20 px, headline ≥ 60 px khi toàn màn hình; trong feed body ≥ 32 px, headline ≥ 90 px. Một danh sách "Banned" gồm 19 font bị lạm dụng trùng một phần với bộ đi kèm. Đi kèm và không bị cấm: Montserrat, Oswald, League Gothic, Archivo Black, Space Mono, IBM Plex Mono, JetBrains Mono, Source Code Pro, Noto Sans JP. **Không tìm thấy tuyên bố nào về hỗ trợ tiếng Việt** cho bất kỳ họ font đi kèm nào.

Lời dẫn: "2.5 words per second" (2.5 từ mỗi giây); 60 s ≈ 150 từ.

### 6.8 Kiểu phụ đề

File: `SK/media-use/audio/references/captions/authoring.md`, `motion.md`. 15 component phụ đề trong registry, tag `caption-style`:

| Component | Hợp nhất với |
| --- | --- |
| `caption-highlight` | Highlight kiểu TikTok |
| `caption-pill-karaoke` | Viên thuốc karaoke, video lời bài hát |
| `caption-editorial-emphasis` | Tài liệu, kể chuyện |
| `caption-glitch-rgb` | Công nghệ, gaming |
| `caption-kinetic-slam` | Đập toàn màn hình |
| `caption-neon-glow` | Neon |
| `caption-neon-accent` | Neon nhiều màu |
| `caption-clip-wipe` | Hé lộ bằng wipe |
| `caption-gradient-fill` | Tô gradient |
| `caption-matrix-decode` | Giải mã kiểu khoa học viễn tưởng |
| `caption-emoji-pop` | Mạng xã hội, thân mật |
| `caption-parallax-layers` | Chiều sâu |
| `caption-particle-burst` | Ăn mừng |
| `caption-texture` | Texture dung nham |
| `caption-weight-shift` | Thiên về typography |

Liên quan: `caption-blend-difference`. Bảng giọng điệu: Hype, Corporate, Tutorial, Storytelling, Social. Gom từ theo nhóm 2–3, 3–5, 4–6 từ tuỳ năng lượng. Highlight karaoke là mức nền ở mọi mức năng lượng.

### 6.9 Tính năng âm thanh

| Tính năng | Cách làm | Đường dẫn |
| --- | --- | --- |
| Dò beat cho Studio | `npx hyperframes beats` ghi `beats/<audio>.json`; cần `<audio data-timeline-role="music">` | `SK/hyperframes-cli/references/beats.md` |
| Bản đồ beat và năng lượng cho một phim | `/music-to-video` → `scripts/analyze-beatgrid.py` → `audiomap.json`. **Chưa cài** | `SK/hyperframes/references/capability-menu.md` |
| Motion phản ứng theo âm thanh | Trích trước các dải tần bằng `extract-audio-data.py --fps 30 --bands 16`, lấy mẫu mỗi frame bằng `tl.call()` | `SK/hyperframes-creative/references/audio-reactive.md`, `scripts/extract-audio-data.py` |
| TTS | HeyGen Starfish (mốc thời gian từng từ) → ElevenLabs → Kokoro-82M cục bộ. `hyperframes tts` chỉ có Kokoro | `SK/media-use/audio/references/tts.md` |
| Chép lời | Mặc định Parakeet, dự phòng whisper.cpp; luôn truyền `--model` | `SK/media-use/audio/references/transcribe.md` |
| BGM | Lấy từ catalogue HeyGen; dự phòng Lyria rồi MusicGen | `SK/media-use/audio/references/bgm.md` |
| SFX | Lấy từ HeyGen, hoặc thư viện đi kèm | `SK/media-use/audio/references/sfx.md`, `audio/assets/sfx/manifest.json` |
| Một lượt xử lý âm thanh | `audio.mjs --request audio_request.json` → `audio_meta.json` | `SK/media-use/references/audio.md` |
| Mix | `data-fx-chain`, `data-automation`, `data-fx-carve`, bus `<hf-audio-group>` | `SK/hyperframes-audio/SKILL.md`, `references/attributes.md` |
| Hiệu ứng | gain, highpass, lowpass, peaking, lowshelf, highshelf, compressor, limiter, gate, saturate, bitcrush, delay, reverb, chorus, phaser | `references/fx-registry.md` |
| Preset | Giọng: `voice-clean`, `voice-broadcast`, `voice-warm`. Sửa lỗi: `rumble-cut`, `room-gate`, `boom-tame`, `harsh-tame`. Tính cách: `telephone`, `radio-am`, `megaphone`, `lofi-tape`, `pa-system`, `intercom`, `doofus-worble`. Không gian: `room-tight`, `room-natural`, `hall`, `slap-echo`, `dub-throw` | `references/presets.md` |
| Carve cho voiceover | `node <SKILL_DIR>/scripts/carve.mjs --comp index.html`, cường độ mặc định 0.8; "required whenever music plays under a voice" (bắt buộc mỗi khi nhạc chạy dưới giọng nói) | `SK/hyperframes-audio/SKILL.md` |
| Khớp độ lớn | `npx hyperframes normalize-audio` | `references/diagnosis.md` |

SFX đi kèm, 19 key: chime, click-soft, click, error, glitch-1, glitch-2, glitch-3, impact-bass-1, impact-bass-2, key-press, notification, ping, pop, riser, sparkle, typing, whoosh-cinematic, whoosh-short, whoosh.
Mâu thuẫn: `SK/media-use/SKILL.md` nói "19-file library" (thư viện 19 file), `sfx.md` nói "21-file library" (thư viện 21 file). Thư mục chứa 19 mp3 cộng `manifest.json` và `CREDITS.md`.

Giới hạn được nêu: "HyperFrames does not provide automatic waveform sync or drift correction." (HyperFrames không cung cấp đồng bộ waveform tự động hay hiệu chỉnh độ trôi.) Dữ liệu âm thanh được trích trước: "no Web Audio API, no runtime analysis" (không Web Audio API, không phân tích lúc chạy). Tham số của `compressor`, `limiter`, `gate`, `bitcrush` không thể automation.

---

## 7. Camera và keyframe

Nguồn: `SK/hyperframes-keyframes/SKILL.md`, `references/keyframe-patterns.md`, `SK/hyperframes-core/references/creator-editing-recipes.md`, các quy tắc camera trong `SK/hyperframes-animation/rules/`.

| Chuyển động | Cơ chế | Giới hạn được nêu |
| --- | --- | --- |
| Punch-in / punch-out | Keyframe `scale` cùng `x`/`y` trên một wrapper không định thời bên trong clip: `tl.to("#clip .inner", { scale: 1.35, xPercent: -8, duration: 0.18 }, 1)` | Nhắm vào wrapper bên trong, không bao giờ nhắm vào clip có định thời |
| Zoom hoặc reframe nhiều trạng thái | Giữ một wrapper sống, một thang tư thế với easing riêng từng đoạn | |
| Ken Burns / pan | `tl.fromTo("#clip .inner", { scale: 1.05, xPercent: 0 }, { scale: 1.2, xPercent: -12, duration: 4, ease: "none" }, 0)` | "authored geometry, not automatic face tracking" (hình học do người soạn đặt, không phải bám khuôn mặt tự động) |
| Reframe bằng crop / mask | Nội suy `clip-path` trên wrapper bên trong | Không phải trim theo thời gian |
| Zoom tới mục tiêu lệch tâm | `coordinate-target-zoom`: lớp ngoài scale, lớp trong tịnh tiến, `T = -offset` | Đo một lần sau `fonts.ready`, không bao giờ đo mỗi frame |
| Camera ảo | `viewport-change`: một `.world`, trạng thái `cam {scale,x,y}`, `T = -offset × S` | Hai công thức không thay thế cho nhau được |
| Camera theo pha có trôi | `multi-phase-camera`: scale theo pha cộng trôi hình sin, tỉ lệ tần số ≈ 1.3 | Nền đặt trên `.scene`, không đặt trên camera |
| Chiều sâu 3D, DOM | `3d-camera-flight`: sân khấu `perspective` tĩnh, thế giới `preserve-3d`, trạng thái `cam {x,y,z,rx,ry}`, một hàm ghi duy nhất `applyCamera()`, thứ tự `translate3d` rồi `rotateX` rồi `rotateY` | "A `filter` on a `preserve-3d` element flattens it" (một `filter` trên phần tử `preserve-3d` làm nó bị dẹt); tư thế đặt bằng mắt, "don't hand-derive 3D projections" (đừng tự tay tính phép chiếu 3D) |
| Rack focus | `depth-of-field-blur`: biến `--dof` trên các lớp không lấy nét | |
| Chiều sâu 3D, canvas | Camera, target, transform đối tượng Three.js từ một proxy GSAP hoặc `hf-seek` | Kiểm bằng `keyframes --ghost` |
| Whip pan | Block shader registry `whip-pan`; hoặc `nudge-curve` cộng `motion-blur-streak` trên một cửa sổ | Tìm trong registry trước khi tự tay soạn |
| Match cut | Skill animation phụ trách việc chuyển giao, registry cung cấp primitive | "There is no automatic matching-frame discovery" (không có tự động tìm frame khớp) |
| Speed ramp | Làn `rate` trong `data-automation`, nội suy log | |
| Freeze | Tư thế hình ảnh hoặc frame cuối có thể giữ lại | "Arbitrary mid-source freeze is not supported" (không hỗ trợ freeze tuỳ ý giữa nguồn) |

Luật ease cho camera (`blueprints/camera-journey.md`): `power4.out` cho các cú lao và hạ cánh, `power2.inOut` cho việc đổi vị trí; easing lò xo trên camera "feels wrong" (cảm giác sai).

Công cụ kiểm chứng: `keyframes --shot` (onion skin), `--layout strip`, `--ghost` (canvas và WebGL), `--angle front|iso|top|side|rear-iso`, `snapshot --at`, `snapshot --angle`.

Motion blur (`references/motion-blur.md`): hai đường. Component registry `motion-blur`, thuộc tính `data-hf-motion-blur`, mặc định `shutterAngle` 720, `samplesPerFrame` 16, tốn N+1 bản sao cây con và N+1 lần seek mỗi frame; "Three marked elements is fine. Thirty is a different render." (Ba phần tử được đánh dấu thì ổn. Ba mươi là một lần render khác hẳn.) Tuỳ chọn render `motionBlur` của engine làm nhoè cả frame, chỉ cho bản render cuối.

---

## 8. Studio

Nguồn: `SK/hyperframes-studio/SKILL.md`, `SK/hyperframes-cli/references/preview-render.md`.

Nó là gì: `npx hyperframes preview` khởi động một server cục bộ, cổng mặc định 3002, và mở Studio trong trình duyệt: "the full timeline editor, where the user can play the video and edit anything by hand before rendering. This is the review surface, not just a viewer." (trình chỉnh timeline đầy đủ, nơi người dùng có thể phát video và tự tay sửa bất cứ thứ gì trước khi render. Đây là bề mặt duyệt, không chỉ là trình xem.) Tự hot-reload khi file thay đổi.

Một project được preview thế nào:
- URL để đưa cho người xem: `http://localhost:<port>/#project/<project-name>`. Không có phần hash, Studio nạp lên mà không có project.
- `preview --background` giữ nó sống; dừng bằng `npx hyperframes preview --stop`; có `--list`, `--kill-all`.
- `play`: player gọn nhẹ trên cổng 3003 qua web component nhúng được `<hyperframes-player>`, `http://localhost:<port>` trơn. `playback-rate` của player bị kẹp trong `[0.1, 5]`.
- `present`: bộ slide với đồng bộ người trình bày và khán giả, cổng 3004.
- `publish`: URL được host "renders in the browser" (render trong trình duyệt).

Người xem thấy gì, theo những gì file nói:
- Mỗi phần tử cấp cao nhất một hàng timeline; các loại track `video`, `graphics`, `captions`, `audio`.
- Icon con mắt bật tắt `data-hidden`; fader ghi `data-volume`; rack hiệu ứng có module Voiceover carve; làn automation; nút bật tắt lề an toàn khi preview; phần tử được chọn mà agent đọc được qua `preview --context --json`.
- Studio dùng Tailwind v3; `init --tailwind` scaffold Tailwind v4.

Quy ước timeline:
1. Mỗi cảnh là một sub-composition; root chỉ giữ các host có định thời, media, audio.
2. Một track phụ đề, một host được đánh dấu `data-track-kind="captions"`.
3. Mỗi track một loại phần tử.
4. Không có phần tử guide bên trong composition.

Vùng an toàn:

| Hộp | Tỉ lệ so với frame | Lề mỗi cạnh |
| --- | --- | --- |
| Action-safe | 90% | 5% |
| Title-safe | 80% | 10% |

Cả hai khung, ngang và dọc, dùng cùng hai hộp này.

Mâu thuẫn về chỗ phụ đề và nội dung được phép nằm:

| File | Quy tắc |
| --- | --- |
| `SK/hyperframes-studio/SKILL.md` | Phụ đề và nội dung chính nằm trong title-safe, 80% |
| `SK/hyperframes/references/frame-worker-core.md` | Viên phụ đề chiếm ~17% phía dưới; nội dung nằm trên `0.83 × height` |
| Mặc định của `check --caption-zone` | dải từ `y0=.82` |
| `SK/media-use/audio/references/captions/authoring.md` | Ngang: 80–120 px phía dưới; dọc: ~600–700 px tính từ đáy |

Không cái nào trong số này là vùng an toàn UI của nền tảng cho TikTok, Reels hay Shorts.

---

## 9. Độ phù hợp và giới hạn

### 9.1 HyperFrames mạnh ở đâu

| Loại video | Bằng chứng [stated] |
| --- | --- |
| Video giải thích có lời dẫn và phụ đề | Pipeline `faceless-explainer`: TTS có thời gian từng từ → đồng bộ thời lượng → frame → phụ đề → transition. Điểm ngọt 30–90 s, trần khoảng 3 phút |
| Promo từ một website | `capture` cộng route `product-launch-video`; 22 blueprint đúc kết từ các clip ra mắt |
| Slide và bộ trình chiếu | Route `slideshow`, lệnh `present` |
| Đồ hoạ DOM và SVG | 48 quy tắc GSAP; `check` kiểm layout, chồng lấn, độ tương phản trên các hộp DOM |
| Tác phẩm dẫn dắt bởi voice-over | `SCRIPT.md`, carve, các lần hé lộ theo nhịp `voiceover` |
| Phụ đề trên footage có sẵn, overlay | Route `embedded-captions`, `talking-head-recut` |
| Motion graphics ngắn, overlay có alpha | `motion-graphics`; `render --format webm\|mov` có trong suốt |
| Loạt video theo dữ liệu | `render --batch rows.json`, biến composition |
| Demo UI có con trỏ | Quy tắc `cursor-click-ripple`, `cursor-drag`, `multi-cursor-choreography`, `control-target-sync`; blueprint `cursor-ui-demo`, `panel-edit-live-sync`, `prompt-type-submit-generate`, `agent-progress-theater` |
| Đi qua code | Heading registry "Code Animations (9)" và "Code snippets (24)" |

Tuyên bố chung trong các file: "the framework renders anything a browser can run" (framework render được mọi thứ trình duyệt chạy được) (`transitions/catalog.md`).

### 9.2 Các giới hạn file nêu ra

| Chủ đề | Phát biểu | File |
| --- | --- | --- |
| Hạt DOM | "cap ~40 — per-frame style writes; past that, seek perf and register degrade" (giới hạn ~40 — ghi style mỗi frame; quá mức đó, hiệu năng seek và độ khớp suy giảm) | `rules/particle-burst.md` |
| HTML-in-canvas | "a separate, heavier capability" (một năng lực riêng, nặng hơn); "Use it for 1–3 hero beats per video, not every beat" (dùng cho 1–3 beat chính mỗi video, không phải mọi beat) | `techniques.md` |
| Bàn tay 3D cộng bloom | "One genuine out-of-scope special remains ... needs R3F/Three.js + WebGL — a heavier capability than the rule library" (còn một trường hợp đặc biệt thật sự nằm ngoài phạm vi ... cần R3F/Three.js + WebGL — năng lực nặng hơn thư viện quy tắc) | `blueprints-index.md` |
| Three.js | Không suy ra thời lượng. Tránh "Post-processing passes that depend on previous frame history unless you can reconstruct state from time" (các pass hậu kỳ phụ thuộc lịch sử frame trước, trừ khi bạn dựng lại được trạng thái từ thời gian). Không dùng `requestAnimationFrame` làm nguồn chân lý. Ghim kích thước renderer và pixel ratio | `adapters/three.md` |
| WebGPU với chụp DOM | Headless shell đi kèm không hỗ trợ WebGPU cùng lúc với `drawElementImage` | `adapters/typegpu.md` |
| Video làm texture GPU | "headless Chrome may fail `copyExternalImageToTexture` for video elements" (headless Chrome có thể thất bại `copyExternalImageToTexture` với phần tử video) | `adapters/typegpu.md` |
| Transition shader | Chụp DOM qua html2canvas; sáu hạn chế CSS (không `transparent` trong gradient, không `var()`, v.v.); root composition bị ép trong suốt trên đường này | `transitions/overview.md`, `hyperframes-core/SKILL.md` |
| GL phần mềm | "Heavy compositions can stall on software GL" (composition nặng có thể bị treo trên GL phần mềm) | `preview-render.md` |
| Chi phí render | Mỗi worker là một Chrome ~256 MB; "60fps doubles render time" (60fps làm gấp đôi thời gian render) | `preview-render.md` |
| Motion blur | N+1 bản sao và N+1 lần seek cho mỗi mục tiêu mỗi frame | `references/motion-blur.md` |
| Gradient | Gradient tuyến tính toàn màn hình trên nền tối "band visibly under H.264 compression" (bị sọc dải thấy rõ khi nén H.264) | `video-composition.md` |
| `check` | "is not a visual gate. It passes compositions that render nothing" (không phải cổng kiểm hình ảnh. Nó cho qua cả composition không render ra gì) | `component-quality-bar.md` |
| Chẩn đoán canvas | "Use `--ghost` because marker boxes cannot see internal canvas motion" (dùng `--ghost` vì hộp marker không thấy được chuyển động bên trong canvas) | `hyperframes-keyframes/SKILL.md` |
| Đồng bộ âm thanh | Không có đồng bộ waveform tự động hay hiệu chỉnh độ trôi | `hyperframes-audio/SKILL.md` |
| Mix âm thanh | "Almost no static gate covers the mix" (hầu như không có cổng kiểm tĩnh nào bao được phần mix); xác minh bằng cách render và nghe | như trên |
| Look phản ứng theo âm thanh | "Never add: equalizer bars, spectrum analyzers, waveform displays ... generic particle systems ... abstract pulsing orbs" (không bao giờ thêm: thanh equalizer, máy phân tích phổ, hiển thị waveform ... hệ hạt chung chung ... quả cầu trừu tượng nhấp nháy) | `audio-reactive.md` |
| Trang live được chụp | "No iframes for captured content" (không dùng iframe cho nội dung chụp) | `motion-principles.md` |
| Registry offline | `add` lần nào cũng cần mạng | `hyperframes-registry/SKILL.md` |
| Độ dài | Workflow kể chuyện mạnh nhất ở 30–90 s; dài hơn thì sang `general-video` | `hyperframes/SKILL.md` |
| Agent macOS trong sandbox | Chrome có thể chết lúc khởi động trong sandbox seatbelt; "Do not build a substitute rasterizer" (đừng dựng một rasterizer thay thế) | `doctor-browser.md` |

### 9.3 Khi nào một engine WebGL2 viết tay là công cụ tốt hơn

Mỗi dòng: những gì file cung cấp, rồi kết luận của tôi.

| Nhu cầu | Những gì file cung cấp [stated] | Kết luận [inferred] |
| --- | --- | --- |
| Shader toàn frame làm hình ảnh chính | Kỹ thuật 13 (một quad toàn màn hình điều khiển bởi proxy GSAP); adapter `three` và `typegpu` chỉ chuyển tiếp thời gian: "The adapter does not own your scene" (adapter không sở hữu scene của bạn) | Làm được, nhưng HyperFrames chỉ thêm đồng hồ seek và một encoder, ngoài ra chẳng mấy. Quy tắc, blueprint, preset frame, kiểm tra layout và tương phản của `check` đều dựa trên DOM và không nhìn vào trong canvas. Engine viết tay là công cụ tốt hơn khi shader chính là bộ phim |
| Hàng chục nghìn đường hoặc hạt instanced | Giới hạn DOM ~40. `keyframe-patterns.md` có một dòng "Instanced system — Three InstancedMesh". Một block `code-particle-assemble` ("Thousands of GPU points" — hàng nghìn điểm GPU) | Không quy tắc, blueprint hay công thức nào dạy điều này. Engine viết tay |
| Camera bay xuyên một thế giới 3D | `3d-camera-flight` là CSS 3D trên card và lưới DOM, tư thế chỉnh bằng mắt. 3D thật chỉ qua adapter Three.js | Tốt cho card UI có chiều sâu. Với một thế giới được dựng mô hình và camera di chuyển, dùng engine viết tay hoặc Three.js thuần |
| Render theo hàm thuần mỗi frame | `hf-seek` truyền `time`; `renderAt(time)` là mẫu Three.js được tài liệu hoá; quy tắc tất định khớp mô hình này | Mô hình phù hợp. HyperFrames có thể chứa một canvas như vậy làm một lớp |
| Đồng bộ với lưới beat đã đo | `kinetic-beat-slam` dùng lưới `PULSE` đều ("keep spacing even" — giữ khoảng cách đều). `beats` ghi một file Studio mà định dạng không được mô tả. `audiomap.json` thuộc một skill chưa cài | Không tìm thấy gì về độ trôi tempo hay lưới bám theo tiếng kick. Với track bị trôi, giữ lưới đo riêng của project; engine viết tay |
| Chuỗi hậu kỳ: bloom, grain | Bloom chỉ có dạng `UnrealBloomPass` của Three.js bên trong HTML-in-canvas. Grain dạng component DOM `grain-overlay`, hoặc `media-treatment` trên một `<img>`/`<video>` đơn lẻ. Các pass dựa trên lịch sử bị khuyến cáo không dùng | Không có chuỗi hậu kỳ hạng nhất trên toàn frame. Engine viết tay |
| Look music visualizer | Văn bản route liệt kê "music visualizer" là một output, trong khi `audio-reactive.md` cấm look phổ và waveform | Hai file mâu thuẫn nhau. Các quy tắc thẩm mỹ lái tránh xa loại phim này |

### 9.4 Dùng kết hợp [inferred]

- Một canvas WebGL có thể nằm làm một lớp dưới tiêu đề và phụ đề DOM, điều khiển bởi `hf-seek`. Cả hai adapter được viết cho việc đó.
- Những phần hữu ích để mượn mà không cần áp dụng cả pipeline: component phụ đề và quy tắc gom nhóm, bộ từ vựng năm transition của injector, voiceover carve, `snapshot --at` cho từng ảnh tĩnh, bộ SFX đi kèm, preset frame làm tham chiếu look.

### 9.5 Đối chiếu với quy tắc của chủ dự án [inferred]

Các quy tắc là những quy tắc mà các phim tham chiếu đã được làm theo; quy tắc 10 của `SKILL.md` chứa các quy tắc chung.

| Quy tắc dự án | Mặc định của HyperFrames | Hệ quả |
| --- | --- | --- |
| Không xuất video | Mọi workflow kể chuyện kết thúc bằng `render` → MP4; văn bản cổng kiểm nói `renders/video.mp4` phải tồn tại | Dừng trước bước Deliver. Một composition đã kiểm cộng preview là trạng thái cuối |
| Giao HTML phát được, một trang xem | Phát lại cần `preview`, `play`, hoặc `publish`. Không file nào nói `index.html` phát được từ `file://` | Bản thân một project HyperFrames không đáp ứng sản phẩm bàn giao là trang xem. Xem Câu hỏi mở |
| Chỉ ảnh tĩnh, mỗi lúc một tiến trình | `snapshot` và `check` mỗi cái khởi động một headless Chrome; `render --workers auto` khởi động nhiều cái | `snapshot --at` và `check` phù hợp nếu chạy từng cái một. Frame worker không được chạy CLI, điều mà `frame-worker-core.md` vốn đã cấm |
| Không để server chạy lại | `preview --background` được thiết kế để tồn tại lâu | Phải gọi `npx hyperframes preview --stop` |
| Không chạy lấy mẫu motion-blur | Component `motion-blur` seek N+1 lần mỗi frame trong trang; tuỳ chọn engine lấy mẫu sub-frame | Cả hai đều thuộc phạm vi quy tắc này |
| Cảnh do sub-agent Opus dựng, lead duyệt | Mỗi frame một worker, gói việc trong `.hyperframes/frame-packets/`, tờ phác thảo được duyệt trước | Tương thích về hình thức |
| Xác nhận storyboard trước khi dựng | Vòng duyệt `storyboard: yes` với `storyboard.html` | Tương thích |
| Không tạo nội dung trả phí khi chưa hỏi | Quy tắc chi phí: agent xác nhận trước một lệnh gọi trả phí do agent khởi xướng | Tương thích; dù vậy, việc đăng nhập HeyGen vẫn bị thúc ở bước Setup |
| Nhạc nền không lời, không vocal, trên 130 BPM | Bảng prompt BGM trong `SK/media-use/audio/references/bgm.md` có tempo gốc 92 đến 115 BPM, cộng 10 cho một archetype; hướng dẫn `--bpm` của Lyria dừng ở 130 | Nguồn nhạc ở đây không khớp với brief |

### 9.6 Các quy tắc mâu thuẫn nhau trong cùng họ

| Chủ đề | File A | File B |
| --- | --- | --- |
| Dựng timeline trong code async | `hyperframes-core/references/determinism-rules.md`: "Building inside an async callback is supported" (dựng bên trong callback async được hỗ trợ) | `hyperframes-animation/SKILL.md`: "no timeline construction inside `async` / `setTimeout` / `Promise`" (không dựng timeline bên trong `async` / `setTimeout` / `Promise`); `hyperframes-keyframes/SKILL.md`: không bao giờ dùng "async-created timelines" (timeline tạo bằng async) |
| Thuộc tính animate được | core: "no fixed allowlist" (không có allowlist cố định); `width`, `height` là "legitimate targets" (mục tiêu hợp lệ) | `rules-index.md`: "`width`/`height`/`top`/`left` tweens are forbidden" (cấm tween `width`/`height`/`top`/`left`); SKILL animation trích dẫn "Core's allowlist" (allowlist của Core) |
| `window.__timelines = window.__timelines \|\| {}` | core: không cần | `transitions/catalog.md` và `hyperframes-keyframes/SKILL.md` vẫn viết nó |
| Font | core: một họ font có tên cần `@font-face` trong file trỏ tới một file đi kèm | `transitions/catalog.md`: "Just write the `font-family` you want" (cứ viết `font-family` bạn muốn); `typography.md`: 18 họ đi kèm không cần gì, các họ khác được tải từ Google lúc build |
| Animation thoát | `transitions/overview.md`: "Exit animations are BANNED except on the final scene" (animation thoát bị CẤM trừ ở cảnh cuối) | `techniques.md` #10 và `beat-direction.md` dạy một tween thoát tăng tốc trong composition đang ra |
| `data-track-index` | core: chỉ để hiển thị | `hyperframes-registry/SKILL.md`: "layer ordering (higher = in front)" (thứ tự lớp, cao hơn = ở trước) |
| `class="clip"` trên cảnh | core: thêm nó vào các clip hình ảnh có định thời | `transitions/catalog.md`: "No `class=\"clip\"` on scene divs in standalone compositions" (không đặt `class=\"clip\"` trên div cảnh trong composition độc lập) |
| Dạng tween xuất hiện | `transitions/overview.md`: dùng `fromTo`, không dùng `from` | Khung sườn `minimal-composition.md` dùng `tl.from` |

---

## 10. Câu hỏi mở

1. Kích thước registry thật. Các tuyên bố dao động từ "50+" đến "~400". `npx hyperframes catalog --json` sẽ giải quyết được; chưa chạy.
2. Liệu một composition có phát được như HTML thuần mà không cần `preview` hay `play` không, và `<hyperframes-player>` được nhúng vào một trang của riêng mình thế nào. Không file đã cài nào trả lời. Điều này quyết định HyperFrames có đáp ứng được sản phẩm bàn giao là trang xem hay không.
3. Nội dung của mười skill workflow chưa cài, trên hết là `music-to-video`: `analyze-beatgrid.py`, cấu trúc `audiomap.json`, và mọi cách xử lý độ trôi tempo.
4. Định dạng và phương pháp của `beats/<audio>.json` từ `hyperframes beats`. Không được mô tả.
5. Tuỳ chọn render `motionBlur` của engine được bật thế nào. Không có cờ đó trong `render --help`.
6. Ma trận hỗ trợ hệ điều hành. Không được nêu ở đâu.
7. Trạng thái telemetry thật như CLI báo cáo. Chưa chạy `telemetry status`; file config nói đang bật.
8. `history` và các lệnh con chỉnh sửa của `timeline`: không skill đã cài nào tài liệu hoá chúng.
9. Độ phủ glyph tiếng Việt của 18 font đi kèm. Không được nêu.
10. Giá cloud render mỗi credit. Không được nêu.
11. Catalogue "identity" (nhận diện) phụ đề của `embedded-captions`. Chưa cài.
