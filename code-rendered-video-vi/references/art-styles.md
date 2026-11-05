# Phong cách hình ảnh (Art styles)

Một danh mục các look mà code có thể vẽ, nhóm theo nguồn gốc, kèm theo mỗi look hợp với gì và tốn kém ra sao. Nó cũng nêu vài thứ mà một phim phải giữ cố định để có thể thay đổi mọi thứ còn lại, và các công thức theo từng loại phim.

Đọc file này khi: viết treatment, chọn ngôn ngữ hình ảnh (idiom) cho từng phần trong storyboard, brief cho một builder về look của một phần, hoặc đánh giá một shot có "lạc thiết kế" (out of design) hay không.

## 1. Phong cách vận hành thế nào trong phương pháp này

| Nguyên tắc | Nghĩa là |
|---|---|
| Khóa ít, thả phần còn lại | Một phim được giữ liền mạch nhờ vài quy tắc cố định, không phải nhờ một phong cách duy nhất. Ba quy tắc là đủ: vai trò của một màu, chỗ chữ được phép đứng, và việc các sự kiện rơi đúng beat |
| Mượn một idiom | Mỗi phần mượn look của một thứ có thật: một ấn phẩm in, một cỗ máy, một chất liệu. Rồi nó dựng look đó bằng những phương tiện mà bản gốc chưa từng có (chiều sâu, ánh sáng, camera bay, shader) |
| Idiom thuộc về chủ đề | Một chủ đề có loại giấy của riêng nó. Bếp có phiếu gọi món, tòa nhà có bản vẽ kỹ thuật (blueprint), chuyến đi có bản đồ và vé. Một idiom lấy từ thế giới của chủ đề đã giải thích trước khi người xem đọc một chữ nào |
| Một màu nghĩa là một thứ | Màu tín hiệu (signal) đánh dấu thứ CHÍNH LÀ ý tưởng của phần đó, và không gì khác. Một shot về vấn đề thì không có màu tín hiệu trong đó |
| Vẽ thì hơn để trơn | Một cái hộp trơn, một hình người không đặc điểm, một tấm phẳng là đồ giữ chỗ (placeholder), không phải một bức hình. Mọi bề mặt người xem thấy đều được vẽ: độ dày nét, gạch bóng, texture, chữ |
| Sáng và tối luân phiên | Nền luân phiên giữa sáng và tối từ shot này sang shot khác, để mắt được đánh thức ở mỗi cú cắt |
| Chủ sở hữu có thể cấm một phong cách duy nhất | Nếu chủ sở hữu nói "đừng khóa một phong cách", hãy hiểu theo nghĩa đen: mỗi phần có idiom riêng, và các hằng số ở trên gánh sự thống nhất |

Từ thực tế: look của bộ phim tham khảo mà chủ sở hữu ngưỡng mộ được chính chủ sở hữu mô tả là "retro trộn với hiện đại". Đó chính là nguyên tắc thứ hai. Nó không có style guide nào ngoài một palette và hai typeface; mỗi cảnh mượn look của một ấn phẩm in cũ khác nhau.

## 2. Lựa chọn

1. **Viết ra thế giới của chủ đề.** Những đồ vật, giấy tờ, màn hình và địa điểm nào thuộc về nó? Liệt kê mười thứ. Đó là các ứng viên.
2. **Chốt tông.** Nghiêm túc hay vui nhộn, ấm hay lạnh, ồn ào hay yên tĩnh, cho ai. Tông sẽ loại bỏ một nửa số ứng viên.
3. **Cho mỗi phần một idiom** từ những gì còn lại, và không idiom nào dùng cho hai phần.
4. **Đặt các idiom cạnh nhau mà so.** Hai phần dùng cùng một đạo cụ (vé, màn hình cửa hàng, điện thoại) sẽ bị nhầm với nhau. Đổi một trong hai.
5. **Kiểm tra chi phí.** Một look cần shader khúc xạ hay mô phỏng thì đáng dùng cho shot chủ đạo (hero) của phim, không phải cho một shot lướt qua.
6. **Kiểm tra khung hình.** Khung dọc cần chủ thể cao và bố cục xếp chồng. Một look làm từ các toàn cảnh rộng sẽ chống lại nó.
7. **Dựng một phần làm mẫu** và cho chủ sở hữu xem trước khi dựng phần còn lại.

## 3. Danh mục

Các cột: **Dựng bằng** nêu bề mặt vẽ: một layer canvas 2D, line batch trên GPU, một shader toàn màn hình, một cảnh 3D, hoặc chính trang web (HTML, CSS, SVG: route HyperFrames). **Chuyển động kiểu** là kiểu chuyển động mà look đó đòi hỏi.

### 3.1 Giấy và in ấn

| Phong cách | Trông như | Dựng bằng | Chuyển động kiểu | Hợp với | Lưu ý |
|---|---|---|---|---|---|
| Blueprint (bản vẽ kỹ thuật) | Nét nhạt trên nền xanh đậm hoặc xanh mòng két tối, lưới, đường kích thước, khung tên, tên phòng viết hoa | Layer 2D hoặc line batch; gạch bóng ở chỗ tường bị cắt | Các nét tự vẽ ra; các phòng lần lượt sáng lên; camera lướt trên tờ giấy | Tòa nhà, hệ thống, hạ tầng, mọi thứ "như đã xây" | Nét mảnh như sợi tóc biến mất trên điện thoại. Dùng độ dày nét: dày cho tường bị cắt, mảnh cho đồ nội thất |
| Bản khắc bằng sáng chế | Đổ bóng bằng nét gạch đi theo ánh sáng, đường dẫn tới các nhãn số nhỏ, "FIG. 3" | Shader khắc một vật 3D, hoặc 2D có gạch bóng | Bàn xoay, hình cắt, các bộ phận tách rời | Cơ cấu, thiết bị, đầu nối, phần cứng | Nét gạch co giãn theo vật sẽ tạo moiré. Giữ bước nét cố định trên màn hình |
| Risograph | Hai hoặc ba màu pha (spot colour), hơi lệch chồng màu, lưới chấm thô | Shader halftone, blend multiply | Các lớp màu trượt vào khớp chồng | Văn hóa, thời trang, explainer vui nhộn | Bước chấm so với độ phân giải; multiply trong ánh sáng tuyến tính tối hơn dự kiến |
| Poster chữ gỗ | Chữ slab khổng lồ, mực không đều, hai màu | Layer 2D với texture mực | Các từ được đóng dấu, mỗi beat một từ | Tuyên bố, tiêu đề, tóm tắt | Chữ lớn hơn frame vẫn phải đọc được |
| Báo chí, biên tập | Các cột, một tiêu đề, một trích dẫn nổi bật, một ảnh halftone | Layer 2D hoặc trang web | Camera đi xuống theo một cột; các tiêu đề thay thế nhau | Tin tức, lịch sử, báo chí dữ liệu | Quá nhiều chữ nhỏ |
| Hóa đơn in nhiệt | Chữ dot-matrix trên một dải giấy có mép xé | Layer 2D, một font dạng chấm | Dải giấy in từng dòng rồi bị xé | Cửa hàng, đơn hàng, log, mọi thứ được đếm | Dấu tiếng Việt bị vỡ trong font chấm thô. Dùng chấm lớn hơn hoặc font khác cho từ có dấu |
| Vé, thẻ đục lỗ | Đường đục lỗ, lỗ bấm, cuống vé, con dấu | Layer 2D | Bấm lỗ theo beat; trượt vào khe | Lựa chọn, tùy chọn, quyền truy cập, du lịch | Nhãn nhỏ |
| Phiếu đặt hàng, phiếu ghi | Các bước in sẵn, ô để tick, một trường cho mỗi lựa chọn | Layer 2D | Một điểm đánh dấu di chuyển từ bước này sang bước khác; các ô được điền theo beat | Quy trình, cấu hình, mọi thứ được tạo từ các lựa chọn | Phiếu phải đọc được khi camera di chuyển |
| Rập may | Đường cắt đứt nét, khấc, mũi tên canh sợi trên giấy lụa | Layer 2D, nền vải dệt | Các mảnh được cắt ra và ráp lại | Bộ, vừa vặn, template, thời trang | |
| Sách hướng dẫn lắp ráp | Hình tách lớp, các bước đánh số trong vòng tròn, mũi tên chỉ hướng lắp | Cảnh 3D có đường viền, hoặc 2D | Các bộ phận tách ra dọc một trục rồi ghép lại | Các lớp, cách một thứ được ráp lại | Mũi tên và số trong vòng tròn không có trong hầu hết typeface: hãy vẽ chúng |
| Bản đồ gấp | Đường sá, công viên, ghim A và B, chú giải, nếp gấp | Layer 2D; lộ trình là các đường phát sáng | Lộ trình vẽ từ A tới B; camera bay qua | Hành trình, chọn giữa các con đường, mạng lưới | Bản đồ thì rộng. Trong khung dọc hãy xoay hoặc crop nó |
| Sổ cái, giấy kẻ ô | Dòng kẻ, chữ số viết tay, lề | Layer 2D | Các con số được viết, gạch bỏ, cộng tổng | Tiền bạc, thí nghiệm, số học | |
| Con dấu, triện | Một con dấu tròn hoặc vuông, mực không đều ở mép | Layer 2D | Đập xuống theo beat, kèm một cú giật | Một điểm nhấn: đã duyệt, xong, bị từ chối | Tối đa một cái mỗi shot |
| Giấy cắt, cắt dán (collage) | Các lớp giấy với bóng đổ cứng | Layer 2D có drop shadow, hoặc mặt phẳng 3D | Các mảnh trượt và rơi; nảy nhẹ | Trẻ em, câu chuyện, explainer thân thiện | Mọi bóng đổ phải cùng một hướng |
| Sách pop-up | Các mặt phẳng gấp dựng đứng lên từ trang sách | Mặt phẳng 3D | Trang mở ra và cảnh dựng lên | Câu chuyện, thế giới nhỏ | |
| Zine, bản photocopy | Tương phản gắt, nhiễu mực, mép xé, băng dính | Layer 2D với threshold và noise | Jump cut, frame rung | Âm nhạc, biểu tình, phản văn hóa | |
| Tranh khắc gỗ | Các mảng đen đậm cắt bởi nét trắng | Layer 2D | Hé lộ chậm, đóng dấu nặng | Văn hóa dân gian, lịch sử, tuyên bố mạnh | |
| Bảng đen | Nét phấn trên nền xanh lá đậm, vết lem, vết lau | Layer 2D với nét thô | Viết tay; lau đi | Dạy học, công thức nấu ăn, toán học | |
| Bảng trắng | Nét bút lông, mũi tên, bút dạ quang | Layer 2D | Vẽ nhanh, khoanh tròn, gạch chân | Lập kế hoạch, explainer cho start-up | Trông như một explainer đại trà nếu không làm gì thêm |
| Ghi chú trên bảng | Giấy nhớ, ghim, dây | Layer 2D | Các ghi chú được chuyển giữa các cột | Lập kế hoạch, ý tưởng, phân loại | |
| Thẻ bài | Bài tây, flash card, thẻ chỉ mục | Layer 2D hoặc mặt phẳng 3D | Chia bài, lật, xòe | Lựa chọn, so sánh, câu đố | |

