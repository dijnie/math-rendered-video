# Môi trường

Máy phải có những gì trước khi có thể dựng một phim trên đó, cách kiểm tra, cách cài những gì còn thiếu trên macOS, Windows và Linux, và những khác biệt giữa các hệ thống đó có thể làm hỏng một phim.

Nạp file này khi: skill khởi động trên một máy lần đầu, một project được chép sang máy khác, một công cụ không khởi động được, hoặc một shot trông đúng trong capture nhưng sai trên máy của owner.

Ký hiệu dùng trong file này: **đã xác minh** (verified) nghĩa là đọc từ nguồn chính thức trong lúc research ngày 2026-09-28. **Chưa xác minh** (not verified) nghĩa là thường được nhắc tới nhưng chưa được xác nhận khi đó. **Đã thử** (tried) nghĩa là đã chạy trên một máy: cho đến nay chỉ có macOS trên Apple silicon.

## 1. Kiểm tra trước

```sh
node scripts/check-environment.mjs                                  # the engine route
node scripts/check-environment.mjs --route hyperframes
node scripts/check-environment.mjs --route both --with audio,video,webkit,blender
node scripts/check-environment.mjs --with audio --venv <film>/analysis/python-env
node scripts/check-environment.mjs --json
```

`scripts/` ở đây là thư mục riêng của skill. `<film>` là thư mục của phim, một bản sao của `assets/starter/`; môi trường phân tích nằm bên trong nó.

Khi máy không có cả Node.js lẫn Bun, khởi động nó qua `scripts/check-environment.sh` (macOS, Linux) hoặc `scripts/check-environment.ps1` (Windows). Chúng cho biết cách cài Node.js rồi dừng.

| Trình kiểm tra | |
|---|---|
| Không cài gì cả | Nó in ra lệnh. Owner, hoặc agent khi được owner cho phép, chạy lệnh đó |
| Báo cáo | Hệ thống, các trình quản lý gói tìm thấy, từng công cụ với phiên bản và việc nó có bắt buộc hay không, có tạo được link hay không, graphics backend dùng cho capture, và lời khuyên |
| Exit code | 0 khi mọi thứ bắt buộc đều có; 1 khi có thứ bắt buộc bị thiếu hoặc quá cũ; 2 khi sai tham số |
| Đã thử trên | macOS 26 trên Apple silicon, dưới Node.js 24 và dưới Bun 1.3. Các nhánh Windows và Linux được viết từ tài liệu và chưa được chạy |

Cài đặt là một thay đổi trên máy của owner. Cho thấy những gì còn thiếu và các lệnh, và hỏi trước khi chạy chúng.

## 2. Cần gì cho việc gì

| Công cụ | Route engine | Route HyperFrames | Thêm: phân tích audio | Thêm: file video, clip | Thêm: capture bằng WebKit |
|---|---|---|---|---|---|
| Node.js | 20 trở lên. 22 trở lên nếu dùng Playwright để capture | 22 trở lên | | | |
| Bun | 1.3 trở lên (trình quản lý gói và chạy script của starter) | | | | |
| git | Khuyến nghị. Không có nó thì một hình bị mất không lấy lại được | Khuyến nghị | | | |
| Python 3 | 3.9 trở lên, cho trình sinh storyboard | | 3.12 với môi trường riêng | | |
| Các gói Python | | | librosa, soundfile, numpy, scipy, matplotlib (được pin trong `analysis/requirements.txt` của starter) | | |
| Một trình duyệt họ Chromium | Bắt buộc để capture: Chrome, Edge, hoặc Chromium của Playwright | Trình duyệt được pin riêng của nó | | | |
| WebKit của Playwright | | | | | Bắt buộc |
| ffmpeg, ffprobe | | Bắt buộc | | Bắt buộc, với encoder `libx264`: để export, để encode lần hai theo một kích thước, để kiểm tra một file đã export, và để trích xuất các frame của một clip vào `media/` | |
| Docker | | Chỉ cho render trong container | | | |
| Blender | Chỉ khi model được làm ở đó | | | | |

Trình duyệt riêng của owner không có trong bảng này nhưng lại quan trọng nhất: xem mục 6.

