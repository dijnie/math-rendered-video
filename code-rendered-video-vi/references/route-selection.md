# Chọn route

Cách chọn đường dựng một phim (route), dựa trên những gì brief yêu cầu. Skill nắm sâu hai route, route engine và route HyperFrames, và nêu tên các route khác để một yêu cầu thuộc về chỗ khác thì được chuyển sang đó.

Nạp file này khi: brief đã thống nhất và chưa có gì được thiết lập, owner nêu tên một công cụ, một yêu cầu có thể hoàn toàn không phải là phim (một game, một thế giới để đi dạo, một bản dựng footage), hoặc một phim đang làm hóa ra cần thứ mà route của nó không cung cấp được.

## 1. Các route

| Route | Nó là gì | Phim được làm từ | Kết thúc bằng |
|---|---|---|---|
| **Engine** | Một rendering engine nhỏ viết riêng cho mục đích này, trên WebGL2, với các layer canvas 2D, line batch, shader và cảnh 3D. Mỗi frame là một hàm của thời gian bản nhạc | Các shot viết thành module code, mỗi shot một file | Một trang studio phát phim trực tiếp. Chỉ ra file video khi được yêu cầu |
| **HyperFrames** | Một framework render video từ HTML. Timing được khai báo trong trang, animation chạy trên một timeline có thể seek | Các composition HTML, mỗi cảnh một composition, kèm style và một timeline | Một file video, qua Studio của nó để review |
| Mixed (kết hợp) | Canvas của engine làm một layer bên trong composition HyperFrames, với tiêu đề, caption và âm thanh từ framework | Cả hai | Một file video |

Các công cụ đã cài trên máy là ứng viên. Không công cụ nào là bắt buộc chỉ vì nó có sẵn.

## 2. Quyết định theo những gì brief yêu cầu

Đi xuống bảng. Dòng đầu tiên khớp sẽ quyết định, trừ khi một dòng sau mâu thuẫn mạnh với nó.

| Brief yêu cầu | Route | Lý do |
|---|---|---|
| Một giọng đọc kịch bản, với caption chạy theo từng chữ | Cả hai | HyperFrames khai báo lời nói với word timing, transcription, các component caption và nhạc được khoét xuống dưới giọng; chưa thứ nào trong số đó được chạy thử ở đây. Engine có giọng local hoặc thời gian từ ước lượng, cụm từ đặt trên beat, ducking và nhóm caption (`references/sound-and-voice.md`). Giọng tiếng Việt cần edge-tts, vốn gửi văn bản ra ngoài, hoặc một giọng trả phí: hãy hỏi |
| Một phim làm từ website, các màn hình của sản phẩm, hoặc một pull request, giữ nguyên các component của chính site | HyperFrames | Nó chụp một site thành các component chỉnh sửa được và có các blueprint cảnh rút ra từ các phim launch |
| Một phim làm từ màn hình thật của sản phẩm, dựng lại để chúng morph (biến hình), trên beat | Engine | Phần research của `thinking-and-brainstorm.md`, mục 2, rồi các màn hình được dựng lại thành hình khối trong một shot. Xem `short-pieces.md`, mục 7.3 |
| Caption hoặc card overlay trên footage có sẵn | HyperFrames | Nó nắm việc phát media và có workflow cho cả hai |
| Một deck để trình chiếu, không phải để phát | HyperFrames | Nó có route slideshow với presenter mode |
| Một overlay có độ trong suốt, để đặt lên video khác | HyperFrames | Nó render các định dạng có kênh alpha |
| Một đoạn ngắn 5 đến 40 giây: showreel, logo sting, teaser, đoạn UI, quảng cáo | Engine, trong lane ngắn | Hình vẽ trên beat, giao dưới dạng một trang. `short-pieces.md` |
| Nhiều phiên bản của một phim từ một bảng dữ liệu | HyperFrames | Biến và batch render |
| Hình ảnh là shader, hoặc hàng nghìn đường hay hạt | Engine | Các bước kiểm tra và công thức của framework làm việc trên trang và không nhìn được vào bên trong canvas. Phần tử trang dùng làm hạt bị giới hạn ở khoảng bốn mươi |
| Một camera di chuyển xuyên qua một thế giới được dựng mô hình | Engine | Camera bay của framework di chuyển các card theo chiều sâu, chỉnh bằng mắt |
| Mọi sự kiện nằm trên beat đo được của một track, có drop | Engine | Engine đọc một grid đo từ track, grid này có thể trôi (drift). Framework nói rõ nó không sửa drift |
| Một lớp hoàn thiện trên toàn frame: bloom, grain, halation, viền màu | Engine | Framework không có chuỗi hiệu ứng trên toàn frame |
| Một trang phát phim, và không có file video | Engine | Các workflow của framework kết thúc bằng một lần render. Không file nào tìm thấy nói rằng một composition phát được như một trang thường mà không cần server hay player của nó. Studio của engine phát phim, và bản build một file của phim hoàn chỉnh mở được mà không cần server (`studio-viewer.md`) |
| Không tải lên máy ngoài các still đơn lẻ | Engine | Lần render của framework khởi động nhiều trình duyệt |
| Giao diện, chữ, biểu đồ, sơ đồ vẽ dưới dạng phần tử trang | Cả hai | Chọn theo những gì khác mà phim cần |
| Một explainer có caption dài ba mươi đến chín mươi giây về một chủ đề, với hình ảnh sáng tác | Cả hai | Có giọng thì cả hai: engine khi hình được vẽ và nhạc nền được soạn; HyperFrames khi một giọng thu sẵn phải được transcribe. Cắt theo nhạc với hình được vẽ: engine |