### 3.2 Vẽ và minh họa

| Phong cách | Trông như | Dựng bằng | Chuyển động kiểu | Hợp với | Lưu ý |
|---|---|---|---|---|---|
| Monoline | Một độ dày nét đều, tô phẳng | Layer 2D, SVG | Nét vẽ ra; hình bật lên | Explainer doanh nghiệp thân thiện | Chung chung nếu không có ý tưởng riêng |
| Hình phẳng (flat shapes) | Hình tô màu không viền | Layer 2D, SVG | Hình trượt và co giãn | Sản phẩm, dịch vụ | Look của hàng nghìn video template |
| Isometric | Lưới 30 độ, những thế giới nhỏ nhìn từ trên xuống | Layer 2D trên lưới isometric, hoặc 3D với camera trực giao (orthographic) | Đồ vật di chuyển dọc lưới; các khối mọc lên | Hệ thống, logistics, thành phố, hạ tầng | Chữ trên mặt phẳng isometric khó đọc: giữ nhãn phẳng |
| Axonometric, mặt cắt kiến trúc | Tường có độ dày, hoa văn sàn, cung mở cửa, nội thất, hình người | Layer 2D với phép chiếu, hoặc line batch | Xoay chậm; nghiêng phẳng thành mặt bằng | Hộ gia đình, văn phòng, ai ở đâu | Không loại bỏ nét khuất thì các thứ nhìn xuyên qua nhau |
| Nét rung (boiling line) | Nét vẽ tay được vẽ lại mỗi hai hoặc ba frame | Layer 2D với jitter có seed, nhảy bậc theo thời gian | Sống động ngay cả khi đứng yên | Phim ấm áp, mang tính cá nhân | Jitter phải được seed từ số thứ tự frame, không bao giờ ngẫu nhiên |
| Mực và màu nước loang | Mép mềm loang ra, vân giấy | Shader hoặc 2D nhiều lớp | Màu lan ra từ một điểm | Thiên nhiên, cảm xúc, câu chuyện | Tốn công để làm cho thuyết phục |
| Bóng đen (silhouette) | Hình đen trên nền sáng | Layer 2D | Hình người đứng dậy, giơ tay, bước đi | Đám đông, kịch tính, người không mặt | Một silhouette là hình người duy nhất trong một cảnh vẽ trông như chưa hoàn thiện |
| Hình người tô đặc | Các thân hình đơn giản, mỗi người một tư thế, cả một gia đình hình như vậy | Layer 2D | Cử chỉ nhỏ theo beat | Bất kỳ shot nào có người | Vẽ chúng một lần, trong một file, và dùng ở mọi nơi |
| Pictogram | Một icon lặp lại để thể hiện số lượng | Layer 2D | Các icon điền vào từng hàng | Thống kê | |
| Truyện tranh (comic) | Khung tranh, đường tốc độ, halftone, impact frame, bong bóng thoại | Layer 2D, shader halftone | Khung tranh đập vào; impact frame ở dạng âm bản | Hành động, hài hước, xung đột | |
| Hoạt hình (cartoon) | Hình tròn trịa, nặng, viền tối một màu, tô phẳng với một bậc bóng, mắt to | Layer 2D với rig (`characters-and-story.md`), hoặc cảnh 3D với toon shading | Squash and stretch, anticipation, overshoot, hold | Câu chuyện, mascot, hé lộ phần thưởng, trẻ em | Mỗi nhân vật một khuôn mặt riêng. Nền tối dưới viền tối sẽ làm mất viền: cho nhân vật một viền sáng (rim) |
| Anime, cel | Nét sạch với độ dày thay đổi, bóng cel hai tông có mép cứng, mắt to có điểm sáng, đường tốc độ, bầu trời kịch tính | Layer 2D với rig; nền vẽ bằng gradient; hoặc cảnh 3D với toon shading và một pass viền | Tư thế giữ lâu, chuyển động nhanh bất ngờ có vệt nhòe, impact frame, camera lia qua một ảnh tĩnh | Trailer, cảnh đánh nhau, kịch tính | Khuôn mặt vẽ bằng code trông cứng cạnh anime vẽ tay. Giữ ít khuôn mặt và vẽ lớn; để tư thế, hiệu ứng và camera gánh hành động |
| Người que (stick figures) | Một nét đậm cho mỗi chi, đầu tròn | Layer 2D với rig | Tư thế hành động lớn, rõ ràng; vệt nhòe; impact frame | Đánh nhau, trận chiến, hài, explainer nhanh | Người que không có silhouette riêng: mọi tư thế phải đọc được chỉ qua các chi |
| Stop-motion vẽ tay | Một hình vẽ thay đổi mỗi hai hoặc ba frame, vân giấy, độ lắc làm bằng tay | Layer 2D, tư thế nhảy bậc theo đồng hồ frame, nét rung | Nhảy bậc: 8 đến 12 tư thế mỗi giây | Câu chuyện cá nhân, explainer ngôi thứ nhất | Các bậc phải lấy từ đồng hồ frame, không bao giờ từ thời gian bài hát |
| Hoạt họa cát | Cát nhạt trên bàn kính được chiếu sáng, hoặc cát tối trên nền sáng; các hình được xóa đi và lớn dần thành hình tiếp theo | Shader toàn màn hình cho hạt cát và ánh sáng xuyên qua; các hình là mask vẽ trên layer 2D rồi blur | Hình này thành hình kia bằng cách xóa, rắc và cào nét, không bao giờ bằng cú cắt | Lịch sử, truyền thuyết, một cuộc đời kể trong một dòng chảy | Bản chất là chậm. Phim dài cần một câu chuyện chảy từ hình này sang hình khác. Xem mục 3.8 |
| Nét cọ hội họa | Các nét sơn ngắn dày đi theo hình khối và dòng chảy của cảnh, như bầu trời của Van Gogh | Hàng nghìn nét ngắn trong một line batch (`src/engine/lines.ts`), mỗi nét đặt trên một lưới có seed, xoay theo một trường dòng chảy (flow field) và lấy màu từ hình bên dưới; hoặc một pass toàn màn hình làm nhòe hình dọc theo dòng chảy. Xem mục 3.8 | Các nét trôi chậm dọc trường; rung theo bậc hai frame | Giấc mơ, lịch sử nghệ thuật, thiên nhiên, cảm xúc | Nét cùng một cỡ trông như một filter. Nét lớn trên trời, nét nhỏ trên chủ thể |
| Bút chì, graphite | Nét xám với vân giấy lộ qua, gạch bóng trong vùng tối, nét dựng hình | Layer 2D trên nền giấy; nét được jitter và bị vân giấy làm đứt; gạch bóng trong vùng tối (hàm `hatch` của thư viện shader trong `src/engine/glsl/common.ts`) | Vẽ ra, rồi đánh bóng; nét rung nhẹ | Phác thảo, ý tưởng, kế hoạch, sổ tay họa sĩ | Xám thuần trên trắng trông như wireframe. Thay đổi lực nhấn dọc mọi nét |
| Bút bi | Nét xanh gạch chéo dày đặc, thấy rõ lực nhấn, trang giấy có dòng kẻ | Layer 2D; nhiều nét mảnh hơi lắc; tối hơn ở chỗ giao nhau | Gạch dần theo beat, lớp này đến lớp khác | Trường học, ghi chú, vẽ nguệch ngoạc bên lề | Gạch dày đặc là rất nhiều nét: dùng line batch khi chúng lên tới hàng nghìn |
| Sáp màu và bút dạ | Màu sáp bị vân giấy làm đứt; bút dạ phẳng và tươi, tối hơn ở chỗ hai nét chồng nhau; tranh trẻ con vẽ | Layer 2D; sáp màu là một mảng tô bị mask bởi noise giấy với mép thô, bút dạ là nét phẳng composite bằng `multiply` để chỗ chồng tối đi | Vẽ nguệch ngoạc ra; nhảy bậc hai frame | Trẻ em, truyền hình thiếu nhi, hài hước, "làm bằng tay" | Giữ nét vẽ ngây ngô nhưng bố cục phải có thiết kế |
| Nét run, chữ mập | Nét vẽ tay lượn run, chữ tròn lớn có bóng lệch cứng màu thứ hai | Nét rung cho hình vẽ; chữ đặt bằng giọng display, với một bản sao dịch vài px phía sau ở màu bóng | Mọi thứ rung theo bậc hai frame; các từ bật lên có nảy | Explainer thân thiện, nội dung mạng xã hội, thương hiệu có giọng vui nhộn | Bóng lệch phải rơi về một hướng cho cả phim |
| Rối giấy cắt | Hình người cắt từ giấy hoặc ảnh, ghim ở các khớp, chuyển động bậc hai frame, trên phông nền in | Rig (`src/scenes/parts/kit-rig.ts`) với ảnh hoặc hình giấy làm bộ phận; tư thế nhảy bậc theo đồng hồ frame | Chuyển động khớp bản lề giật cục, thứ lớn bất ngờ xuất hiện từ ngoài khung | Châm biếm, lịch sử, hài siêu thực | Chuyển động mượt sẽ giết look này: hãy cho nó nhảy bậc |
| Múa rối bóng | Rối đen trên que phía sau một màn sáng, ánh sáng ấm xuyên qua màn, mép mềm khi rối rời khỏi màn | Bộ phận rig vẽ đen; blur tăng theo khoảng cách tới màn (vẽ rối ở xa trên một layer có backing scale thấp hơn) | Rối lướt và xoay; ánh sáng chập chờn | Truyện dân gian, truyền thuyết, câu chuyện tĩnh lặng | Giữ lại các que: chúng làm nên sân khấu |
| Xử lý kiểu manga | Đen trắng, screen tone, đường tốc độ, mực bắn, hiệu ứng âm thanh viết bằng katakana (ドドド), bong bóng thoại | Layer 2D; threshold hình về đen trắng, tông chấm từ halftone của nền, chữ vẽ thành các hình lớn | Đóng băng khi va chạm, đường tốc độ phía sau chủ thể, một hiệu ứng âm thanh đập vào | Hành động, kịch tính, nhại | Katakana cần một font có các glyph đó. Kiểm tra font của phim có glyph trước khi thiết kế dựa trên chúng |
| Tableau pastel đối xứng | Bố cục canh giữa nhìn chính diện phẳng, màu pastel, mọi thứ đặt như trên sân khấu | Layer 2D hoặc camera 3D trực giao, bố cục trên một đường trục giữa | Chuyển động thẳng dọc các trục, whip pan giữa các tableau, giữ yên tỉnh bơ | Câu chuyện, thương hiệu độc lạ, các chương của một danh sách | Đối xứng phải chính xác; một sai lệch nhỏ trông như lỗi |
| Giấy cắt có ánh sáng | Các lớp giấy cắt ở các độ sâu, các tia sáng xuyên qua khe (god rays), các đốm sáng mất nét phía trước (bokeh) | Các layer 2D xếp chồng có drop shadow; tia sáng là các hình nêm mềm cộng thêm ánh sáng; bokeh là các đĩa mềm trên một layer có backing scale thấp | Parallax chậm khi camera trượt; bụi trong tia sáng | Sách truyện, lễ hội, explainer cao cấp | Giấy phải vẫn là giấy: tia sáng và bokeh là ánh sáng cộng thêm, không bao giờ đè lên mép giấy |
| Sticker | Viền nhạt dày và một drop shadow quanh mỗi thứ | Layer 2D | Mọi thứ tiếp đất có nảy | Tiêu đề, phim mạng xã hội, icon của phần tóm tắt | |
| Hình cắt (cut-away) | Một vật bị cắt đôi, bên trong tô bằng đường mặt cắt | Layer 2D | Vết cắt mở ra; bên trong lần lượt được tô màu từng phần | Bên trong một cỗ máy | Người xem tin hình vẽ theo nghĩa đen: đừng vẽ những gì sai so với thực tế |
| Sơ đồ | Hộp, đường nối, nhãn, được cho chiều sâu và trọng lượng | Layer 2D hoặc 3D nhẹ | Các bộ phận trượt vào và ra; đường nối định hình lại | Shot "trong app của bạn" của một explainer | Nhỏ và phẳng thì trông như một slide. Cho nó lấp đầy frame và để một chuyện xảy ra |