Bản build một file (`bun run single` trong thư mục phim) không cần gì ngoài route engine: Vite, thứ starter đã có, build script, và một script của starter đóng gói phần còn lại. File nó ghi ra mở được trong trình duyệt mà không cần server. Mỗi lần chạy ffmpeg trên máy của owner (một lần export, encode lần hai, kiểm tra một file đã export, trích xuất một clip) là một lần chạy nặng cần lời của owner; `engine-architecture.md`, mục 4 và 8, có các lệnh.

## 3. Cài đặt

Một lệnh cho mỗi công cụ và hệ thống, cách chuẩn nhất trước.

### Node.js

| Hệ thống | Lệnh | Trạng thái |
|---|---|---|
| macOS | `brew install node` | đã xác minh |
| Windows | `winget install --id OpenJS.NodeJS.LTS -e` | đã xác minh |
| Debian, Ubuntu | `curl -fsSL https://deb.nodesource.com/setup_lts.x -o nodesource_setup.sh && sudo -E bash nodesource_setup.sh && sudo apt install -y nodejs` | đã xác minh. Gói của bản phân phối quá cũ: Ubuntu 24.04 có bản 18 |
| Fedora | `sudo dnf install nodejs` | chưa xác minh |
| Arch | `sudo pacman -S nodejs npm` | chưa xác minh |

### Bun

| Hệ thống | Lệnh | Trạng thái |
|---|---|---|
| macOS, Linux | `curl -fsSL https://bun.com/install \| bash` | đã xác minh. Linux cần `unzip` |
| Windows | `powershell -c "irm bun.sh/install.ps1 \| iex"` | đã xác minh |

### git

| Hệ thống | Lệnh | Trạng thái |
|---|---|---|
| macOS | `brew install git` | chưa xác minh; hệ thống tự đề xuất bản của nó ở lần dùng đầu tiên |
| Windows | `winget install --id Git.Git -e --source winget` | đã xác minh |
| Linux | `sudo apt install git`, `sudo dnf install git`, `sudo pacman -S git` | chưa xác minh |

### Python

