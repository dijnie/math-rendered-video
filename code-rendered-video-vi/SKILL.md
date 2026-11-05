---
name: code-rendered-video
description: Đạo diễn và dựng một bộ phim mà hình ảnh được vẽ bằng code trong trình duyệt và được cắt theo nhạc hoặc theo giọng đọc, từ ý tưởng đầu tiên đến một trang studio mà owner chỉ việc bấm play. Bao gồm phỏng vấn, nghiên cứu một sản phẩm thật hoặc số liệu thật, nhạc và beat grid, âm thanh viết bằng code, voice-over kèm caption, một storyboard giữ dưới dạng dữ liệu cùng một animatic, look, camera, transition, hiệu ứng, nhân vật và câu chuyện không lời, các agent builder, review bằng still; một làn nhẹ cho tác phẩm ngắn, với một chế độ tự hành. Chọn giữa một engine WebGL viết tay và HyperFrames. Dùng cho explainer, data explainer, music visual, lyric film, kinetic type, title sequence, showreel, logo sting, launch teaser, tác phẩm UI motion, quảng cáo mạng xã hội, loop liền mạch, nhiều định dạng, reveal bấm-để-phát, pixel art, collage và zoom powers-of-ten, làm mà không cần footage, kể cả khi yêu cầu nêu tên Manim, Remotion hay Blender. Không dùng cho game, thế giới khám phá được hay dựng footage.
license: MIT
metadata:
  version: "0.4"
  origin: "Written from two films made in the opus-videos repository, 2026-09"
---

# Video render bằng code

Ở đây một bộ phim là một chương trình. Mỗi frame là một hàm của thời gian của bản nhạc, nên một still đại diện được cho bộ phim, có thể tua tới bất kỳ khoảnh khắc nào, và những gì owner thấy trong studio chính là những gì một file sẽ chứa. Công việc được làm bởi một **lead** (phiên làm việc này), là người quyết định và review, và bởi các agent **builder**, là những người dựng các shot.

## Thuật ngữ

| Thuật ngữ | Nghĩa |
|---|---|
| Owner | Người yêu cầu bộ phim. Quyết định chủ đề, gu thẩm mỹ, tiền bạc, và phê duyệt |
| Lead | Phiên làm việc này. Quyết định route, viết storyboard và các quy tắc, dựng các lớp dùng chung, review |
| Builder | Một sub-agent dựng các shot của một section |
| Story writer | Một sub-agent suy nghĩ thấu đáo một section hoặc cả bộ phim và soạn nháp shot và câu chữ cho lead |
| Section | Một chương của bộ phim: một nhóm shot |
| Shot | Một module scene, dài vài bar |
| Beat, bar | Đo từ bản nhạc, không bao giờ tính từ một tempo |
| Studio | Trang mà bộ phim phát trên đó, từ storyboard card đến phim hoàn chỉnh |
| Animatic | Studio phát các storyboard card cùng với nhạc |
| Capture | Một still đơn lẻ, hoặc một sheet gồm nhiều still, tạo ra để review |
| Phim tham chiếu | Hai bộ phim mà phương pháp được viết ra từ đó: một phim ngang dài 135 giây, một phim dọc dài 172 giây với 54 shot. Code của chúng không thuộc skill; starter là bản sao chung của nó. Các ghi chú "From practice" trong các reference kể lại những gì đã xảy ra trên chúng |

## Các quy tắc áp dụng cho mọi bộ phim