### 3.3 Màn hình và máy móc

| Phong cách | Trông như | Dựng bằng | Chuyển động kiểu | Hợp với | Lưu ý |
|---|---|---|---|---|---|
| Terminal | Chữ monospace xanh lá hoặc hổ phách trên nền đen, con trỏ, scanline | Layer 2D, scanline ở post | Gõ ra, cuộn | Developer, log | Code trên màn hình làm mất người xem không đọc code |
| Tivi, băng từ | Kính cong, scanline, lỗi tracking, màu lem | Post chain | Cuộn, xé, tắt thành một chấm | Hoài niệm, phát lại | |
| Radar, máy hiện sóng | Một đường quét trên lưới tròn, các đốm, phosphor mờ dần | Shader hoặc line batch | Đường quét xoay theo ô nhịp; các đốm sáng khi nó đi qua | Phát sóng, người đăng ký, phát hiện, giám sát | |
| Bảng lật, màn hình chấm | Chữ split-flap, chấm lật, chữ số bảy đoạn | Layer 2D | Các chữ cái lách cách xoay tới từ đích | Menu, bảng giờ, bộ đếm, tên | |
| Màn hình máy tính đời đầu | Đồ họa một bit, cửa sổ có gờ vát | Layer 2D | Cửa sổ mở ra với hiệu ứng zoom các đường viền | Lịch sử máy tính, hài hước | |
| Pixel art | Pixel lớn trên một lưới, palette 16 đến 32 màu, không có mép mềm ở bất cứ đâu | Một canvas nhỏ ở độ phân giải riêng của tác phẩm, đặt lên frame với tỉ lệ số nguyên: `PixelLayer` trong `src/scenes/parts/kit-pixel.ts` | Nhảy bậc: 8 đến 12 tư thế mỗi giây trong khi phim chạy ở frame rate của nó | Game, retro, nhân vật nhỏ, một phù thủy niệm phép | Bất kỳ mép mềm, xoay tự do, bloom hay grain nào cũng phá lưới. Xem mục 3.8 |
| Vector arcade | Nét mảnh phát sáng trên nền đen | Line batch với bloom | Nhanh, xoay | Âm nhạc, vũ trụ, phim tối giản | |
| Màn hình thiết bị đo | Nét mảnh, ngoặc, số đọc | Line batch, layer 2D | Ngoặc khóa mục tiêu; số nhảy | Phân tích, máy móc biết nhìn; HUD của showreel (bên dưới) | Trang trí không có nghĩa. Mỗi số đọc nên nói một điều có thật |
| HUD của showreel | Timecode chạy, bộ đếm frame, "120 BPM · 60 FPS", dấu crop ở các góc, nhãn chương "04 / 07", một thanh tiến trình mảnh | Layer 2D, thường ở overlay (`src/scenes/overlay.ts`), bằng giọng máy móc; mọi giá trị tính từ đồng hồ frame và dữ liệu của phim | Các giá trị chạy theo phim; chương đổi ở cú cắt | Showreel, tác phẩm motion nói về chính quá trình làm ra nó, các buổi ra mắt kỹ thuật | Được phép như một hệ thống có thiết kế với các giá trị có thật và chạy theo phim. Là lỗi khi nó chỉ để trang trí, sai, hoặc đặt ở các góc để lấp chỗ, và bị bỏ khi chủ sở hữu hoặc prompt cấm nó |
| CRT và demoscene | Kính cong, scanline, phosphor phát sáng; raster bar màu, một dải chữ xoắn, font bitmap, trường sao, dòng chào chạy cuộn | Shader toàn màn hình cho các bar, twister và sao; layer 2D cho font bitmap (hoặc `kit-pixel.ts` ở độ phân giải thấp); độ cong và scanline là một pass post (xem `effects.md`) | Mọi thứ theo sóng sin trên beat; dòng chạy chữ không bao giờ dừng | Máy tính retro, âm nhạc, gợi nhắc thập niên 1990 | Độ cong màn hình làm cong vùng an toàn (safe area): giữ chữ tránh xa các góc |
| Hệ thống chữ của phim ra mắt | Nền trắng ngà, tiêu đề sans với một từ serif nghiêng màu nhấn, một eyebrow mono nhỏ có dấu chấm, các phần đánh số ("02 —"), thẻ có bóng mềm lớn, cửa sổ trình duyệt có ba chấm | Layer 2D; ba giọng chữ của `src/scenes/parts/kit-type.ts` được gán font của thương hiệu; bóng là các hình tối đã blur dưới thẻ | Chữ trồi lên từ một mask, thẻ vào so le, một điểm nhấn chuyển động | Ra mắt SaaS và công cụ cho developer. Cấu trúc của một tác phẩm như vậy nằm trong `short-pieces.md`, mục 7.3 | Look phổ biến nhất của thể loại: trông như template trừ khi màn hình và lời lẽ riêng của sản phẩm lấp đầy nó |
| Motion design nói về motion design | Trình chỉnh đường cong easing với các tay nắm, timeline keyframe với các hình thoi và playhead, chú thích viết tay có mũi tên ("stagger: 45 ms"), thanh trượt trước và sau | Layer 2D; các đường cong vẽ từ chính các ease trong `src/engine/util.ts`, để đường cong hiển thị chính là chuyển động nhìn thấy | Playhead chạy theo phim; thứ được chú thích chuyển động đúng như đường cong của nó nói | Showreel của một motion designer, explainer về animation | Ở đây chú thích là nội dung: chúng phải đúng với những gì đang chuyển động |
| HUD game | Thanh máu, bản đồ nhỏ, hotbar, đồng hồ, điểm số, màn hình kết quả | Layer 2D phủ lên cảnh | Số nhảy, thanh cạn dần, một banner đập vào | Trailer game, nhại, hé lộ phần thưởng | Bản thân một game không phải là phim của phương pháp này (`route-selection.md`); trailer của nó thì phải |
| VHS phủ anime | Một ảnh tĩnh anime hoặc cảnh cel với scanline, màu lem sang ngang, một dải nhiễu tracking, một dấu thời gian | Hình trên một layer; lỗi băng là một pass post (xem `effects.md`) | Hình giữ yên; băng lắc và xé trên tiếng snare | Hoài niệm, nhạc lo-fi, meme | Hình bên dưới phải tốt: băng chỉ là gia vị |
| Màn hình app | Thẻ, nút, công tắc, thanh trạng thái, khung thiết bị | Layer 2D hoặc trang web | Một ngón tay hoặc con trỏ nhấn; màn hình đáp lại | Shot "trong app của bạn"; demo sản phẩm | Hai phần cùng dùng màn hình cửa hàng sẽ bị nhầm |
| Dashboard | Biểu đồ, con số lớn, small multiples | Layer 2D hoặc trang web | Thanh lớn dần, số đếm lên | Kinh doanh, kết quả | |
| Trình soạn code | Cú pháp tô màu, số dòng | Layer 2D hoặc trang web | Gõ ra; dòng được highlight | Chỉ cho developer | |
| Đồ thị node, mạch điện | Hộp và dây, xung chạy dọc dây | Line batch | Xung chạy theo beat | Luồng dữ liệu, pipeline | Một xung rời một node tới nhiều node là hình ảnh của thông báo: chỉ dùng khi đó là ý muốn nói |
| Lưới neon | Một lưới phát sáng tới chân trời, mặt trời, chrome | Shader | Di chuyển tới trước bất tận | Nhạc kiểu thập niên 1980 | Sáo mòn; dùng kèm một cú twist |
| Text mode | Ký tự làm pixel | Layer 2D | Ký tự thay đổi để tạo thành hình | Developer, retro | |