| Hệ thống | Lệnh | Trạng thái |
|---|---|---|
| macOS | `brew install python@3.12` | chưa xác minh |
| Windows | `winget install --id Python.Python.3.12` | đã xác minh |
| Ubuntu 24.04 | `sudo apt install python3.12 python3.12-venv python3-pip` | bản phát hành đi kèm 3.12 |
| Debian 12 | Đi kèm 3.11. Dùng `uv python install 3.12` | đã xác minh |
| Fedora | `sudo dnf install python3.12` | chưa xác minh |
| Arch | Python của hệ thống luôn là bản mới nhất. Dùng `uv python install 3.12` | đã xác minh |
| Bất kỳ | `uv python install 3.12`, sau khi cài uv: `curl -LsSf https://astral.sh/uv/install.sh \| sh`, trên Windows `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | đã xác minh |

Môi trường cho phân tích, khi đã có Python, được tạo bên trong thư mục phim:

```sh
python3.12 -m venv analysis/python-env
analysis/python-env/bin/python -m pip install -r analysis/requirements.txt
```

Trên Windows: `py -3.12 -m venv analysis\python-env`, và trình thông dịch là `analysis\python-env\Scripts\python.exe`. Một môi trường tạo trên máy này không chạy được trên máy khác: hãy tạo lại. Các pin được resolve trên macOS; nếu một pin không có bản build cho hệ thống khác, hãy cài bộ không pin `librosa soundfile numpy scipy matplotlib` thay thế (chưa thử). Trên Windows 11 với Python 3.13, mọi pin đều cài được, vào ngày 2026-09-28.

Các bản build sẵn của `soundfile` cho Windows, macOS và Linux trên x86-64 mang theo thư viện âm thanh của chúng. Chỉ ở nơi không có bản build như vậy phù hợp thì hệ thống mới cần nó: `sudo apt install libsndfile1`.

### Một trình duyệt để capture

| Hệ thống | Lệnh | Trạng thái |
|---|---|---|
| macOS | `brew install --cask google-chrome` | chưa xác minh |
| Windows | `winget install --id Google.Chrome -e` | chưa xác minh |
| Bất kỳ | `npx playwright install chromium` | đã xác minh |

Capture phải chạy trong một trình duyệt vẽ bằng card đồ họa. Trình duyệt headless mặc định của Playwright là một "headless shell" vẽ WebGL bằng phần mềm: quá chậm để đánh giá một phim, và cho kết quả khác. Hãy khởi động trình duyệt đầy đủ: Chrome của hệ thống (`channel: 'chrome'`) hoặc Chromium đầy đủ của Playwright (`channel: 'chromium'`).

### WebKit

`npx playwright install webkit`, trên Linux thêm `--with-deps`. Đã xác minh.

Trên Windows và Linux, WebKit này là một bản build thật của engine nhưng không thay thế được Safari về mặt âm thanh và video. Chính tài liệu của Playwright nói rằng để gần với Safari nhất, hãy chạy WebKit trên một máy Mac.

### ffmpeg

| Hệ thống | Lệnh | `libx264` | Trạng thái |
|---|---|---|---|
| macOS | `brew install ffmpeg` | có | đã xác minh |
| Windows | `winget install --id=Gyan.FFmpeg -e` | có, trong bản build đầy đủ | đã xác minh |
| Ubuntu | `sudo apt install ffmpeg` | có | đã xác minh |
| Debian | `sudo apt install ffmpeg` | chưa xác nhận: kiểm tra bằng `ffmpeg -encoders` | còn bỏ ngỏ |
| Fedora | Gói mặc định không có. Thêm RPM Fusion, rồi `sudo dnf install ffmpeg` | có, từ RPM Fusion | chưa xác minh |
| Arch | `sudo pacman -S ffmpeg` | có | chưa xác minh |

Encoder AAC được tích hợp sẵn trong mọi bản ffmpeg chuẩn. Chỉ `libx264` là đáng kiểm tra, và trình kiểm tra có làm việc đó.

### Blender

`brew install --cask blender`, `winget install --id BlenderFoundation.Blender -e`, hoặc gói của bản phân phối. Trên macOS chương trình không nằm trên path: gọi `/Applications/Blender.app/Contents/MacOS/Blender`. Chạy không có cửa sổ bằng `blender -b file.blend -P script.py`; các tham số được thực thi theo thứ tự đã cho.

## 4. Những gì khác nhau giữa các hệ thống

### Link trong thư mục public

App tham chiếu phục vụ nhạc và dữ liệu cho trang qua các symbolic link trong thư mục public của nó, và chúng bị hỏng khi project được chép đi. Starter không có link: `vite.config.ts` tự phục vụ `audio/` và `data/`. Hãy giữ như vậy. Bảng dưới chỉ quan trọng với một project vẫn link thư mục.

| Hệ thống | Hành vi | Làm gì |
|---|---|---|
| macOS, Linux | Link hoạt động | Không cần gì |
| Windows | Tạo symbolic link cần Developer Mode hoặc một shell chạy với quyền administrator | Bật Developer Mode; hoặc dùng directory junction, không cần cái nào trong hai thứ trên (`mklink /J`, hoặc trong Node.js `fs.symlinkSync(target, path, 'junction')`); hoặc chép các thư mục |
| Ổ đĩa định dạng exFAT hoặc FAT | Link bị mất khi chép | Tạo lại chúng bằng script thiết lập của project |
| git trên Windows | Khi không tạo được link, nó lặng lẽ ghi các file text nhỏ vào chỗ của chúng | Kiểm tra các link là thư mục sau khi clone |

Junction chỉ dùng được cho thư mục và chỉ trên một ổ đĩa. Như vậy là đủ cho một thư mục public.

### Graphics backend

Chrome vẽ WebGL qua một lớp giao tiếp với giao diện đồ họa riêng của hệ thống. Flag `--use-angle` chọn lớp đó.

| Hệ thống | Mặc định | Flag cho capture | Nếu thất bại |
|---|---|---|---|
| macOS | Metal | `--use-angle=metal` | `--use-angle=gl` |
| Windows | Direct3D 11 | `--use-angle=d3d11`, hoặc không có flag | `--use-angle=gl`, `--use-angle=vulkan` |
| Linux có card đồ họa | OpenGL | `--use-angle=gl` | `--use-angle=vulkan` |
| Linux không có card, container | Không có | `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader` | Vẽ bằng phần mềm: đánh giá hình ảnh, không đánh giá tốc độ |
| WSL | Chưa xác lập | Coi như vẽ bằng phần mềm | Đánh giá tốc độ ở phía Windows |

Các giá trị đã được xác minh từ mã nguồn Chromium. `metal` chỉ có trên macOS, `d3d11` chỉ có trên Windows. Một công cụ capture nêu tên một trong hai phải chọn theo hệ thống. Công cụ capture của starter làm vậy: `metal` trên macOS, `d3d11` trên Windows, `gl` trên Linux, và `--angle` ghi đè lựa chọn đó.

Hãy hỏi trình duyệt nó vẽ bằng gì, trước khi tin vào một phép đo: chuỗi unmasked renderer của WebGL nêu tên backend và card. Công cụ capture của starter có một chế độ cho việc này: `bun scripts/render.ts gpu`.

### Một đường chậm trên Windows

Upload một canvas 2D vào một texture sRGB rất chậm trong Chrome trên Windows. Nguyên nhân nằm ở đường Direct3D và là một vấn đề đã biết của trình duyệt. Trên macOS, cùng lần upload đó mất nửa mili giây cho một frame 1080 x 1920 (đã thử).

Cách sửa, trong engine: upload canvas vào một texture RGBA8 thường, rồi chép nó sang texture sRGB bằng một pass nhỏ trên card đồ họa. Phần còn lại của code vẫn nhận một texture sRGB. Starter mang bản sửa này trong `src/engine/gl.ts`. Nó được viết từ mô tả của bản sửa đã làm trên máy Windows của owner, không phải từ code của bản đó, và mới chỉ chạy trên macOS; chưa được so sánh trên Windows. Khi kiểm tra bản sửa đó, hãy so một still của cùng một thời điểm trên cả hai hệ thống: bước chép phải chuyển các giá trị canvas sang linear light, nếu không mọi layer 2D đều ra quá sáng.

### Windows, thêm nữa

| Vấn đề | Sự thật | Làm gì |
|---|---|---|
| Chạy một script cài đặt | Policy mặc định chặn script từ mạng | Cho một process: `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process` |
| `python` mở Store | Windows đi kèm các stub tên `python.exe` mở Store | Settings, "Manage app execution aliases", tắt hai mục Python |
| Python nào | Launcher `py -3.12` chọn trong các phiên bản đã cài | Dùng nó, hoặc đường dẫn đầy đủ tới trình thông dịch của môi trường |
| Đường dẫn dài | Đường dẫn trên 260 ký tự thất bại trừ khi bật long path | Đặt project gần gốc ổ đĩa |
| Ký tự xuống dòng | Một shell script được checkout với ký tự xuống dòng kiểu Windows sẽ lỗi dưới bash | Một mục `.gitattributes` giữ `*.sh` với ký tự xuống dòng kiểu Unix |
| Sau khi cài | Một công cụ mới không có trên path của các terminal đã mở từ trước | Mở một terminal mới |
| Ổ đĩa | Render dài có thể làm đầy ổ hệ thống | Đặt cache trên ổ khác |

### macOS

| Vấn đề | Sự thật |
|---|---|
| Thư mục của Homebrew | `/opt/homebrew` trên Apple silicon, `/usr/local` trên Intel. Hỏi `brew --prefix`; không bao giờ ghi cứng đường dẫn vào script |
| Một chương trình tải về bị chặn | Mở nó một lần qua System Settings, Privacy and Security, "Open Anyway" |

### Linux

`npx playwright install-deps` cài các thư viện và font mà một trình duyệt headless cần. Khi ở sau proxy, phải chỉ rõ proxy cho nó, vì nó bỏ môi trường khi chuyển thành root.

## 5. Chép một project sang máy khác

| Bước | Lý do |
|---|---|
| Bỏ qua các gói đã cài, môi trường Python và đầu ra capture | Chúng được tạo lại, hoặc là đồ nháp. Chúng chiếm phần lớn dung lượng |
| Giữ file secrets ngoài mọi thứ công khai | Nó đi theo bản sao của thư mục |
| Chạy trình kiểm tra trên máy mới | Trước mọi thứ khác |
| Cài và kiểm tra project | `bun install` và `bun run typecheck` trong thư mục phim. Một project link thư mục sẽ tạo lại link ở đây |
| Tạo lại môi trường Python | Nó không chuyển đi được |
| Mang theo memory của assistant | Nó nằm ngoài project. Giữ một bản sao bên trong project và khôi phục nó |
| Đưa project vào version control | Để hai bản sao có thể được so sánh và hợp nhất sau này |
| Quyết định bản nào mới hơn | Sau lần sửa đầu tiên trên máy mới, hai bản sẽ khác nhau. Không bao giờ chép file engine từ bản cũ đè lên bản mới |

Từ thực tế: một project chép từ macOS sang Windows đã chạy được, nhưng chậm. Nguyên nhân là lần upload mô tả ở trên, chỉ được sửa trên bản sao Windows. Từ đó trở đi bản Windows là bản mới hơn.

## 6. Trình duyệt của owner

Trình duyệt capture và trình duyệt của owner thường không giống nhau. Một shot có thể đúng trong mọi capture và trống trơn trên màn hình của owner.

| Tính năng | Chrome | Safari | Làm gì |
|---|---|---|---|
| Thuộc tính `filter` của canvas 2D | Có | Thiếu trong các phiên bản gặp trong thực tế. Đã vào mã nguồn engine năm 2024; phiên bản stable có nó chưa được xác lập | Đừng dùng nó trong shot. Code engine vá nó phải kiểm tra nó có tồn tại không |
| `letterSpacing` của canvas 2D | Có | Từ 18.4 | Đừng để layout phụ thuộc vào nó |
| `roundRect` | Có | Từ 16.4 | An toàn |
| `OffscreenCanvas` | Có | Dùng được từ 16.4 | An toàn ở các phiên bản hiện tại |
| Render vào texture float | Có | Half-float là lựa chọn an toàn; full float phụ thuộc phần cứng và không có trên điện thoại | Dùng target half-float |
| Âm thanh tự phát | Cả hai đều cần một thao tác của người dùng | | Owner bấm play: không có vấn đề gì với studio. Nó chỉ quan trọng với các công cụ tự phát âm thanh khi không có người |

Cách tìm lỗi trong trình duyệt của owner:

1. Hỏi họ dùng trình duyệt nào. Hoặc đọc từ log của development server: một stack có các frame dạng `name@http://...` và `[native code]` là WebKit.
2. Đọc các lỗi mà trang gửi về log server. Đảm bảo server được thiết lập để chuyển console của trình duyệt sang; nó có thể chỉ làm vậy khi được một agent khởi động.
3. Tái hiện trong WebKit của Playwright, trên máy Mac nếu owner dùng Safari.
4. Sửa trong engine nếu lỗi do engine; nếu không thì sửa trong shot.

