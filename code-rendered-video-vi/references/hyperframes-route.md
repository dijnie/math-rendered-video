# Route HyperFrames

HyperFrames là gì, nó cần gì, nạp skill nào của nó cho tác vụ nào, và cách dùng nó bên trong skill này mà không phá vỡ quy tắc của owner. Các dữ kiện lấy từ file skill của họ HyperFrames và từ các lần chạy chỉ-đọc dòng lệnh của nó, phiên bản 0.8.81, ngày 2026-09-28. Bảng dữ kiện đầy đủ, kèm nguồn, là `hyperframes-facts.md`.

Nạp file này khi: `route-selection.md` đưa một bộ phim sang HyperFrames hoặc sang dùng kết hợp, owner nêu tên HyperFrames, hoặc một phần của nó (caption, âm thanh, một transition, một still) được mượn cho một phim engine.

Ký hiệu dùng trong file này: **stated** (đã nêu) nghĩa là được viết trong một file skill của HyperFrames hoặc được dòng lệnh của nó in ra. **Inferred** (suy ra) nghĩa là một kết luận rút ra từ đó. **Unknown** (chưa biết) nghĩa là không có file nào trả lời.

## 1. Nó là gì

| Vấn đề | Dữ kiện |
|---|---|
| Ý tưởng | Video render từ HTML. Một composition là một trang mà các phần tử khai báo timing của chúng trong các thuộc tính `data-*` và hoạt ảnh chạy trên một timeline có thể tua (seek) được |
| Nhà sản xuất | HeyGen. Package là `hyperframes` trên npm, mã nguồn và các skill nằm tại `github.com/heygen-com/hyperframes` |
| Cách tạo frame | Một Chrome headless được pin phiên bản tải composition, runtime tua nó từng frame một, các frame được capture, ffmpeg encode |
| Tính tất định | "Same input time, same pixels." (Cùng thời điểm đầu vào, cùng pixel.) Bị cấm cho mọi thứ nhìn thấy được: đồng hồ thực, số ngẫu nhiên không có seed, tải qua mạng lúc render, trạng thái con trỏ và cuộn, lặp vô tận |
| Runtime mặc định | GSAP, với một timeline tạm dừng cho mỗi composition, được đăng ký theo id của composition |
| Các runtime khác | Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU |

Quy tắc tất định của nó giống với nguyên tắc đầu tiên của route engine. Đó là lý do một canvas của engine có thể nằm bên trong một composition.

## 2. Nó cần gì

| Hạng mục | Yêu cầu | Ghi chú |
|---|---|---|
| Node.js | 22 trở lên | stated |
| ffmpeg và ffprobe | Có trên path | stated |
| Trình duyệt | Chrome headless được pin riêng của nó, tải về bằng `npx hyperframes browser ensure` | stated |
| Docker | Chỉ cho việc render trong container | stated |
| Python | Chỉ cho giọng nói cục bộ tuỳ chọn, nhạc cục bộ và việc trích xuất dữ liệu audio | stated |
| Tài khoản | Không cần cho công việc cục bộ: lint, check, snapshot, preview, render | render cục bộ là stated; phần còn lại là inferred |
| Tài khoản | Cần để publish, để render trên cloud của nó, và cho giọng đọc, nhạc, hiệu ứng âm thanh và hình ảnh của nó | stated |
| Hệ điều hành | Không có danh sách nào được đưa ra. Các file của nó có nhắc tới macOS, Linux và Windows | unknown hệ nào được hỗ trợ hàng đầu |

Kiểm tra máy bằng `scripts/check-environment.mjs --route hyperframes`, sau đó bằng `npx hyperframes doctor` của chính nó. Doctor của nó ở chế độ JSON luôn thoát với mã không: hãy đọc trường `ok` trong những gì nó in ra.

### Nó gửi những gì ra ngoài

| Vấn đề | Dữ kiện | Công tắc |
|---|---|---|
| Telemetry sử dụng | Bật theo mặc định | `HYPERFRAMES_NO_TELEMETRY=1`, hoặc `npx hyperframes telemetry disable` |
| Kiểm tra các skill so với nguồn ở mỗi lần `init` | Bật theo mặc định | `HYPERFRAMES_SKIP_SKILLS=1` |
| Một lượt đánh giá sau khi render | Skill dòng lệnh của nó bảo agent gửi một lượt, tới một kênh công khai | Đừng gửi khi chưa có sự cho phép của owner |
| Font | Một họ font không đi kèm sẵn sẽ được tải từ một dịch vụ font khi phim được build | Dùng các họ font đi kèm, hoặc đóng gói kèm file |