### 3.4 Ánh sáng và chất liệu

| Phong cách | Trông như | Dựng bằng | Chuyển động kiểu | Hợp với | Lưu ý |
|---|---|---|---|---|---|
| Đường phát sáng | Các đường mang ánh sáng trên nền tối | Line batch, bloom | Vẽ ra; đập nhịp theo kick | Mạng lưới, tín hiệu, năng lượng, lộ trình | Chữ không bao giờ được phát sáng. Ánh sáng cộng thêm không được đẩy alpha vượt quá một |
| Low-poly | Khối nhiều mặt, đổ bóng phẳng | Cảnh 3D | Quỹ đạo chậm | Phong cảnh, đồ vật đơn giản | |
| Đất sét (clay) | Khối tròn trịa, bóng mềm | Cảnh 3D | Squash and stretch | Sản phẩm thân thiện, phim vui nhộn | |
| Diorama đất sét trên bệ | Một thế giới isometric nhỏ gồm các vật bằng đất sét tròn trịa đứng trên một bệ tròn hoặc vuông, ánh sáng mềm, một nhãn giá hoặc thẻ nhãn bên cạnh | Cảnh 3D với camera trực giao ở góc isometric; chất liệu thô với ánh sáng chính (key) ấm và ánh sáng phụ (fill) lạnh; một bóng tiếp xúc mềm dưới mỗi vật; nhãn trên layer 2D | Các vật bật lên từ bệ có squash; bệ xoay nhẹ | Sản phẩm, dịch vụ, "nó hoạt động thế nào" trong một hình, quảng cáo dọc | Bệ phải đứng trên thứ gì đó: cho nó một bóng trên mặt đất |
| Kính | Khúc xạ, blur những gì phía sau | Shader | Xoay chậm để thấy sự bẻ cong | Sản phẩm cao cấp, màn hình hiện đại | Tốn kém. Chỉ dành cho hero |
| Kính lỏng và goo | Tấm kính bẻ cong những gì phía sau với mép có màu; các khối nhầy hợp lại và tách ra như chất lỏng; một giọt trở thành thanh công cụ | Một pass post hoặc pass layer khúc xạ từ distance field của một hình, và một pass blur-và-threshold cho goo: xem `effects.md` | Các khối hợp lại theo beat; một tấm trượt và thế giới uốn cong bên dưới | Giao diện hiện đại, tác phẩm ra mắt, transition vui nhộn | Khúc xạ một nền rối là nhiễu; đặt thứ gì đó đơn giản và sáng phía sau kính |
| Bình nhìn xuyên | Một chiếc cốc hoặc chai thấy được bên trong | Cảnh 3D với chất liệu trong suốt | Rót đầy, đổ | Đồ ăn, thức uống, bình chứa | Vật đặc bên trong vật trong suốt bị ẩn trừ khi cũng được đánh dấu trong suốt và sắp xếp thứ tự |
| Toon | Màu phẳng ba hoặc bốn bậc, viền tối, ánh sáng viền (rim light) | Cảnh 3D, chất liệu toon, pass viền (mục 3.8) | Dứt khoát; squash and stretch; overshoot | Đồ vật và nhân vật mang cảm giác truyện tranh, hé lộ phần thưởng, mascot | Viền vẽ từ mặt sau (back faces) không đều và đứt ở các góc |
| Matcap | Một quả cầu ánh sáng bọc lên mọi bề mặt | Cảnh 3D | Bất kỳ | Một look cao cấp nhanh gọn | |
| Khối hộp | Các khối lập phương | Cảnh 3D, instancing | Xếp chồng, xây dựng | Xây dựng, dữ liệu dạng khối | |
| Đám mây điểm (point cloud) | Hàng nghìn điểm tạo thành một hình | Instanced points | Ráp lại, tản ra | Dữ liệu, bộ nhớ, machine learning | |
| Wireframe | Chỉ có cạnh | Line batch | Xoay; từ khung dây thành khối đặc | Kỹ thuật, trước và sau | |
| Studio sản phẩm | Bàn xoay, phản chiếu mềm | Cảnh 3D | Một vòng quỹ đạo trọn vẹn rồi dừng phắt | Hero của một phim sản phẩm | |
| Tiểu cảnh (miniature) | Một thế giới nhỏ với độ sâu trường ảnh nông | Cảnh 3D, blur theo độ sâu | Di chuyển chậm | Thành phố, logistics | |
| Thế giới ray-marched | Các hình bất tận từ distance function | Shader | Bay | Hành trình trừu tượng, đường hầm, tỉ lệ | Nặng nhất trên card đồ họa |
| Ánh sáng và sương mù | Chùm sáng, sương | Shader | Chậm | Hé lộ, kịch tính | |
| Thế giới 3D cách điệu | Phong cảnh kiểu hội họa hoặc cel-shaded: bầu trời lớn có mây, đồi mờ dần vào sương, nước phản chiếu bầu trời, cỏ lay trong gió, ánh sáng của một giờ trong ngày | `Sky` của `src/scenes/parts/kit-ground.ts` cho trời, mặt trời, mây và nước ở 2D; đồi và cây trên các layer tô bằng `hazed`; hoặc một cảnh three.js với sương mù và vòm trời (sky dome). Xem mục 3.8 | Camera trôi chậm, mây trôi, giờ trong ngày chuyển dần | Câu chuyện, trailer game, tác phẩm tĩnh lặng, các mùa | Một thế giới không có sương trông phẳng và nhỏ. Mỗi layer ở xa hơn càng gần màu chân trời |
| Chân thực (photoreal) và vật lý (physically based) | Kim loại, kính, nước và da được chiếu sáng như thật, bóng mềm, độ sâu trường ảnh, tia sáng | three.js với chất liệu physically based, ánh sáng môi trường, sương mù, blur theo độ sâu, tia sáng là một pass post | Chậm và nặng, như một camera thật | Kiến trúc, sản phẩm, thiên nhiên | Engine tiến gần tới nó nhưng không đạt được. Nó tốn nhiều thời gian và sức mạnh đồ họa nhất trong mọi look, và một chất liệu sai là lộ ngay. Photoreal thật sự thuộc về một bộ công cụ 3D (`route-selection.md`). Hãy nói rõ với chủ sở hữu, và đề xuất một phiên bản cách điệu mà code làm tốt |