Từ thực tế: hai phim đã được làm trên route engine. Cả hai đều cắt theo một track làm riêng cho chúng, không có giọng; cả hai dùng shader, line batch và 3D; phim thứ hai được giao dưới dạng trang studio vì owner cấm xuất video trên máy đó.

## 3. Mỗi route mạnh ở đâu

| | Engine | HyperFrames |
|---|---|---|
| Hình ảnh | Bất cứ thứ gì tính được theo từng pixel hay từng vertex | Bất cứ thứ gì trình duyệt dàn trang được: chữ, hộp, SVG, ảnh, video |
| Đồng bộ | Theo một grid đo được gồm beat, bar và section; các cụm từ của giọng đặt trên beat, các từ ở đúng thời gian của giọng | Theo giây; theo word timing của giọng; theo một nhịp đều |
| Camera | Tự do, phẳng hoặc trong không gian, theo từng shot | Các wrapper di chuyển bên trong một clip; card theo chiều sâu |
| Transition | Viết riêng cho phim: xem `transitions.md` | Một catalogue transition trang và các khối shader, tối đa hai transition shader mỗi phim |
| Chữ | Đặt bởi overlay hoặc bởi shot | Chữ trên trang; component caption |
| Âm thanh | Một track hoàn chỉnh, tiếng click của grid, hoặc một bản score, hiệu ứng âm thanh và voice-over viết bằng code và mix với ducking và limiter (`references/sound-and-voice.md`) | Track, mix, hiệu ứng, ducking, hiệu ứng âm thanh |
| Review | Trang studio; still và contact sheet | Studio của nó, một trình chỉnh timeline; snapshot; một bước kiểm tra audit layout, chuyển động và độ tương phản |
| Sản phẩm giao | Một trang. Một file nếu được yêu cầu | Một file. Một trang được host qua lệnh publish của nó |
| Chi phí khởi đầu | Trung bình: starter của skill (`assets/starter/`) mang theo engine, kit, studio và công cụ capture, và phim tự đặt look của mình: palette, font, zone, nền, giọng chữ, preset post | Thấp: một scaffold và một registry các phần làm sẵn |
| Chi phí mỗi cảnh | Một builder viết code và xem still | Một worker viết một trang từ một công thức |
| Độ dài phù hợp | Bất kỳ; đã thử đến ba phút | Mạnh nhất trong khoảng ba mươi đến chín mươi giây, đến khoảng ba phút |
| Ai đọc bên trong | Shader và code vẽ | HTML và CSS |

## 4. Dùng kết hợp

Ba cách lấy từ cả hai.