Báo cho owner về những điều này trước lần chạy đầu tiên, và đặt các công tắc theo lựa chọn của họ.

## 3. Họ skill

Cài bằng `npx hyperframes skills`. Nạp skill sở hữu tác vụ đó.

| Skill | Sở hữu | Nạp khi | Không dùng cho |
|---|---|---|---|
| `hyperframes` | Điểm vào: trạng thái dự án, phỏng vấn, định tuyến, các contract cho brief, storyboard, review và sản xuất | Một yêu cầu mới; tiếp tục một dự án | Viết một composition |
| `hyperframes-core` | Contract của một composition: thuộc tính timing, clip, track, sub-composition, biến, tính tất định | Trước khi viết bất kỳ composition nào | Chuyển động, look, mix |
| `hyperframes-cli` | Vòng làm việc và mọi lệnh | Chạy hoặc chẩn đoán một lệnh | Chọn media hoặc chuyển động |
| `hyperframes-animation` | Quy tắc chuyển động, blueprint của scene, transition, kỹ thuật, các adapter cho runtime | Mọi tác vụ chuyển động | Contract; các quyết định về thương hiệu |
| `hyperframes-creative` | Đặc tả thiết kế, preset khung hình, bảng màu, chữ, phong cách hình ảnh, lời dẫn, điều phối beat, hình ảnh phản hồi theo âm thanh | Look, nhịp độ, kịch bản | Công thức hoạt ảnh |
| `hyperframes-keyframes` | Keyframe chịu được việc tua: punch in, reframe, slow push, chiều sâu 3D, chuyển giao bằng match hoặc whip | Một chuyển động camera | Chiến lược scene, caption, media |
| `hyperframes-registry` | Tìm, cài và nối các block và component có sẵn | Trước khi tự tay dựng bất kỳ look nào đã có tên | Ví dụ |
| `hyperframes-studio` | Cách bố trí một timeline để dễ đọc; vùng an toàn | Dựng một dự án mà mọi người sẽ mở trong Studio của nó | Cách thực hiện một chỉnh sửa |
| `hyperframes-audio` | Mix âm thanh đã được đặt sẵn: fade, automation, khoét chỗ cho giọng đọc trong nhạc, hiệu ứng, một bus | Âm thanh trên timeline cần mix | Tìm hoặc tạo âm thanh |
| `media-use` | Tìm, tạo và ghi nhớ media: nhạc, hiệu ứng âm thanh, hình ảnh, icon, giọng đọc, caption, chép lời | Mọi nhu cầu về asset | Mix các track đã đặt |
| `faceless-explainer` | Một workflow: từ một văn bản đến một explainer có lời dẫn với hình ảnh sáng tác | Một chủ đề, một bài viết, ghi chú; không có sản phẩm và không có website | Phim dựng từ một website |

Các workflow mà skill điểm vào nêu tên và được cài ở lần dùng đầu tiên: `general-video`, `product-launch-video`, `pr-to-video`, `motion-graphics`, `music-to-video`, `slideshow`, `embedded-captions`, `talking-head-recut`, `remotion-to-hyperframes`, `figma`. Cài một workflow là một lần tải về: hãy hỏi owner.

## 4. Skill điểm vào của nó hoạt động thế nào

1. Nó bắt đầu từ trạng thái của dự án. Một file brief nghĩa là "thực thi và không hỏi gì". Một file dự án hoặc một storyboard nghĩa là "tiếp tục". Không có gì nghĩa là "phỏng vấn".
2. Nó định tuyến theo thứ cần bàn giao, theo một thứ tự ưu tiên cố định. Nhạc chỉ chọn workflow nhạc khi beat dẫn dắt bộ phim; nhạc làm nền thì không.
3. Nó phỏng vấn theo tám bước: xem `interview.md`, mục 9.
4. Nó viết brief, rồi storyboard, và xin review khi lần chạy là "có người đồng hành" ("in company").
5. Nó phân công một worker cho mỗi frame của storyboard.
6. Nó chỉ render khi có lời của owner: "Rendering remains user-gated in both modes." (Việc render vẫn phải chờ người dùng cho phép ở cả hai chế độ.)

Các file nó giữ trong một dự án:

| File | Vai trò |
|---|---|
| `BRIEF.md` | Ý định đã được xác nhận. Tài liệu định tuyến duy nhất |
| `STORYBOARD.md` | Kế hoạch: mỗi frame một section, mỗi section có một trạng thái |
| `SCRIPT.md` | Lời dẫn, đã khoá |
| `frame.md` | Đặc tả thiết kế |
| `storyboard.html` | Một sheet các bản phác để review |
| `index.html`, `compositions/` | Bộ phim |
| `hyperframes.json`, `package.json` | Dự án và phiên bản đã pin |
| `audio_meta.json`, `caption_groups.json` | Giọng đọc, thời điểm từng từ, nhạc, hiệu ứng âm thanh; các nhóm từ của caption |

## 5. Các lệnh quan trọng

| Giai đoạn | Lệnh | Làm gì |
|---|---|---|
| Thiết lập | `npx hyperframes doctor` | Kiểm tra máy |
| | `npx hyperframes init NAME` | Tạo một dự án |
| | `npx hyperframes capture URL` | Biến một website thành các component chỉnh sửa được |
| Biên soạn | `npx hyperframes catalog --query "..."` | Tìm trong registry. Việc tìm là cục bộ |
| | `npx hyperframes add NAME` | Cài một block hoặc một component. Cần mạng |
| Kiểm tra | `npx hyperframes lint` | Kiểm tra tĩnh |
| | `npx hyperframes check` | Lint, runtime, bố cục, chuyển động và độ tương phản, trong một trình duyệt. Cổng kiểm cuối cùng. Nó không phải là cổng kiểm cho hình ảnh: nó cho qua một composition không vẽ gì cả |
| | `npx hyperframes snapshot --at 3.5` | Still tại các thời điểm được chọn |
| | `npx hyperframes keyframes --ghost` | Onion skin (ảnh chồng mờ), cả cho canvas và WebGL |
| Xem trước | `npx hyperframes preview` | Khởi động Studio của nó trên port 3002. Địa chỉ phải mang theo dự án: `http://localhost:3002/#project/NAME` |
| | `npx hyperframes play` | Một trình phát nhẹ trên port 3003 |
| | `npx hyperframes preview --stop` | Dừng server. Làm điều này khi owner đã xem xong |
| Âm thanh | `npx hyperframes beats` | Tìm beat trong track nhạc, cho Studio |
| | `npx hyperframes tts`, `transcribe` | Giọng nói cục bộ; thời điểm từng từ từ một bản ghi âm |
| Render | `npx hyperframes render` | Bộ phim dưới dạng một file. Chỉ khi có lời của owner |

Luôn nhìn vào still. Bước check của nó là về cấu trúc; một frame có tốt hay không là thứ được nhìn thấy, không phải được tính toán.

## 6. Những gì nó đã có sẵn

Trước khi tự tay viết bất cứ thứ gì, hãy xem ở đây. Tên và đường dẫn nằm trong `hyperframes-facts.md`, mục 6.

| Danh mục | Quy mô | Nằm ở đâu trong các skill của nó |
|---|---|---|
| Transition trang | 32 tên trong 13 nhóm | `hyperframes-animation/transitions/` |
| Transition shader | 14 block | registry. "Use at most two per video" (Dùng tối đa hai cái mỗi video) |
| Transition an toàn để chèn giữa các scene | 5: `crossfade`, `blur-crossfade`, `push-slide`, `zoom-through`, `squeeze` | `hyperframes-animation/transitions/TRANSITION-REGISTRY.md` |
| Quy tắc chuyển động | 48 | `hyperframes-animation/rules/` |
| Blueprint của scene | 22, rút ra từ các phim ra mắt sản phẩm | `hyperframes-animation/blueprints/` |
| Kỹ thuật | 13 | `hyperframes-animation/techniques.md` |
| Preset khung hình | 13 | `hyperframes-creative/frame-presets/` |
| Phong cách hình ảnh, bảng màu | 8 và 9 | `hyperframes-creative/references/`, `palettes/` |
| Họ font đi kèm | 18 | `hyperframes-creative/references/typography.md` |
| Component caption | 15 | `media-use/audio/references/captions/` |
| Hiệu ứng âm thanh đi kèm | 19 | `media-use/audio/assets/sfx/` |
| Registry của block và component | Các file của nó đưa ra bốn con số khác nhau, từ "50+" đến "khoảng 400" | registry; đếm bằng `catalog` |

Các danh mục của skill này tham chiếu chéo tới chúng theo tên: `transitions.md`, `art-styles.md`, `camera.md`, `effects.md`, `type-and-captions.md`.

## 7. Giới hạn của nó, theo chính các file của nó