### 3.5 Tạo sinh (generative) và trừu tượng

| Phong cách | Trông như | Dựng bằng | Hợp với |
|---|---|---|---|
| Trường dòng chảy (flow field) | Hàng nghìn đường đi theo một dòng chảy vô hình | Line batch | Giao thông, gió, dòng dữ liệu |
| Giao thoa | Sóng từ nhiều nguồn chồng lên nhau thành moiré | Shader | Tín hiệu nhiễu loạn lẫn nhau, nhiễu, xung đột |
| Sinh trưởng | Các nhánh mọc theo quy tắc | Layer 2D, line batch | Mở rộng quy mô, lan rộng, thay đổi hữu cơ |
| Bầy đàn (swarm) | Nhiều tác tử nhỏ di chuyển cùng nhau | Instancing, mô phỏng một lần rồi tra cứu | Đám đông, người dùng, thị trường |
| Tế bào | Một mặt phẳng chia thành các ô | Shader | Lãnh thổ, phân vùng, cụm |
| Lan tràn | Các họa tiết lan ra và ăn lẫn nhau | Shader | Sinh học, lây lan, sự chấp nhận (adoption) |
| Lát gạch (tiling) | Vài loại viên gạch tạo thành họa tiết bất tận | Layer 2D | Quy tắc, tổ hợp |
| Gạch Truchet lật | Một lưới các viên gạch mỗi viên chứa hai cung một phần tư, xoay ngẫu nhiên để các cung nối thành những con đường bất tận; các viên lật theo một làn sóng và các con đường định hình lại | Layer 2D, hoặc một pass toàn màn hình quyết định góc xoay mỗi viên từ hash của ô; cú lật là một lần xoay viên gạch tại thời điểm tăng theo khoảng cách từ một điểm | Con đường, lựa chọn, mạng lưới, đoạn giữa của một showreel |
| Lưới qua mắt cá | Một lưới ô hoặc chấm phồng lên như nhìn qua thấu kính, chỗ phồng di chuyển hoặc tạo thành một hình hay một từ | Một pass toàn màn hình dịch mỗi pixel ra xa tâm theo một đường cong của khoảng cách trước khi tra lưới; hình dạng chỗ phồng lấy từ một mask | Nhấn mạnh, một con số được hé lộ, một thấu kính trên dữ liệu |
| Kính vạn hoa | Một hình phản chiếu thành các múi quanh tâm, xoay | Một pass toàn màn hình gấp góc vào một múi trước khi tra hình | Âm nhạc, trance, vòng lặp thôi miên |
| Đường hầm, trường sao | Di chuyển vào chiều sâu | Shader | Transition, thời gian trôi |
| Trường gradient | Các trường màu mềm trôi dạt | Shader | Nền tĩnh lặng, phim cao cấp |
| Phổ, dạng sóng | Các thanh hoặc một đường đi theo âm thanh | Layer 2D từ dữ liệu audio | Hiếm khi. Đó là ý tưởng đầu tiên của tất cả mọi người |

Look tạo sinh mạnh khi làm nền và yếu khi làm chủ thể. Một explainer vẫn cần một thứ để nhìn vào.

### 3.6 Các trường phái thiết kế đồ họa

| Phong cách | Trông như | Hợp với | Lưu ý |
|---|---|---|---|
| Swiss | Lưới nghiêm ngặt, font grotesque, bất đối xứng, đen, trắng và một màu đỏ | Thông tin, tổ chức | Lạnh lẽo nếu không có gì chuyển động |
| Constructivist (kiến tạo) | Màu cơ bản, hình tròn và tam giác, đường chéo mạnh | Tuyên ngôn, giáo dục | |
| Brutalist | Thô, chữ khổng lồ, tương phản gắt | Tuyên bố táo bạo | |
| Art Deco | Đối xứng, đường vàng, hình quạt | Sang trọng, thập niên 1920 | |
| Mid-century | Hình phẳng có texture, hình học vui nhộn | Explainer thân thiện | |
| Psychedelic (ảo giác) | Chữ lượn sóng, màu chọi nhau | Âm nhạc | Khó đọc |
| Memphis | Nét ngoằn ngoèo, hình confetti, pastel với đen | Tuổi trẻ, vui chơi | |
| Tạp chí | Serif lớn, khoảng trống rộng rãi | Câu chuyện cao cấp | |
| Kinetic type | Chữ và không gì khác | Trích dẫn, lời bài hát, tuyên ngôn | Phim đứng hay đổ là nhờ lời lẽ |
| Đơn sắc | Một sắc độ cùng đen và trắng | Chủ đề nghiêm túc | |

### 3.7 Với ảnh chụp hoặc footage

Khi có hình của vật thật, hoặc có thể tạo ra. Việc tạo hình tốn tiền thì không bao giờ được bắt đầu khi chưa hỏi chủ sở hữu.

| Phong cách | Trông như | Hợp với |
|---|---|---|
| Duotone | Một bức ảnh hai màu | Chân dung, địa điểm |
| Ảnh halftone | Một bức ảnh dưới dạng chấm | Look in ấn |
| Cắt ghép (cut-out) | Đồ vật chụp ảnh được cắt ra và đặt lên một nền vẽ | Collage, hài hước |
| Collage từ ảnh chụp | Ảnh cắt ra có viền giấy trắng, halftone hoặc in báo, mép xé, băng dính, drop shadow mềm, trên nền phong cảnh chụp ảnh | Câu chuyện, phim "về chúng tôi", du lịch, hành trình như mơ, zoom vô tận. Xem mục 3.8 |
| Cắt ghép halftone với con dấu và ticker | Ảnh dưới dạng cắt ghép halftone thô, con dấu cao su và nhãn đập lên trên, một dải tin chạy ở chân, ảnh chụp màn hình và chú thích trong một lưới thô bạo | Music video, "internet brutalism", nhại tin tức, meme. Hình phải là của chủ sở hữu hoặc có giấy phép rõ ràng (mục 3.8) |
| Đẩy chậm vào ảnh tĩnh | Một ảnh tĩnh được tiến vào chậm rãi | Lịch sử, đoạn tĩnh lặng |
| Quay màn hình | Màn hình thật trong một khung thiết bị | Demo sản phẩm |
| Các lớp theo chiều sâu | Một ảnh tĩnh tách thành các lớp di chuyển tách rời nhau | Chiều sâu từ một hình phẳng |

Trên route engine, một bức ảnh, logo hay ảnh chụp màn hình được vẽ bằng `ImageTexture` và `drawPicture`, hoặc trên một layer canvas bằng `drawImageFit`, còn một clip là một `ImageSequence` (`src/engine/media.ts`; `engine-architecture.md`, mục 4). File nằm trong `media/`.

Phim dựng chủ yếu từ footage, một website hay một giọng đọc thì phù hợp hơn với route HyperFrames: xem `hyperframes-route.md`.

### 3.8 Chi tiết các look

Những look này hay được yêu cầu và có những quy tắc dễ bị phá.

#### Pixel art ở tỉ lệ số nguyên

| Quy tắc | Cách làm |
|---|---|
| Một độ phân giải logic | Chọn kích thước tác phẩm trước: 128 x 96, 160 x 90, hoặc với phim dọc là 90 x 160 hay 135 x 240. Mọi thứ được vẽ trên canvas nhỏ đó, bằng pixel của nó |
| Một tỉ lệ số nguyên | `PixelLayer` (`src/scenes/parts/kit-pixel.ts`) đặt tác phẩm lên frame với mỗi pixel đúng `factor` x `factor` pixel đầu ra, nearest neighbour, canh giữa. Mặc định factor là số nguyên lớn nhất vừa khít; phần frame quanh tác phẩm giữ nguyên những gì shot đã vẽ trước. 135 x 240 lấp đầy frame 1080 x 1920 ở tỉ lệ 8 |
| Mọi thứ trên lưới | Vị trí là số pixel nguyên. Vẽ bằng hình chữ nhật, `dot`, `pixelLine` và `sprite` (một sprite viết dưới dạng các hàng ký tự tra trong palette). Một hình vẽ bằng cung, chữ hoặc phép xoay sẽ có mép mềm; chạy `toPalette` sau đó, hàm này đưa mọi pixel về palette và làm alpha thành 0 hoặc 1. Truyền cho nó hình chữ nhật bao hình và chỉ các màu riêng của hình cùng các màu phía sau nó: khi snap theo toàn bộ palette, mép mềm của một mặt trăng trắng trên bầu trời đêm đã nhặt phải các pixel xanh lá trong một lần thử |
| Một palette cố định | 16 đến 32 màu, viết một lần cho phim. Mọi pixel đều lấy từ đó. Ánh sáng được làm bằng cách chọn một mục tối hơn hoặc sáng hơn, không bao giờ bằng blend |
| Chuyển động nhảy bậc | Tính tư thế từ `stepTime(frameTime(f.t), 10)`: 8 đến 12 tư thế mỗi giây, trong khi studio phát ở frame rate của phim. Tư thế có thể được key và ease như thường rồi lượng tử hóa: trước là tư thế, sau là lưới |
| Bộ phận không xoay tự do | Một sprite pixel bị xoay một góc sẽ bị lấy mẫu lại và mất pixel. Vẽ vài góc mà một bộ phận cần thành các sprite, hoặc dựng nhân vật từ các hình chữ nhật có góc được snap sau khi tính tư thế |
| Tắt phần hoàn thiện | Trả về `POST_PIXEL` từ `render()`: không bloom, không halation, không grain, không viền màu, không vignette. Một quầng sáng được vẽ trong tác phẩm như một vòng màu palette sáng hơn |
| Rung trên lưới | Rung một hoặc hai pixel của tác phẩm làm dịch hình vẽ theo số pixel nguyên. Shake và zoom của post chain dịch frame theo phân số của một pixel tác phẩm và làm nhòe lưới |
| Transition | Cắt thẳng, và wipe di chuyển theo số pixel nguyên của tác phẩm. Punch và step zoom của engine thay đổi zoom của frame hoàn chỉnh và lấy mẫu lại pixel; một mosaic lớn dần theo pixel nguyên là transition bản địa của look này |