| Cách | Làm thế nào | Khi nào |
|---|---|---|
| Canvas của engine bên trong một composition | Framework chuyển thời gian cho canvas qua sự kiện seek của nó, và canvas vẽ thời điểm đó. Quy tắc của engine rằng một frame là một hàm của thời gian khớp chính xác với điều này | Một phim cần hình ảnh của engine và caption, giọng, âm thanh của framework |
| Mượn các phần, không mượn pipeline | Các quy tắc nhóm caption của nó, bộ từ vựng năm transition an toàn của nó, các hiệu ứng âm thanh đi kèm, các preset frame của nó làm tham chiếu cho một look | Một phim engine muốn một trong những thứ đó |
| Still từ công cụ của nó | Lệnh snapshot của nó tạo các still đơn lẻ ở những thời điểm chọn trước | Review một composition theo quy tắc "chỉ still" |

Khi dùng kết hợp, trước hết hãy quyết định clock nào cai quản. Với một grid đo được thì clock của engine cai quản và framework được báo các thời điểm. Với một giọng thì word timing cai quản và engine được báo.

## 5. Công cụ được nêu tên, và các yêu cầu nằm ngoài phương pháp

### Khi một yêu cầu nêu tên một công cụ

Các công cụ được nêu tên trong yêu cầu là ứng viên, giống như các công cụ đã cài trên máy. Nói rõ công cụ được nêu sẽ thay đổi điều gì, và skill đề xuất gì thay vào đó, trước khi chọn.

| Công cụ được nêu | Nó là gì | Skill làm gì |
|---|---|---|
| HyperFrames | Một framework render video từ HTML | Route HyperFrames của skill này: `hyperframes-route.md` |
| Remotion | Một framework dựa trên React, mô tả video dưới dạng component và render ra file | Không bao quát. Đích thường thấy của nó là một file đã render, việc này ở đây cần owner yêu cầu; giấy phép của nó không phải là mã nguồn mở thuần túy cho mọi người dùng, nên hãy đọc trước khi chọn. Nếu owner muốn chính Remotion, nói rằng starter, studio và các bước kiểm tra của skill này không áp dụng, và giữ các quy tắc của phương pháp (frame là hàm của thời gian, still, không export trừ khi được yêu cầu). HyperFrames có một workflow chuyển mã nguồn Remotion sang |
| Manim, hoặc một thư viện khác cho animation toán học | Các thư viện Python render chứng minh, đồ thị và công thức ra file video | Không bao quát. Đầu ra của nó là một file video đã render, tức là một lần export theo quy tắc của owner. Đề xuất route engine, vốn vẽ đồ thị, công thức và dựng hình bằng code và phát dưới dạng một trang; hoặc, nếu owner muốn thư viện đó, nói rằng lần render của nó cần owner yêu cầu |
| Blender | Một bộ công cụ 3D, viết script được bằng Python | Không phải một route của skill này. Lần render của nó là một export và tải nặng lên máy. Các model làm ở đó, dưới dạng glTF, có thể được three.js nạp vào một shot engine. Xem `environment.md` để cài đặt |
| After Effects, "kiểu After Effects" | Một chương trình compositing trên desktop | Hiểu là mô tả một look (chuyển động nhiều lớp, có easing, được composite), không phải một công cụ để chạy. Route engine tạo ra look đó |
| GSAP | Một thư viện animation JavaScript với timeline seek được | Được route HyperFrames dùng, mỗi composition một timeline tạm dừng. Route engine không dùng nó: spring và ease là các hàm của thời gian trong kit |
| Công cụ tạo ảnh hoặc video (các model có tên, dịch vụ trả phí) | Nguồn hình ảnh hoặc clip | Trả phí: hỏi owner mỗi lần, kèm giá. Clip được tạo ra là footage (bên dưới) |
| Unity, Unreal, game engine | Engine cho game tương tác | Nằm ngoài phương pháp (bên dưới) |
| C hoặc C++ với OpenGL, một demo native | Một chương trình vẽ bằng GPU bên ngoài trình duyệt | Không bao quát. Route engine vẽ bằng WebGL2 trong trình duyệt, với shader viết bằng ngôn ngữ gần như giống hệt, và phát dưới dạng một trang. Phim của một chương trình native là một lần render từng frame, tức là một export theo quy tắc của owner. Đề xuất route engine; nếu owner muốn code native, nói rằng starter và studio không áp dụng |
| Python với ffmpeg | Một script vẽ các frame và encode chúng | Không bao quát: nó là một export ngay từ frame đầu tiên. Đề xuất route engine và studio của nó. Nếu owner muốn một file, dùng chế độ `video` của công cụ capture khi owner yêu cầu |
| Một tracker module (S3M, MOD, XM, IT) làm nhạc | Nhạc lưu dưới dạng pattern và sample, phát bởi một tracker | Phần phân tích đọc file audio, nên module trước hết được một module player render ra WAV, đó là một lần cài đặt: hãy hỏi. Các row, speed và tempo của nó cho ra beat chính xác, nên một grid có thể được viết từ chúng thay vì đo. Chưa thử |
| "Không thư viện", "một file HTML", "vanilla JavaScript" | Một yêu cầu một file duy nhất không phụ thuộc | Skill giao studio để làm việc và một bản build một file của phim hoàn chỉnh (xem `studio-viewer.md`), mang three.js và font bên trong. Hãy nói rõ điều đó. Nếu owner muốn hoàn toàn không có code thư viện, kể cả khi đã bundle, thì starter không phù hợp: báo owner trước khi bắt đầu; các quy tắc của phương pháp vẫn giữ nguyên, và builder viết code WebGL2 hoặc canvas thuần |
| 3D photoreal, PBR, "càng thật càng tốt" | Vật liệu, ánh sáng và ống kính dựa trên vật lý | Engine tiếp cận nó bằng three.js: ánh sáng môi trường, vật liệu vật lý, sương mù, độ sâu trường ảnh, god ray. Nó tốn thời gian frame và các vòng builder; nói rõ sẽ đạt gần đến mức nào. Photoreal thực sự (caustic, global illumination, người trông như thật) thuộc về một bộ công cụ 3D, mà lần render của nó là một export và tải nặng lên máy: cần lời của owner |