1. **Một frame là một hàm của thời gian.** Không đồng hồ thực (wall clock), không số ngẫu nhiên không có seed, không trạng thái nào không thể dựng lại được từ thời gian.
2. **Nhìn vào kết quả.** Code chạy được không nói lên gì về việc hình có đẹp hay không. Capture, nhìn, đánh giá, sửa, capture lại.
3. **Owner phê duyệt trên giấy, rồi trên animatic, rồi trên một bản mẫu, trước khi bộ phim được dựng.** Một mục lục đã được duyệt không phải là giấy phép để dựng. Một tác phẩm ngắn có hai cổng kiểm, và trong chế độ tự hành các cổng kiểm trở thành các quyết định được viết ra (xem bên dưới).
4. **Lead không dựng shot**, kể cả một bản mẫu, kể cả trong một tác phẩm ngắn. Lead dựng engine, kit, transition, overlay và studio, và lead review.
5. **Trên Claude, các sub-agent suy nghĩ về storyboard và các sub-agent dựng shot chạy trên model Opus mới nhất.** Nêu tên model khi khởi động agent. Lead giữ model của chính mình và chịu trách nhiệm về kết quả. Trên trợ lý khác, dùng model mạnh nhất của nó cho công việc dài và cẩn thận.
6. **Thời gian được đo bằng beat đọc từ bản nhạc.** Sự kiện rơi vào beat. Không bao giờ vào giây, không bao giờ từ một con số tempo.
7. **Một nguồn sự thật duy nhất.** Shot, bar, transition và mọi câu chữ nằm trong hai file dữ liệu. Tài liệu storyboard, thời điểm của shot và các card được sinh ra từ chúng.
8. **Gu thẩm mỹ thuộc về tai và mắt của owner.** Đo những gì có đáp án đúng. Đừng tranh luận về gu bằng các phép đo.
9. **Một shot không được là hình ảnh của một ý tưởng lân cận.** Viết ra, cho từng section, những gì nó phải cho thấy và những gì nó không bao giờ được cho thấy, và đối chiếu mọi shot với cả hai.
10. **Không có gì tốn tiền, làm máy chạy nặng, hay rời khỏi máy mà không có lời đồng ý của owner.** Không export video trừ khi được yêu cầu trong cuộc hội thoại này. Capture từng cái một. Không để server nào chạy lại. Không upload thứ gì của owner. "Tự quyết đi" không gỡ bỏ quy tắc này.

## Các giai đoạn

| # | Giai đoạn | Output | Cổng kiểm | Nạp |
|---|---|---|---|---|
| 0 | Môi trường | Báo cáo của trình kiểm tra; những gì còn thiếu và cách cài | Owner cho phép cài đặt | `references/environment.md`, `scripts/check-environment.mjs` |
| 1 | Brief | Một trang: thông điệp rút ra (takeaway), khán giả, các phần, khung hình, độ dài, âm thanh, look, sản phẩm bàn giao, máy, tiền | **Owner xác nhận brief** | `references/interview.md` |
| 2 | Route | Engine, HyperFrames, hoặc kết hợp, kèm lý do | Thông báo cho owner | `references/route-selection.md`, `references/hyperframes-route.md`, `references/hyperframes-facts.md` |
| 3 | Suy nghĩ và concept | Cho từng phần: ý tưởng, vấn đề, phép so sánh, sự vật, nơi gặp nó, phải cho thấy, không bao giờ được cho thấy. Ba hướng đi | **Owner chọn một hướng và duyệt các phép so sánh** | `references/thinking-and-brainstorm.md` |
| 4 | Nhạc | Các ứng viên; lựa chọn của owner; một beat grid đã đo và đã kiểm; một bản đồ của bản nhạc theo bar | **Owner chọn bản nhạc bằng tai** | `references/music-and-beat.md`, `assets/starter/analysis/` |
| 5 | Storyboard | Danh sách shot và câu chữ dưới dạng dữ liệu; tài liệu được sinh ra; animatic trong studio | **Owner duyệt storyboard và câu chữ trên animatic** | `references/storyboard.md`, `references/transitions.md`, `references/camera.md`, `references/type-and-captions.md`, `references/art-styles.md` |
| 6 | Nền móng | Engine, kit, overlay, studio, công cụ capture; một phép thử rằng capture bằng với lúc phát | Lead tự kiểm | `references/engine-architecture.md`, `references/studio-viewer.md`, `assets/starter/` |
| 7 | Section mẫu | Một section do một builder dựng, được review, được trau chuốt | **Owner duyệt look trên bản mẫu** | `references/orchestration.md`, `references/effects.md` |
| 8 | Các section | Mọi section do builder của nó dựng; vòng nội dung, rồi tay nghề (craft), rồi trau chuốt (polish) | Lead chấp nhận từng section | `references/orchestration.md`, `references/quality-gates.md` |
| 9 | Toàn bộ phim | Các cú cắt giữa các section, recap, tiêu đề, end card, cường độ transition, hiệu năng | **Owner xem phim hoàn chỉnh** | `references/quality-gates.md` |
| 10 | Bàn giao | Studio đang chạy cho owner, hoặc đã dừng kèm hướng dẫn; README; trạng thái được ghi lại | Owner chấp nhận | `references/studio-viewer.md` |

Các giai đoạn có thể chồng lên nhau khi chúng nuôi lẫn nhau: hình dạng của bản nhạc quyết định độ dài trong storyboard. Các cổng kiểm thì không chồng lên nhau: tại một cổng kiểm, công việc dừng lại và chờ owner.