Đã kiểm tra qua ảnh tĩnh của một cảnh thử: một cảnh đêm 128 x 96 trên frame 1080 x 1920 ra tỉ lệ 8, canh giữa, có nền của shot bao quanh, mọi pixel vuông và sắc nét, các góc đúng chiều. Việc đọc canvas ngược lại cho `toPalette` khiến trình duyệt cảnh báo rằng đọc lặp lại sẽ nhanh hơn với một canvas tạo riêng cho việc đó; ở kích thước này chi phí là nhỏ.

#### Collage từ ảnh chụp

| Quy tắc | Cách làm |
|---|---|
| Ảnh đến từ đâu | Ảnh của chính chủ sở hữu; ảnh thuộc phạm vi công cộng (public domain) hoặc có giấy phép mở, với nguồn và giấy phép được ghi lại trong thư mục của phim bên cạnh mỗi file; hoặc một trình tạo ảnh, thứ tốn tiền và chỉ được bắt đầu khi chủ sở hữu đồng ý, mỗi lần, với chi phí được nêu rõ. Không bao giờ dùng một bức ảnh tìm trên web mà không rõ giấy phép |
| Hình cắt | Một hình cắt là một bức ảnh có nền trong suốt, chuẩn bị trước khi dựng phim và lưu thành file. Viền giấy trắng do shot vẽ: nới hình dạng của hình cắt ra vài pixel bằng màu trắng, rồi đặt bức ảnh lên trên |
| In ấn | Halftone cho look báo chí: một lưới chấm trong một pass toàn màn hình phủ lên hình cắt, hoặc nền giấy-và-chấm của `src/scenes/parts/kit-ground.ts` bên dưới. Hình cắt đen trắng trên phong cảnh màu là một tương phản kinh điển |
| Giấy | Mép xé vẽ thành đường viền lởm chởm từ noise có seed, cố định cho mỗi mảnh; băng dính là một dải trong mờ nhạt màu; một hướng sáng cho mọi drop shadow |
| Chuyển động | Các mảnh trượt, rơi và nảy như giấy; nhảy bậc hai frame (12 hoặc 15 tư thế mỗi giây) để có cảm giác hoạt hình cắt giấy; chiều sâu từ các layer chuyển động với tốc độ khác nhau |
| Chiều sâu từ một bức hình | Một phong cảnh tách thành ba hoặc bốn layer (trời, xa, giữa, gần) tách rời khi camera đẩy vào. Các lỗ phía sau các layer gần phải được lấp khi cắt layer, không phải trong shot |

#### Toon và cartoon có viền

| Phần | 2D | 3D |
|---|---|---|
| Tô | Màu phẳng, một tông bóng dạng hình, một điểm sáng | `MeshToonMaterial` với gradient map ba hoặc bốn bậc, lọc bằng `NearestFilter` |
| Viền | Ngoài dày, trong mảnh, một màu tối cho toàn bộ dàn nhân vật | Một pass cạnh từ normal và depth: dày ở silhouette, mảnh ở nếp gấp. Xem `characters-and-story.md`, mục 8 |
| Ánh sáng | Một viền tông sáng hơn ở phía xa mặt đất | Key, sky và rim light theo sắc độ của phần đó |
| Bóng trên mặt đất | Một hình elip mềm co lại khi vật bay lên | Như vậy, vẽ thành một mặt phẳng hoặc trên một layer 2D bên dưới |
| Post | Bloom thấp, và viền giữ dưới ngưỡng của nó | Như vậy |

#### Hoạt họa cát

Hoạt họa cát kể một câu chuyện như một bức hình chảy liên tục: mỗi hình được tạo ra từ hình trước bằng cách xóa, rắc và cào, không bao giờ bằng một cú cắt. Trong code, look này là một bàn sáng đầy hạt: một pass toàn màn hình vẽ hạt cát và ánh sáng xuyên qua chỗ cát mỏng; các hình là mask vẽ trên layer 2D, được blur, và chuyển thành độ dày của cát. Một cú xóa là một mask di chuyển dọc đường đi của bàn tay; một cú rắc là một mask lớn dần từ một điểm với mép nhiễu. Câu chuyện được lên kế hoạch như một chuỗi hình trong đó mỗi hình chứa khởi đầu của hình kế tiếp. Nó chưa được dựng trên phim nào.

#### Chất liệu hội họa và vẽ

Chưa cái nào trong số này được dựng trên phim. Mỗi cái là một cách đặt nét, và mỗi cái có một quy tắc khiến nó đọc ra đúng.

| Chất liệu | Cách dựng | Quy tắc khiến nó đọc ra đúng |
|---|---|---|
| Nét cọ (Van Gogh) | Vẽ cảnh một cách đơn giản trước (một layer hoặc một target). Rồi đặt các nét lên một lưới có seed, hơi jitter; xoay mỗi nét theo một trường dòng chảy (curl của noise, hoặc hướng các cạnh của hình); lấy màu mỗi nét từ hình bên dưới, đẩy nhẹ sắc độ và độ sáng; vẽ chúng thành các đường ngắn rộng đầu tròn trong một line batch. Trời và đất có dòng chảy riêng | Các nét đi theo hình khối. Một nét cắt ngang hình khối ngẫu nhiên trông như nhiễu |
| Bút chì | Nét bị vân giấy làm đứt (nhân với một noise theo vân giấy), lực nhấn thay đổi dọc nét, gạch bóng một góc trong vùng tối, gạch chéo ở vùng tối nhất | Giấy lộ ra ở mọi nơi, kể cả phần tối nhất |
| Bút bi | Nét xanh mảnh gần như đều độ rộng, gạch dày đặc tối hơn chỗ các nét giao nhau, một vết mực ở đầu nét | Nhiều nét, không bao giờ tô mảng |
| Sáp màu | Một mảng tô bị mask bởi vân giấy với threshold, để màu chỉ bám trên đỉnh vân; mép không khớp hẳn đường viền | Khoảng hở: các đốm trắng bên trong màu |
| Bút dạ | Nét phẳng bão hòa một độ rộng, composite bằng `multiply` để chỗ chồng tối hơn | Chỗ chồng hiện ra |
| Stop-motion vẽ tay | Bất kỳ cái nào ở trên, vẽ lại mỗi hai hoặc ba frame với seed mới mỗi bậc | Các bậc lấy từ đồng hồ frame (`frameTime` trong `src/scenes/parts/kit-frame.ts`) |

Một pass toàn màn hình làm bất kỳ hình nào trông như được vẽ sơn (bộ lọc Kuwahara, làm phẳng màu thành từng mảng mà vẫn giữ cạnh) là một kỹ thuật đã biết và không có trong starter.

#### Thế giới cách điệu, bầu trời và giờ trong ngày

`Sky` trong `src/scenes/parts/kit-ground.ts` vẽ toàn bộ một nền ngoài trời trong một pass và ghi đè target, như `Ground`: một gradient từ thiên đỉnh tới chân trời, sương dày dần về phía chân trời, mặt trời hoặc mặt trăng với quầng sáng, mây từ noise (mềm, hoặc hai đến bốn bậc cel cứng, sáng ở phía hướng mặt trời), và dưới chân trời là nước phản chiếu bầu trời với gợn sóng và một vệt lấp lánh dưới mặt trời, hoặc đất liền mờ dần vào sương. Màu là chuỗi hex của bầu trời riêng của cảnh, không phải khóa palette.

| Helper | Làm gì |
|---|---|
| `Sky`, `SkyStyle` | Pass và các thiết lập của nó: `zenith`, `horizon`, `horizonY`, `haze`, `sun`, `clouds`, `below`, và `t` cho gợn sóng |
| `skyAt(at, keys)` | Màu của trời, mặt trời và ánh sáng tại một khoảnh khắc, trộn giữa các `SkyKey`. `at` có thể là một giờ, một beat hay một mùa: đây là cách giờ trong ngày chuyển dần bên trong một shot |
| `hazed(colour, horizon, depth, haze)` | Một màu nhìn qua không khí, ở `depth` phần quãng đường tới chân trời: phối cảnh khí quyển cho đồi, cây và tòa nhà vẽ trên các layer |
| `mixHex(a, b, k)` | Hai màu hex trộn trong ánh sáng tuyến tính: ánh sáng của giờ trong ngày trên màu riêng của một vật |