### Những yêu cầu không phải là phim theo phương pháp này

Một số yêu cầu trông giống yêu cầu làm phim nhưng không phải. Nói thẳng điều đó, nói skill có thể làm gì thay thế, và để owner chọn. Đừng lặng lẽ dựng thứ khác dưới cái tên một bộ phim.

| Yêu cầu | Skill làm gì | Những gì nó không làm |
|---|---|---|
| Một game chơi được, một prototype game, một game "trong một file HTML" | Một phim về game đó: trailer, màn tiết lộ phần thưởng, một lượt chơi theo kịch bản, vẽ bằng code và cắt theo nhạc. Một đoạn phát khi click (`short-pieces.md`, mục 11) | Bản thân game: điều khiển, luật chơi, vật lý chạy trực tiếp, màn chơi, lưu game. Đó là phần mềm, nằm ngoài skill này |
| Một thế giới 3D khám phá được: một ngôi nhà để đi qua, một thành phố, một hành tinh để xoay | Một chuyến bay xuyên qua thế giới đó dưới dạng phim, trên route engine: camera di chuyển theo beat (`camera.md`) | Điều khiển đi bộ hay orbit, camera tự do, một thế giới do người xem điều khiển |
| Một hiệu ứng trang web: header chạy theo thanh cuộn, con trỏ làm lộ một layer, một landing page | Không làm gì của trang đó. Một phim về ý tưởng của trang, nếu owner muốn một phim | Bản thân component đó |
| Một mô phỏng dạng đồ chơi: cát, lửa, chất lỏng, một sandbox vật lý | Một phim về một mô phỏng, nếu nó có thể được phát lại chính xác với bước cố định và ngẫu nhiên có seed: mô phỏng một lần khi shot được nạp và tra theo thời gian (`effects.md`, mục 2), hoặc một cảnh có trạng thái mà engine mô phỏng lại sau khi seek, từ tối đa `prerollMax` giây trước đó (`engine-architecture.md`) | Một món đồ chơi để người xem nghịch |
| Một bản dựng footage camera: một talking head cắt kèm phụ đề, một bản ghi demo được chỉnh, các clip cắt theo nhạc | Không phải phương pháp này. Engine có thể hiện ảnh và clip ngắn bên trong một phim vẽ, qua layer ảnh và một chuỗi frame trích xuất một lần (`engine-architecture.md`; việc trích xuất bằng ffmpeg là một lần chạy nặng và cần lời của owner), nhưng nó không cắt footage. Route HyperFrames có workflow cho caption trên footage và cho việc cắt lại một talking head (`hyperframes-route.md`); cài chúng là một lần tải về, nên hãy hỏi. Nếu không thì dùng một trình dựng video | Cắt footage trên route engine |
| Một phim làm chủ yếu từ các clip được tạo ra | Không phải phương pháp này. Đó là footage, và mỗi lần tạo đều trả phí | Tạo clip mà không có lời của owner mỗi lần |
| Một yêu cầu cấm skill, memory hay connector ("không skill, không MCP") | Tôn trọng nó: không dùng starter hay các chương của skill này cho phim đó, và nói rõ ngay từ đầu. Các quy tắc thường trực của owner trong file quy tắc của project không phải là skill và vẫn giữ nguyên: không export trừ khi được yêu cầu, không tiêu tiền, mỗi lần một still, không gửi gì ra ngoài. Nếu không rõ lệnh cấm nhắm vào skill này hay chỉ các dịch vụ bên ngoài, hãy hỏi; trong chế độ tự động, chọn cách hiểu chặt nhất và ghi lại | Lặng lẽ vẫn dùng starter, hoặc bỏ luôn các quy tắc của owner cùng với skill |