### Tác phẩm ngắn và chế độ tự hành

Một tác phẩm dài khoảng 5 đến 40 giây với một ý tưởng (showreel, sting, teaser, tác phẩm UI, quảng cáo) đi theo **làn ngắn**: vài giả định được nêu ra thay cho brief, một bảng beat trong dữ liệu shot thay cho storyboard đầy đủ, một builder cho cả tác phẩm, và hai cổng kiểm: bảng beat kèm vài still, và tác phẩm hoàn chỉnh. Khi owner nói "đừng hỏi tôi, tự quyết đi", các cổng kiểm trở thành **quyết định được viết ra** và trình bày ở cuối; tiền, export, tải máy, gửi bất cứ thứ gì ra ngoài và các vai trò vẫn giữ nguyên. Cả hai đều nằm trong `references/short-pieces.md`, cùng các công thức, loop liền mạch, nhiều định dạng và tác phẩm phát khi bấm.

## Ghi chú cho từng giai đoạn

### 0. Môi trường

Chạy `node scripts/check-environment.mjs` với route và các phần bổ sung phù hợp. Cho thấy những gì còn thiếu kèm lệnh cài đặt; chỉ cài khi có lời đồng ý của owner. Hỏi owner xem phim trên trình duyệt nào.

### 1. Brief

Nhắc lại yêu cầu trong ba dòng, liệt kê những gì đã được nêu và những gì được suy ra, rồi hỏi theo từng vòng tối đa bốn câu, mỗi câu có các lựa chọn và lựa chọn được khuyến nghị đứng đầu. Viết trang brief và trình bày nó. Giữ nguyên lời của owner trong file trạng thái của dự án. Một bộ phim về một sản phẩm, thương hiệu hoặc số liệu thật bắt đầu bằng phần nghiên cứu của `thinking-and-brainstorm.md`, mục 2: màn hình thật, logo, nội dung chữ (copy), màu sắc và số liệu, mỗi thứ kèm nguồn và quyền sử dụng của nó, không upload gì cả.

### 2. Route

Route engine dành cho hình ảnh là shader, trường đường nét hoặc hạt, bay xuyên qua một thế giới, một beat đã đo với các drop, phần hoàn thiện toàn khung hình, và bàn giao dưới dạng một trang. Route HyperFrames dành cho giọng đã ghi âm cần phải chép lời (transcribe), phim làm từ chính các component của một website hoặc từ footage, deck, overlay có alpha và các lô dựa trên dữ liệu; một voice-over viết riêng cho phim thì chạy được trên cả hai route. Dùng kết hợp khi cần cả hai. Đối chiếu các mặc định của route với quy tắc của owner (`route-selection.md`, mục 6) trước khi bắt đầu. Một game, một thế giới để đi dạo trong đó hay một bản dựng footage không phải là phim theo phương pháp này; yêu cầu nêu tên Manim, Remotion hay Blender được trả lời theo `route-selection.md`, mục 5.

### 3. Suy nghĩ và concept

Trả lời năm câu hỏi của `thinking-and-brainstorm.md` bằng văn bản trước. Sau đó điền bảng các phần, tìm các phép so sánh từ chính đời sống của người xem có cùng cấu trúc với từng ý tưởng, và cho mỗi phần một ngôn ngữ hình ảnh (idiom) lấy từ thế giới của phép so sánh của nó. Khởi động một **story writer trên Opus mới nhất** để soạn nháp bảng và ba hướng đi; tự mình kiểm bản nháp của nó theo các ranh giới. Đưa các hướng đi cho owner.

### 4. Nhạc

Đề xuất các nguồn; hỏi trước khi tạo bất cứ thứ gì có trả phí. Giao các ứng viên và để owner chọn bằng tai. Đo beat, bar và section bằng các script trong `analysis/` của starter: sao chép `assets/starter/` vào thư mục của phim ngay bây giờ (trên route HyperFrames, chỉ cần thư mục `analysis/` của nó), và tạo môi trường Python như README của nó hướng dẫn; kiểm grid bằng mắt, bằng cách đếm và bằng tai; sửa trôi nhịp (drift) và đếm sai. Hoặc soạn score bằng code (`references/sound-and-voice.md`); grid của nó không cần đo, và các section của nó phải cộng lại khớp với danh sách shot, nên hãy soạn nháp music map và storyboard cùng lúc và đưa cả hai cho owner, phần nhạc nghe bằng tai trước. Đặt tên các phần của bản nhạc theo bar và cho owner xem bản đồ cùng với storyboard. Hiệu ứng âm thanh và voice-over kèm caption nằm trong `references/sound-and-voice.md`.