Đã kiểm tra qua ảnh tĩnh của một cảnh thử: một vùng biển từ cuối chiều đến hoàng hôn trong mười hai beat, với ba dãy đồi mờ sương về phía chân trời và mây cel. Mây và vệt lấp lánh cần hai vòng chỉnh: noise năm octave tạo mây loang lổ, và một vệt lấp lánh rộng phủ đầy nước những đốm lốm đốm. Mặc định hiện nay dùng ba octave với chút chi tiết ở mép và một vệt hẹp.

| Quy tắc | Vì sao |
|---|---|
| Mọi thứ nhận ánh sáng của giờ trong ngày | Tint mọi layer bằng `light` của key, và làm mờ sương bằng `horizon` của key. Một bầu trời chuyển cam trên những ngọn đồi xanh vẫn giữ nguyên màu xanh trông như dán vào |
| Mùa cũng là key | Xuân, hạ, thu và đông là các `SkyKey` cộng màu lá và màu đất; tuyết là mặt đất chuyển sang màu giấy với bóng xanh lam |
| Trời lớn, chân trời thấp | Thế giới cách điệu sống trong bầu trời của chúng. Đặt chân trời thấp cho cảm giác kỳ diệu, cao cho một hành trình trên đất liền |
| Gió làm mọi thứ chuyển động cùng một hướng | Cỏ, mây, cờ và tóc nghiêng về một phía, với độ trễ có seed |
| Trong 3D | Sương mù three.js theo màu chân trời, một vòm trời vẽ bằng cùng gradient, mặt trời là một directional light màu `sun` của key, và chất liệu toon hoặc mềm. Cùng các key điều khiển cả hai |

#### CRT và demoscene

Idiom demoscene là một tập nhỏ các hiệu ứng, mỗi cái vài dòng shader, trên nền đen: raster bar (copper bar) lăn theo sóng sin, twister (một cột chữ hoặc sọc xoắn quanh trục của nó), dòng chạy chữ lời chào bằng font bitmap, trường sao ba tốc độ, và một logo nảy. Mọi thứ chuyển động theo sóng sin khóa vào beat. Vẽ ở độ phân giải thấp bằng `kit-pixel.ts` cho look bitmap, hoặc ở độ phân giải đầy đủ cho look vector, và hoàn thiện bằng xử lý CRT của post chain khi có (`effects.md`). Giữ chữ đọc được qua độ cong, và giữ palette đúng thời kỳ: ít màu, sáng trên nền đen.

## 4. Công thức theo loại phim

Một điểm xuất phát cho treatment. Gu của chủ sở hữu và chủ đề là thứ quyết định.

| Loại phim | Tông | Look phù hợp | Chữ | Chuyển động | Nhạc |
|---|---|---|---|---|---|
| Khái niệm giải thích cho người mới | Ấm áp, rõ ràng | Idiom từ đời sống hằng ngày, mỗi khái niệm một cái; giấy cắt; hình người tô đặc; màn hình app cho "nơi bạn gặp nó" | Một font display có cá tính, một font caption đơn giản | Một sự kiện mỗi beat, không gì để trang trí | Nhạc không lời với các drop rõ ràng |
| Đào sâu kỹ thuật | Chính xác | Blueprint, bằng sáng chế, đồ thị node, terminal, axonometric | Monospace cho nhãn | Di chuyển chậm, các bước chính xác | Đều đặn, không ồn ào |
| Ra mắt sản phẩm | Tự tin | Màn hình app, kính, studio sản phẩm, hình phẳng, kinetic type | Font riêng của thương hiệu | Xuất hiện dứt khoát, một chuyển động hero | Sôi nổi |
| Đi qua một tính năng | Thực tế | Màn hình app với con trỏ hoặc ngón tay, khung thiết bị | Font riêng của sản phẩm | Nhấn và đáp lại, cùng nhau trong một beat | Một lớp nền yên tĩnh |
| Câu chuyện dữ liệu | Điềm tĩnh | Báo chí, dashboard, pictogram, sổ cái | Serif cho tiêu đề, con số trong font dạng bảng (tabular) | Thanh lớn dần, số đếm lên, mỗi lần một biểu đồ | Bình thản |
| Hướng dẫn theo bước | Hữu ích | Sách hướng dẫn lắp ráp, phiếu đặt hàng, checklist | Số trong vòng tròn | Một điểm đánh dấu đi từ bước này sang bước khác | Nhẹ nhàng |
| Hình ảnh cho nhạc | Theo chính âm nhạc | Nền tạo sinh, đường phát sáng, vector arcade, impact frame truyện tranh | Ít hoặc không có | Mọi thứ trên lưới của âm nhạc | Chính là chủ đề |
| Lời bài hát | Theo chính bài hát | Kinetic type, chữ gỗ, một idiom từ thế giới của bài hát | Lớn, một giọng | Các từ trên âm tiết của chúng | Bài hát |
| Logo sting | Ngắn và chắc | Shape mask, studio sản phẩm, hình phẳng | Logo | Một lần dựng, một lần giữ | Ba đến năm giây |
| Title sequence | Thiết lập thế giới | Một idiom giữ suốt, silhouette, chữ tạp chí | Tên là một phần của hình | Chậm, liên tục | Nhạc chủ đề |
| Video ngắn cho mạng xã hội | Ồn ào ngay giây đầu | Sticker, truyện tranh, brutalist, màn hình app | Khổng lồ | Một hook ở beat đầu tiên, cắt nhanh | Nhanh |
| Dòng thời gian, tổng kết một sự kiện | Tự hào | Vé, con dấu, tạp chí, ảnh duotone | Một serif | Một đường chạy qua các mốc ngày | Ấm áp |
| Tiền bạc, thị trường | Đáng tin cậy | Sổ cái, báo chí, màn hình chấm, đơn sắc | Chữ số dạng bảng | Con số lăn như bộ đếm | Kiềm chế |
| Cho trẻ em | Vui vẻ | Giấy cắt, đất sét, sách truyện, sticker | Tròn trịa | Nảy, squash and stretch | Vui nhộn |
| Khoa học, thiên nhiên | Tò mò | Mực và màu nước loang, hình cắt, sinh trưởng, tế bào | Một serif nhẹ nhàng | Hé lộ chậm | Thoáng đãng |
| Lịch sử | Tôn trọng | Tranh khắc gỗ, báo chí, bản đồ, con dấu | Font của thời kỳ đó | Đẩy chậm | Của thời kỳ đó |
| So sánh | Công bằng | Khung chia đôi, thẻ, hai giá đỡ | Một font, hai màu | Chuyển động đối xứng gương | Cân bằng |
| Danh sách N mục | Nhanh gọn | Mỗi mục một thẻ với cách sắp xếp riêng, rồi cả danh sách | Một bộ đếm | Mỗi ô nhịp một mục | Thúc đẩy |
| Release notes | Thẳng thắn | Màn hình app, dấu diff, con dấu | Font riêng của sản phẩm | Trước và sau | Nhẹ nhàng |
| Phim ngắn có nhân vật | Theo chính câu chuyện | Một dàn nhân vật trong một look giữ suốt phim: cartoon, giấy cắt, toon 3D, pixel art, người que. Một file dàn nhân vật (cast file) dùng chung cho mọi builder (`characters-and-story.md`) | Ít; một tiêu đề và một thẻ kết bằng font của thế giới phim | Tư thế key trên beat, hold, anticipation, squash and stretch; cận cảnh khi cần đọc được khuôn mặt | Chọn theo hình dạng câu chuyện: các drop của nó là bước ngoặt và phần trả công (pay-off) |
| Câu chuyện kể không lời | Rõ ràng, rồi xúc động | Silhouette mạnh, mỗi nhân vật một màu, đồ vật người xem quen thuộc thay cho lời | Không có, hoặc biển báo trong thế giới phim | Hướng nhìn, phản ứng, gài cài và nhắc lại (plant and callback), một nút thắt ở cuối | Hiệu ứng âm thanh và khoảng lặng lên kế hoạch từng shot; mỗi nhân vật một motif |
| Hành trình xuyên các tỉ lệ | Kỳ diệu | Một cú zoom liền mạch qua các thế giới lồng nhau, mỗi thế giới vẽ ở tỉ lệ riêng (`camera.md`, mục 3.7); một thước tỉ lệ là hằng số duy nhất | Một nhãn nhỏ cho mỗi thế giới, một số đọc tỉ lệ | Di chuyển đều theo bậc mười (decade) mỗi beat, dừng lại ở các thế giới quan trọng | Đều đặn, dồn lên dần |

## 5. Màu sắc

### Vai trò

Cho màu sắc nhiệm vụ, không phải tên gọi.

| Vai trò | Nhiệm vụ | Quy tắc |
|---|---|---|
| Ink (mực) | Màu trung tính tối: nền tối, chữ trên nền sáng | Không bao giờ đen tuyền; một chút sắc độ giữ nó sống động |
| Paper (giấy) | Màu trung tính sáng: nền sáng, chữ trên nền tối | Không bao giờ trắng tinh |
| Mực thứ hai, giấy thứ hai | Tấm nền, bảng, một bậc chiều sâu | Cách màu trung tính của chúng một bậc |
| Xám | Những thứ lùi ra sau | Hai màu là đủ |
| Signal (tín hiệu) | Thứ CHÍNH LÀ ý tưởng | Không thứ gì khác được dùng nó. Nó có một màu đi kèm nóng hơn cho phần lõi |
| Trouble (rắc rối) | Vấn đề, lỗi, cảnh báo | Không bao giờ dùng để trang trí |
| Sắc độ chủ đạo (key hues) | Mỗi phần một màu, cho thế giới của nó | Tổng cộng ba hoặc bốn, cách xa nhau và cách xa signal và trouble |