Owner có thể có skill riêng cho một loại phim hoặc cho game. Hãy hỏi trước khi dựng thứ họ đã có.

## 6. Xung đột với các quy tắc của owner

Các mặc định của một route có thể đi ngược với những gì owner đã quy định. Kiểm tra trước khi bắt đầu.

| Quy tắc của owner | Route engine | Route HyperFrames |
|---|---|---|
| Không export video | Đáp ứng: trang studio chính là phim | Các workflow của nó kết thúc bằng một lần render. Dừng trước bước đó; trạng thái cuối là một composition vượt qua các bước kiểm tra của nó, hiển thị ở preview |
| Một trang phát được, được bàn giao | Đáp ứng, với một development server | Cần preview, player hoặc hosting của nó |
| Chỉ still, mỗi lần một process | Công cụ capture giữ một lock | Snapshot và bước kiểm tra của nó mỗi cái khởi động một trình duyệt: chạy lần lượt từng cái. Không bao giờ chạy lần render của nó với nhiều worker |
| Không để server nào chạy lại | Dừng server studio khi owner đã xem xong | Preview chạy nền của nó cố ý được giữ sống: hãy dừng nó |
| Không tiêu tiền khi chưa hỏi | Tạo nhạc và giọng cloud là các bước trả phí; giọng cloud còn gửi kịch bản ra ngoài | Nó đề xuất giọng, nhạc, ảnh và render cloud trả phí, và thúc đẩy đăng nhập trong lúc thiết lập. Chọn đường offline hoặc hỏi |
| Không gửi gì ra ngoài | Không có gì được gửi | Telemetry bật theo mặc định. Tắt nó đi: `HYPERFRAMES_NO_TELEMETRY=1`. Skill của nó yêu cầu agent gửi đánh giá sau một lần render: đừng làm, trừ khi owner đồng ý |
| Builder chạy trên một model được chọn | Một builder cho mỗi section | Một worker cho mỗi frame, từ các packet: cùng một dạng |
| Storyboard được duyệt trước khi dựng | Animatic trong studio | Bước review storyboard của nó với một sketch sheet |

## 7. Đổi route giữa chừng

| Dấu hiệu | Nghĩa là | Làm gì |
|---|---|---|
| Một phim HyperFrames cần một shot là shader hoặc một trường hạt | Một shot đã vượt quá khả năng của trang | Đặt một layer canvas vào composition đó; giữ phần còn lại |
| Một phim engine có thêm giọng | Đồng bộ vẫn theo beat: các cụm từ của giọng đặt trên beat, các từ giữ thời gian riêng của chúng | Giữ engine (`references/sound-and-voice.md`). Chỉ lấy lời nói và caption từ framework, theo cách kết hợp, khi một giọng thu sẵn phải được transcribe |
| Một phim engine phải thành một file, trên một máy cho phép điều đó | Cách giao đã thay đổi | Công cụ capture của engine có một chế độ export bị từ chối trừ khi owner yêu cầu. Hỏi, rồi dùng nó |
| Owner muốn chỉnh timing bằng tay | Họ muốn một timeline | Studio của framework là một trình chỉnh timeline. Studio của engine là một player |

## 8. Ghi lại lựa chọn

Ghi vào file trạng thái của project: route, lý do trong hai dòng, các dòng của mục 6 áp dụng, và những gì đã bị loại. Phiên làm việc sau không phải quyết định lại.