### 5. Storyboard

Viết hai file dữ liệu. Cho mỗi shot một hình ảnh, một chuyển động theo nhạc, một chuyển động camera, một look, và transition dẫn vào nó; cho mỗi câu chữ một cách để đến được với người xem. Phá khuôn mẫu giữa các section, trừ khi lặp lại chính là ý tưởng. Một phim có nhân vật ghi beat của câu chuyện và cảm xúc vào `see`, cùng cỡ shot mà khuôn mặt cần (`references/characters-and-story.md`). Chạy bộ sinh; nó kiểm dữ liệu và ghi ra tài liệu, thời điểm của shot và các card. Mở studio: mọi shot phát dưới dạng một card cùng với nhạc. Owner duyệt ở đây. Một **story writer trên Opus mới nhất** có thể soạn nháp các section; lead gộp lại, kiểm và chịu trách nhiệm về dữ liệu.

### 6. Nền móng

Trên route engine, sao chép `assets/starter/` vào dự án, nếu giai đoạn 4 chưa làm, và làm theo README của nó; sau đó chỉnh kit cho hợp với bộ phim (bảng màu, kiểu chữ, vùng an toàn, overlay, và các định dạng mà phim được trình chiếu). Trong một phim có nhân vật, lead viết file cast và để owner duyệt một still của đội hình nhân vật trước bản mẫu. Trên route HyperFrames, dùng skill điểm vào của nó và đặt các công tắc cho telemetry và đăng nhập trước tiên. Chứng minh rằng capture bằng với lúc phát trên một shot thử trước bất kỳ shot thật nào.

### 7 và 8. Dựng

Viết hướng dẫn biên soạn (authoring guide) một lần. Giao brief cho một **builder trên Opus mới nhất** cho mỗi section, kèm các bar, shot, transition mà nó phải chừa chỗ hoặc tham gia, câu chữ, ranh giới nội dung, quy tắc thực hành, và báo cáo nó phải viết. Dựng section mẫu trước. Review mọi section bằng contact sheet và cut sheet, theo thứ tự này: nội dung, rồi bố cục và tay nghề, rồi trau chuốt. Gửi các điểm cần sửa lại cho chính builder đó kèm thời điểm, lý do và quyết định. Khi một shot mà owner đã xem được làm lại, nêu tên những hình ảnh phải được giữ lại.

### 9. Toàn bộ phim

Xem mọi cú cắt giữa các section, phần chuyển giao của tiêu đề, recap và end card; tinh chỉnh transition trên hình thật; đo thời gian frame; chạy trình duyệt của owner nếu nó khác trình duyệt dùng để capture. Sau đó báo owner rằng phim đã sẵn sàng và cần xem những gì.

### 10. Bàn giao

Khởi động studio cho owner, hoặc chỉ cho họ cách làm. Khi owner muốn một file để mở hoặc gửi đi mà không cần server, làm bản build single-file của phim hoàn chỉnh (`references/studio-viewer.md`). Nói rõ những gì đang mở. Ghi lại trạng thái: trong README của dự án, trong nhật ký quyết định của nó, và trong bộ nhớ của trợ lý. Dừng mọi server và agent không còn cần nữa.

## Tài liệu tham khảo