| Vấn đề | Giới hạn |
|---|---|
| Phần tử trang dùng làm hạt | Khoảng bốn mươi |
| Trang được vẽ vào canvas để làm hiệu ứng | "For 1 to 3 hero beats per video, not every beat" (Cho 1 đến 3 beat chủ đạo mỗi video, không phải mọi beat) |
| Three.js | Không có độ dài nào được suy ra; root phải nêu rõ nó. Không có hiệu ứng nào phụ thuộc vào các frame trước, trừ khi trạng thái có thể dựng lại từ thời gian |
| Transition shader | Chúng capture trang qua một thư viện không biết mọi style: không `transparent` trong gradient, không biến style, cùng một số thứ khác |
| Âm thanh | "No automatic waveform sync or drift correction" (Không tự động đồng bộ dạng sóng hay sửa trôi nhịp) |
| Hình ảnh phản hồi theo âm thanh | Nó khuyên không nên dùng thanh (bar), phổ (spectrum), dạng sóng và quả cầu nhấp nháy |
| Motion blur | Mỗi phần tử được đánh dấu tốn thêm nhiều lần tua cho mỗi frame |
| Độ dài | Các workflow kể chuyện của nó mạnh nhất từ ba mươi đến chín mươi giây |
| Registry | Mỗi lần cài đều cần mạng |

## 8. Dùng nó theo quy tắc của owner

| Quy tắc | Cách giữ nó |
|---|---|
| Không export video | Dừng trước `render`. Trạng thái cuối là một composition qua được `check`, đã được xem qua still, và phát được trong preview |
| Chỉ still, mỗi lúc một tiến trình | `snapshot --at` và `check`, cái này sau cái kia. Các worker viết frame không chạy dòng lệnh |
| Không để server nào chạy lại | `npx hyperframes preview --stop`, và `--list` để thấy rằng không còn gì |
| Không chi tiền khi chưa hỏi | Chọn đường offline lúc thiết lập. Hỏi trước bất kỳ giọng đọc, nhạc, hình ảnh hay render cloud nào có tốn phí |
| Không gửi gì ra ngoài | Đặt các công tắc của mục 2 trước lệnh đầu tiên |
| Owner duyệt storyboard | Chạy ở chế độ "in company", với sheet phác thảo |
| Builder trên Opus mới nhất | Khởi động các worker frame của nó trên model đó |

## 9. Những chỗ các file của nó mâu thuẫn nhau

Đã tìm thấy tám mâu thuẫn giữa các file trong họ skill. Chúng quan trọng khi một lần lint hoặc check phàn nàn về điều mà một file khác cho phép.

| Vấn đề | Một file | File khác |
|---|---|---|
| Dựng timeline trong code bất đồng bộ | Được hỗ trợ | Bị cấm |
| Những thuộc tính nào được phép animate | Không có danh sách cố định; width và height là hợp lệ | Width, height, top và left bị cấm |
| Font | Một họ font có tên cần khai báo file của nó trong trang | "Just write the family you want" (Cứ viết họ font bạn muốn) |
| Hoạt ảnh làm một scene rời đi | Bị cấm trừ ở scene cuối | Được dạy như một kỹ thuật |
| Chỉ số (index) của một track | Chỉ để hiển thị | Quyết định thứ gì nằm phía trước |
| Class `clip` trên scene | Thêm vào | Đừng thêm trong các composition độc lập |
| Dạng của một lần xuất hiện | Từ điểm bắt đầu đến điểm kết thúc, cả hai đều được cho | Ví dụ tối giản chỉ cho điểm bắt đầu |
| Các frame rate được phép render | 24, 30, 60 | Lệnh chấp nhận từ 1 đến 240 và cả phân số |

Khi hai file mâu thuẫn, contract trong `hyperframes-core` và hành vi của dòng lệnh là bên quyết định. Nói rõ trong báo cáo là đã theo bên nào.

## 10. Chưa biết

| Câu hỏi | Vì sao nó quan trọng |
|---|---|
| Một composition có phát được như một trang thuần, không cần preview, trình phát hay hosting của nó không? | Nó quyết định route này có bàn giao được "một trang phát được" hay không |
| File beat mà `beats` ghi ra chứa gì, và workflow nhạc xử lý một tempo bị trôi ra sao? | Nó quyết định route này có thể bám theo một grid đã đo tới mức nào |
| Các họ font đi kèm của nó có hỗ trợ tiếng Việt không? | Một dấu bị thiếu sẽ rơi về một kiểu chữ khác |
| Registry hiện nay lớn cỡ nào? | Các file của nó đưa ra bốn con số |
| Hệ điều hành nào được hỗ trợ hàng đầu? | Owner có thể dựng trên Windows |

Tìm câu trả lời bằng cách thử, trên một dự án nhỏ, trước khi một bộ phim phụ thuộc vào nó.