Đừng trả lời một báo cáo shot trống bằng một phỏng đoán.

## 7. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Trang tải được nhưng không có âm thanh hoặc không có dữ liệu | File không nằm trong `audio/` hoặc `data/` dưới tên ghi trong `src/project-config.ts` (starter trả về 404); trong một project có link thì các link bị thiếu | Đặt file vào đó; tạo lại link, trên Windows dưới dạng junction |
| Capture rất chậm và trông hơi khác | Headless shell vẽ bằng phần mềm | Khởi động trình duyệt đầy đủ |
| Công cụ capture không khởi động được trình duyệt trên Windows hoặc Linux | Nó yêu cầu backend của hệ thống khác | Chọn flag theo hệ thống |
| Mọi thứ chậm trên Windows và nhanh trên Mac | Lần upload canvas | Bản sửa ở trên |
| Một shot trống với owner, ổn trong capture | Một tính năng mà trình duyệt của họ thiếu | Mục 6 |
| Trang một file mở ra trống trong một trình duyệt | Cho đến nay chỉ Chrome trên Windows đã mở nó. Nó cần inline module script, các đối tượng `Response` tạo trong trang, `createImageBitmap` và blob URL, những thứ các trình duyệt hiện tại đều có | Đọc console của trình duyệt đó; báo lại trình duyệt và phiên bản nào |
| `python` không làm gì trên Windows | Stub của Store | Tắt alias |
| Môi trường Python lỗi sau khi chép | Nó giữ đường dẫn của máy cũ | Tạo lại nó |
| Một công cụ đã cài nhưng báo "not found" | Terminal cũ hơn lần cài đặt | Mở một terminal mới |
| Hai project trả lời trên cùng một port và capture cho thấy nhầm phim | Công cụ capture lấy bất kỳ server nào trả lời | Mỗi project một port, và một dấu hiệu trong trang nêu tên project |
| Thời gian frame đo được tốt mà phát lại vẫn giật | Phép đo được làm trên một hệ thống hoặc trình duyệt khác với của owner | Đo ở nơi phim được xem |