| File | Chứa |
|---|---|
| `references/environment.md` | Công cụ theo route, lệnh cài đặt theo hệ thống, khác biệt giữa các hệ thống, sao chép một dự án, trình duyệt của owner |
| `references/interview.md` | Quy tắc đặt câu hỏi, quyết định thuộc về ai, các vòng câu hỏi bằng tiếng Anh và tiếng Việt (kể cả tác phẩm ngắn và chất liệu thật), trang brief |
| `references/route-selection.md` | Engine so với HyperFrames so với kết hợp; các công cụ được nêu tên; yêu cầu nằm ngoài phương pháp; xung đột với quy tắc của owner |
| `references/hyperframes-route.md` | Họ skill HyperFrames, các lệnh, danh mục, giới hạn của nó, và cách giữ quy tắc của owner khi dùng nó |
| `references/hyperframes-facts.md` | Bảng dữ kiện đứng sau hai chương HyperFrames: yêu cầu, lệnh, bản đồ skill, danh mục, studio, các giới hạn đã nêu, kèm nguồn và phiên bản CLI lúc chúng được đọc |
| `references/thinking-and-brainstorm.md` | Nghiên cứu thứ có thật và nguồn của nó; từ một chủ đề đến hình ảnh; phép so sánh; hình dạng theo thời gian; các hướng đi; bản mẫu |
| `references/music-and-beat.md` | Nguồn, yêu cầu, lựa chọn, quy trình phân tích, kiểm grid, music map, đồng hồ của một shot |
| `references/storyboard.md` | Danh sách shot và câu chữ dưới dạng dữ liệu, schema của chúng, các bước kiểm, những gì được sinh ra, id của shot, animatic |
| `references/transitions.md` | Mô hình, ba phần của một drop, lựa chọn, sử dụng, một danh mục khoảng một trăm loại |
| `references/camera.md` | Cỡ shot, góc, ống kính, chuyển động, các mẫu bên trong một shot, quy tắc, lên kế hoạch cho một section |
| `references/art-styles.md` | Look theo nguồn gốc, công thức theo loại phim, vai trò màu sắc, phần hoàn thiện, giữ cho một phim nhiều look vẫn liền một khối |
| `references/effects.md` | Công việc của một hiệu ứng, chuyển động, giữ nhịp thời gian, sự xuất hiện, vẽ, chữ chuyển động, hạt và particle kit, ánh sáng, post chain và các look của nó, thiết bị và card trong không gian, goo và liquid glass, chi phí |
| `references/type-and-captions.md` | Ba cách cho một câu chữ, viết và ngắt dòng, giọng, vùng an toàn, cỡ chữ, thời gian để đọc, caption ở chân khung cho giọng đọc, CJK và dàn chữ dọc, variable font |
| `references/engine-architecture.md` | Hợp đồng (contract) của engine, các lớp, giao diện scene, các bề mặt vẽ, transition pass, post chain, công cụ capture |
| `references/studio-viewer.md` | Trang studio: yêu cầu, điều khiển, card, overlay, đồng hồ, export hook, trình duyệt, bàn giao |
| `references/orchestration.md` | Vai trò, quyền sở hữu file, hướng dẫn biên soạn, mẫu brief cho builder, vòng review, các vòng, model |
| `references/quality-gates.md` | Cổng kiểm, checklist theo giai đoạn, kiểm nội dung, look, khả năng đọc, đồng bộ, trình duyệt và hiệu năng, lỗi thường gặp, thế nào là "xong" |
| `references/short-pieces.md` | Làn ngắn, chế độ tự hành, công thức cho showreel, tác phẩm UI, launch, reward reveal, kinetic words, sting; loop, định dạng, tác phẩm phát khi bấm |
| `references/sound-and-voice.md` | Score và hiệu ứng âm thanh viết bằng code, voice-over và thời điểm từng từ, nhóm caption, ducking và độ lớn |
| `references/characters-and-story.md` | Thiết kế, rig và diễn xuất nhân vật bằng code, các chu kỳ, nhiều nhân vật, file cast dùng chung giữa các builder, nhân vật trong 3D, câu chuyện kể không lời, lỗi trong still |

## Script và asset

| Đường dẫn | Làm gì |
|---|---|
| `scripts/check-environment.mjs` | Kiểm tra hệ thống và công cụ cho một route; in ra lệnh cài đặt; không cài gì cả |
| `scripts/check-environment.sh`, `.ps1` | Khởi chạy trình kiểm tra khi không biết chắc có runtime JavaScript nào |
| `assets/starter/` | Một engine chung, kit, overlay, storyboard card, trang studio, công cụ capture, bộ sinh và phân tích nhạc, kèm một phim ví dụ nhỏ |

## Khi owner sửa bạn

| Owner nói | Làm |
|---|---|
| "Khoan đã", "Tôi chưa chốt cái đó" | Dừng ngay. Hỏi những gì đã được chốt |
| "Thêm ..." | Thêm vào. Đừng thay thế. Nếu không chắc: thêm vào, hay thay thế? |
| "Xấu quá", "lệch thiết kế" | So với shot tốt nhất trong section của nó; dựng lại theo ngôn ngữ hình ảnh đó |
| "Nó có thể bị hiểu nhầm là ..." | Lỗi nội dung. Viết lại storyboard cho shot đó; báo builder rằng lỗi nằm ở storyboard |
| "Tôi không thấy nó" | Đọc lỗi trên trình duyệt của owner trước khi trả lời |
| "Bản trước tốt hơn" | Tìm ra cái đã bị mất; mang nó trở lại; lần sau nêu tên nó trong brief |