Từ thực tế: một palette mười hai màu đã phục vụ một phim tám phần: hai màu trung tính mỗi màu có một bậc thứ hai, hai màu xám, một màu signal hồng với lõi nhạt hơn, một màu cam cho trouble, và bốn sắc độ chủ đạo.

`src/engine/palette.ts` của starter chứa mười hai màu theo các vai trò này: `ink` và `ink2`, `paper` và `paper2`, các màu xám `graphite` và `ash`, `signal` với lõi `blush`, và các sắc độ chủ đạo `sun`, `tangerine`, `teal` và `violet`. Nó không có màu cho trouble; hãy giao nhiệm vụ đó cho một trong các sắc độ của phim, hoặc thêm một key. `bg` và `fg` lặp lại `ink` và `paper` và phải được giữ lại, vì engine dùng chúng.

### Ngoại lệ được tạo ra có chủ đích

Một quy tắc về màu sắc phục vụ việc đọc. Khi nó không còn làm được điều đó, hãy phá nó và ghi lại lý do. Từ thực tế: các lớp bọc quanh một lõi đều được vẽ bằng màu signal, vì mỗi lớp đều là "ý tưởng". Chủ sở hữu không phân biệt được chúng. Sau đó mỗi lớp được cho một sắc độ riêng và lõi giữ màu trung tính.

### Blend màu

Màu được blend trong ánh sáng tuyến tính. Hai hệ quả gây ngạc nhiên:

| Hiệu ứng | Nguyên nhân | Quy tắc |
|---|---|---|
| Một tấm nền tối trên nền sáng chuyển xám | Vài phần trăm của một nền sáng lộ qua là rất nhiều ánh sáng | Tấm nền phải đục hoàn toàn |
| Multiply tối hơn so với trong phần mềm thiết kế | Phần mềm blend trong không gian gamma | Đánh giá trên frame đã render, không bao giờ trên các con số |

### Độ tương phản

Chữ so với nền cần một khác biệt rõ ràng về độ sáng. Một sắc độ bão hòa đặt trên một sắc độ bão hòa khác cùng độ sáng thì không đọc được, bất kể sắc độ nào. Trên một vòng hoặc tab có màu, đặt tên bằng ink hoặc paper, chọn cái nào xa sắc độ đó hơn.

### Thời điểm trong ngày và mùa

Một cảnh có ánh sáng thay đổi (chiều tới hoàng hôn, hạ sang đông) thay đổi mọi màu của nó cùng lúc, từ một bộ key: `skyAt` của `src/scenes/parts/kit-ground.ts` cho bầu trời, mặt trời và một màu `light` cho mỗi khoảnh khắc, và mọi thứ được vẽ là màu riêng của nó trộn về phía ánh sáng đó (`mixHex`) và làm mờ sương theo khoảng cách (`hazed`). Palette của phim vẫn cho các vai trò: màu signal vẫn là màu signal lúc hoàng hôn, và chữ vẫn là ink hoặc paper.

## 6. Texture và hoàn thiện

| Hoàn thiện | Làm gì | Dùng |
|---|---|---|
| Grain (hạt) | Phá độ mượt của màu kỹ thuật số | Luôn có một chút, ít hơn trên nền sáng |
| Chấm halftone | Cho nền một thứ để bám vào | Nền, bóng, vũng sáng |
| Sợi giấy | Biến một nền sáng thành giấy | Nền sáng |
| Gạch bóng | Đổ bóng mà không có màu xám | Look in ấn |
| Glow (quầng sáng) | Biến màu thành ánh sáng | Chỉ trên những gì là nguồn sáng trong hình. Chữ giữ dưới ngưỡng |
| Halation | Một quầng ấm quanh thứ sáng | Nền tối |
| Bóng cứng | Nói "giấy trên giấy" | Giấy cắt, thẻ, sticker |
| Bóng mềm | Nói "vật trên một bề mặt" | Vật 3D, một hero duy nhất |
| Vignette | Kéo mắt vào trong | Nền tối, nhẹ nhàng |
| Viền màu | Nói "thấu kính" | Va chạm, không bao giờ trên chữ cần đọc |

## 7. Một phim, nhiều look

Khi mỗi phần có idiom riêng, những thứ này gánh sự thống nhất:

| Hằng số | Được mang bởi |
|---|---|
| Palette và các vai trò của nó | Mọi shot |
| Hai hoặc ba typeface, mỗi cái một nhiệm vụ | Mọi chữ |
| Một bộ đếm hoặc một dấu ở một góc | Overlay |
| Màu signal xuất hiện cùng ý tưởng | Mọi phần |
| Cách đặt caption | Overlay |
| Grain và lớp hoàn thiện | Post chain |
| Một phần tóm tắt trong đó thứ của mỗi phần xuất hiện trong một look | Cuối phim |

Đánh giá một shot so với shot tốt nhất trong chính phần của nó. Nếu đặt cạnh nhau nó trông như một phim khác, rẻ tiền hơn, thì nó đã lạc thiết kế và được dựng lại theo idiom của shot tốt nhất đó.

## 8. Route HyperFrames mang lại gì

Skill sáng tạo của nó mang theo các look dựng sẵn. Chúng dành cho trang web, không phải cho shader, và tất cả đều để chuyển động nằm ngoài phạm vi.

| Danh mục | Tên |
|---|---|
| Preset khung (13) | `biennale-yellow`, `blockframe`, `blue-professional`, `bold-poster`, `broadside`, `capsule`, `cartesian`, `cobalt-grid`, `code-editorial`, `coral`, `creative-mode`, `daisy-days`, `editorial-forest` |
| Phong cách hình ảnh (8) | Swiss Pulse, Velvet Standard, Deconstructed, Maximalist Type, Data Drift, Soft Signal, Folk Frequency, Shadow Cut |
| Palette (9) | `bold-energetic`, `clean-corporate`, `dark-premium`, `jewel-rich`, `monochrome`, `nature-earth`, `neon-electric`, `pastel-soft`, `warm-editorial` |
| Ví dụ để bắt đầu | `warm-grain`, `swiss-grid`, `vignelli`, `kinetic-type`, `product-promo`, `nyt-graph`, `decision-tree` |

## 9. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Một shot trông rẻ tiền hơn các shot bên cạnh | Primitive trơn, hình người không đặc điểm | Dựng lại theo idiom của shot tốt nhất trong phần |
| Hai phần bị nhầm với nhau | Chúng dùng chung một đạo cụ hoặc một màn hình | Đổi idiom hoặc ví dụ của một phần |
| Người xem không biết nhìn vào đâu | Màu signal nằm trên nhiều thứ | Mỗi shot chỉ một thứ mang nó |
| Những thứ cần phân biệt trông như một dải | Một màu cho tất cả | Mỗi thứ một sắc độ; lõi không đổi giữ màu trung tính |
| Một tấm nền trông xám và bẩn | Nó gần đục, trên một nền sáng | Làm nó đục hoàn toàn |
| Chữ lấp lánh hoặc bị bloom | Nó vượt ngưỡng glow | Giữ chữ dưới ngưỡng; giảm tông chữ nhẹ |
| Nhãn không đọc được | Một font thô với dấu tiếng Việt, hoặc chữ trên mặt phẳng nghiêng | Chấm lớn hơn, font khác, hoặc nhãn phẳng |
| Look trông như một explainer đại trà | Hình phẳng và bảng trắng không có idiom | Lấy một idiom từ thế giới của chủ đề |
| Một phần ba dưới của khung dọc trống ở mọi shot | Bố cục làm cho khung rộng | Xếp chồng; để chủ thể chạy hết chiều cao của vùng an toàn |
| Tiêu đề đầu tiên bị chê xấu | Một hình đặc và một dòng chữ, không có gì của phim trong đó | Dựng tiêu đề từ những thứ của phim |
| Pixel art trông mềm, hoặc có pixel hai kích cỡ | Vẽ ở độ phân giải đầy đủ, xoay tự do, hoặc hoàn thiện bằng bloom và grain | Vẽ trên canvas nhỏ của `PixelLayer`, snap sau khi đặt tư thế, trả về `POST_PIXEL` |
| Collage trông như dán chứ không phải cắt | Không có viền giấy, bóng nhiều hướng, các hình có độ hạt khác nhau | Viền cho mọi hình cắt, một nguồn sáng cho mọi bóng, một kiểu xử lý in ấn cho mọi hình |
| Một nhân vật trông khác nhau ở mỗi shot | Mỗi builder tự vẽ nó | Một file dàn nhân vật, do lead sở hữu (`characters-and-story.md`) |
| Look hội họa trông như một filter | Nét cùng cỡ, hướng ngẫu nhiên, phủ lên mọi thứ | Nét đi theo hình khối; lớn ở nền, nhỏ trên chủ thể |
| Phong cảnh vẽ trông phẳng và nhỏ | Không có sương, vật ở xa tối và bão hòa như vật ở gần | `hazed` về phía màu chân trời, nhiều hơn theo khoảng cách |
| HUD trông như đồ lấp chỗ | Giá trị không đổi hoặc không đúng, dấu ở mọi góc | Làm mọi số đọc đúng và chuyển động, hoặc bỏ HUD |
