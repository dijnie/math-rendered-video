# Phỏng vấn

Cách tìm hiểu owner muốn gì trước khi vẽ bất cứ thứ gì: đọc gì trước, hỏi gì, theo thứ tự nào, với những lựa chọn nào, và điều gì không bao giờ được tự giả định. File có một ngân hàng câu hỏi bằng tiếng Anh và tiếng Việt.

Nạp file này khi: có yêu cầu làm phim, một brief chưa rõ, owner hỏi "hiểu chưa?", hoặc giữa chừng công việc nảy ra một quyết định thuộc về owner. Với một đoạn dưới khoảng 40 giây, hãy đọc `short-pieces.md` trước: nó thay brief bằng vài giả định được nêu rõ và vòng 5 bên dưới.

## 1. Quy tắc

| Quy tắc | Ý nghĩa |
|---|---|
| Đọc trước khi hỏi | Chính yêu cầu, repository, các tham chiếu owner nêu tên, các phim trước, memory của các phiên trước. Một câu hỏi mà một file đã trả lời sẽ làm hao sự kiên nhẫn của owner |
| Hỏi những gì thuộc về owner | Chủ đề, người xem, gu, tiền, nơi phim được chiếu. Tự quyết những gì tra cứu hoặc thử được |
| Ít câu hỏi, theo vòng | Tối đa bốn câu một vòng. Mỗi vòng phụ thuộc vào câu trả lời của vòng trước |
| Một quyết định mỗi câu hỏi | Với hai đến bốn lựa chọn. Lựa chọn bạn đề xuất đứng đầu và ghi rõ là đề xuất |
| Lựa chọn kèm hệ quả | Mỗi lựa chọn nói trong một dòng điều gì kéo theo nó: tốn gì, loại trừ gì |
| Có mặc định cho mọi thứ | Nếu một câu hỏi không đáng hỏi, hãy lấy mặc định và nói đã lấy mặc định nào |
| Nói lại những gì bạn hiểu | Trước vòng đầu tiên, trong ba dòng. Owner sửa một hình dung sai nhanh hơn là trả lời mười câu hỏi |
| Một câu trả lời không phải là giấy phép để dựng | Một mục lục được duyệt chỉ là một mục lục được duyệt. Tiếp theo là storyboard, rồi animatic, và chỉ sau đó mới đến các shot |
| Ghi lại câu trả lời | Trong file trạng thái của project, bằng chính lời của owner. Phiên sau sẽ cần chúng |

## 2. Quyết định của ai

| Vấn đề | Owner | Lead |
|---|---|---|
| Chủ đề, người xem, điều duy nhất người xem cần mang về | quyết định | đề xuất cách diễn đạt |
| Phim có những phần nào, và thứ tự của chúng | quyết định | đề xuất |
| Ngôn ngữ trên màn hình | quyết định | |
| Khung hình, độ dài, nơi chiếu | quyết định | khuyến nghị dựa trên nơi chiếu |
| Nhạc: track nào | quyết định, bằng tai | tìm hoặc làm các ứng viên |
| Có giọng đọc hay không | quyết định | |
| Tiêu tiền cho một dịch vụ trả phí | quyết định, mỗi lần | hỏi trước |
| Sản phẩm giao: một trang để xem, hay một file video | quyết định | |
| Máy được phép chạy nặng đến đâu | quyết định | |
| Look: khóa cố định hay tự do | quyết định | đề xuất các idiom (lối biểu đạt) |
| Mọi câu chữ trên màn hình | duyệt | viết |
| Hình ảnh được dựng thế nào | | quyết định |
| Công cụ và route | | quyết định, từ brief |
| Kit dùng chung, các quy tắc cho builder | | quyết định |
| Model nào dựng | có thể quyết định | đề xuất |

## 3. Trước câu hỏi đầu tiên

1. Nhắc lại yêu cầu trong ba dòng: phim nói về gì, cho ai, ở dạng nào.
2. Liệt kê những gì bạn coi là đã cho từ yêu cầu, đánh dấu **đã nêu** (stated) hoặc **suy ra** (inferred).
3. Đọc những gì owner chỉ tới. Nếu họ nêu một tham chiếu, hãy nghiên cứu nó làm gì, không phải nó trông thế nào: các shot của nó dài bao lâu, nó cắt ở đâu, nó dùng nhạc ra sao, nó giữ cố định những gì.
4. Chạy bước kiểm tra môi trường của skill (`scripts/check-environment.mjs` trong thư mục skill, với `.sh` và `.ps1` bên cạnh), để không hứa điều gì mà máy không làm được.

Khi owner hỏi "hiểu chưa?", hãy trả lời bằng phần nhắc lại và vòng câu hỏi đầu tiên. Đừng trả lời "rồi" rồi bắt đầu làm.

## 4. Các vòng

Mỗi câu hỏi có: khi nào hỏi, cách diễn đạt bằng tiếng Anh và tiếng Việt, các lựa chọn với lựa chọn đề xuất đứng đầu, và mặc định được lấy khi không hỏi. Phần tiếng Việt dùng cách xưng hô trung tính; hãy theo cách xưng hô mà owner dùng.

### Vòng 1: cái gì và cho ai

| Id | Hỏi khi | English | Vietnamese | Lựa chọn | Mặc định |
|---|---|---|---|---|---|
| `scope` | Chủ đề có nhiều phần | One film with a selection, or a series? | Làm một video gồm các phần chọn lọc, hay làm thành loạt nhiều video? | Một phim với các phần chọn lọc (đề xuất); một loạt, mỗi phim một phần; một phim với tất cả | Một phim với các phần chọn lọc |
| `audience` | Chưa được nêu | Who watches, and what do they already know? | Người xem là ai, và họ đã biết gì về chủ đề này? | Người mới không có nền tảng (đề xuất cho explainer); người trong nghề; lẫn lộn | Suy ra từ yêu cầu, và nói lại |
| `takeaway` | Luôn luôn, dưới dạng một câu khẳng định để xác nhận | The viewer should leave with: ... | Xem xong, người xem cần mang về: ... | Xác nhận; sửa | Một câu của lead |
| `language` | Chưa được nêu | Which language are the words on screen in? | Chữ trên màn hình dùng ngôn ngữ nào? | Ngôn ngữ của owner, giữ tên riêng ở nguyên bản (đề xuất); tiếng Anh | Ngôn ngữ owner dùng để viết |
| `frame` | Chưa được nêu | Which frame? | Khung hình nào? | Dọc 9:16 cho điện thoại (đề xuất cho feed mạng xã hội); ngang 16:9; vuông | Theo nơi phim được chiếu |
| `length` | Chưa được nêu | How long may it be? | Video dài tối đa bao lâu? | Khoảng một phút; khoảng ba phút, dưới 180 giây (đề xuất cho tám phần); dài hơn | Theo số phần: 15 đến 25 giây mỗi phần |
| `wording` | Phim giải thích ý tưởng | How much text per part? | Mỗi phần có bao nhiêu chữ? | Tên và một câu (đề xuất); tên, một câu và một ví dụ; chỉ tên | Tên và một câu |

### Vòng 2: âm thanh và cách giao

| Id | Hỏi khi | English | Vietnamese | Lựa chọn | Mặc định |
|---|---|---|---|---|---|
| `music-source` | Luôn luôn | Where does the music come from? | Nhạc lấy từ đâu? | Tôi làm các ứng viên bằng một dịch vụ tạo nhạc, bạn chọn bằng tai (tốn tiền: xem `spend`); bạn mang một track tới; một thư viện có bản quyền; không có nhạc | Hỏi |
| `music-kind` | Có muốn nhạc | Which kind, how fast? | Thể loại nào, nhanh cỡ nào? | Electronic dồn dập, 125 đến 140 beat một phút (đề xuất cho cắt nhanh); funk hoặc disco, 110 đến 120; nhẹ nhàng, dưới 100 | Hỏi; gu là của owner |
| `voice` | Chưa được nêu | Is there a voice? | Có giọng đọc không? | Không giọng, chỉ chữ trên màn hình (đề xuất cho route engine); một giọng đọc kịch bản | Không giọng |
| `spend` | Sẽ dùng bất kỳ dịch vụ trả phí nào | May I spend on this? It costs about ... per request. | Em dùng dịch vụ trả phí này được không? Mỗi lần gọi tốn khoảng ... | Được, tối đa ... lần gọi; hỏi tôi mỗi lần (đề xuất); không | Hỏi mỗi lần |
| `deliverable` | Luôn luôn | What do you want in the end? | Sản phẩm cuối cùng là gì? | Một trang phát phim trong trình duyệt (đề xuất: không encode gì, thay đổi hiện ra ngay); một file HTML duy nhất của phim hoàn chỉnh, mở được không cần server (bản build một file: `studio-viewer.md`); một file video; cả hai | Hỏi |
| `machine` | Owner làm việc trên cùng máy | May I load this machine with rendering? | Em chạy các tác vụ nặng trên máy này được không? | Chỉ still, mỗi lần một cái (đề xuất); cả clip ngắn; gì cũng được | Chỉ still, mỗi lần một cái |

### Vòng 3: look và mức tự do

| Id | Hỏi khi | English | Vietnamese | Lựa chọn | Mặc định |
|---|---|---|---|---|---|
| `reference` | Chưa có tham chiếu nào | Is there a film whose manner you want? | Có video nào anh/chị muốn làm theo phong cách đó không? | Đây là một cái; không, hãy đề xuất | Đề xuất |
| `style-image` | Owner đính kèm một ảnh "chỉ để lấy phong cách" | I read the image as these rules: palette, light, line, type, composition. Is that the manner you mean? | Em đọc ảnh này thành các quy tắc sau: bảng màu, ánh sáng, nét vẽ, kiểu chữ, bố cục. Đó có đúng phong cách anh/chị muốn không? | Xác nhận; sửa những điểm này | Cho thấy các quy tắc, rồi dựng (`thinking-and-brainstorm.md`, mục 5) |
| `style-lock` | Luôn luôn | One look for the whole film, or a look per part? | Cả video một phong cách, hay mỗi phần một phong cách? | Mỗi phần một look, gắn kết bằng palette, kiểu chữ và nhịp điệu (đề xuất cho phim nhiều phần); một look xuyên suốt; look của thương hiệu | Mỗi phần một look |
| `brand` | Phim dành cho một sản phẩm hoặc một công ty | Are there colours, typefaces, a mark to use? | Có màu, font, logo của thương hiệu cần dùng không? | Có, đây; không | Không |
| `concept` | Sau buổi brainstorm | Which direction? | Chọn hướng nào? | Ba hướng của buổi brainstorm, hướng đề xuất đứng đầu | Hỏi |
| `examples` | Phim giải thích ý tưởng bằng so sánh | Are these comparisons right? | Các ví von này đã đúng ý chưa? | Duyệt bảng; đổi những cái này | Hỏi |

### Vòng 4: công việc chạy thế nào

| Id | Hỏi khi | English | Vietnamese | Lựa chọn | Mặc định |
|---|---|---|---|---|---|
| `gates` | Luôn luôn, dưới dạng một câu khẳng định | I will stop for your approval after: the storyboard, the sample part, the finished film. | Em sẽ dừng chờ duyệt sau: kịch bản phân cảnh, phần mẫu, và bản hoàn chỉnh. | Xác nhận; thêm gate (điểm duyệt); bớt gate | Ba điểm đó |
| `builders` | Công việc sẽ dùng builder agent | Who builds the shots? | Ai dựng các phân cảnh? | Builder agent, mỗi phần một agent, lead review (đề xuất); một mình lead | Builder agent |
| `order` | Thứ tự các phần còn mở | In which order do the parts come? | Các phần xếp theo thứ tự nào? | Thứ tự đề xuất, kèm lý do; thứ tự khác | Đề xuất |
| `deadline` | Chưa được nêu | Is there a date? | Có hạn chót không? | Có; không | Không |

### Vòng 5: một đoạn ngắn

Hỏi các câu này thay cho vòng 1 đến 4 khi yêu cầu đi theo lane ngắn (`short-pieces.md`, mục 1). Chỉ hỏi những câu mà câu trả lời không thể giả định; nêu phần còn lại dưới dạng giả định.

| Id | Hỏi khi | English | Vietnamese | Lựa chọn | Mặc định |
|---|---|---|---|---|---|
| `lane` | Luôn luôn, dưới dạng một câu khẳng định | This is a short piece: I will stop for you only at the beat table with a few stills, and at the finished piece. | Đây là một đoạn ngắn: em làm gọn, chỉ dừng chờ anh/chị duyệt ở bảng nhịp kèm vài ảnh tĩnh, và ở bản hoàn chỉnh. | Xác nhận (đề xuất); quy trình đầy đủ với mọi gate | Lane ngắn |
| `autonomy` | Yêu cầu nói "tự quyết đi", hoặc owner sẽ vắng mặt | Shall I decide everything myself and show you the decisions at the end? Money, video export, heavy load and anything sent out still wait for you. | Anh/chị muốn em tự quyết hết rồi báo lại các quyết định ở cuối không? Việc tốn tiền, xuất video, chạy nặng máy và gửi bất cứ thứ gì ra ngoài vẫn chờ anh/chị. | Có, tự quyết và báo lại (đề xuất khi owner vắng mặt); dừng ở hai gate | Theo yêu cầu |
| `formats` | Đoạn phim dành cho nhiều nơi | Which formats, and which one is the master? | Cần những khung hình nào, và khung nào là chính? | Một định dạng (đề xuất); vuông 1:1 cộng dọc 9:16; cả ba cùng ngang 16:9. Một thư mục phim hiển thị từng định dạng qua bộ chuyển định dạng (tham số trang `?format=<name>` trong studio, flag `--format <name>` cho capture); layout của mỗi định dạng là công việc thêm cho từng beat | Theo nơi đăng |
| `loop` | Đoạn phim dành cho một feed, một trang hoặc một màn hình phát lặp lại | Must it loop seamlessly, the last frame running into the first? | Video có cần lặp liền mạch, khung cuối nối thẳng vào khung đầu không? | Không; có (tốn công ở chỗ nối: con trỏ, camera, nhạc) | Không |
| `trigger` | Đoạn phim là một màn tiết lộ, mở hộp, phần thưởng | Does it play by itself, or when the viewer clicks? | Video tự chạy, hay người xem bấm vào mới chạy? | Tự chạy, như một phim (đề xuất); chạy khi click (studio cho thấy một lượt chạy theo kịch bản; trang live được dựng sau) | Tự chạy |

### Vòng 6: thứ có thật

Hỏi khi phim cho thấy một sản phẩm, thương hiệu hoặc số liệu có thật. Đọc trước những gì đọc được (`thinking-and-brainstorm.md`, mục 2); hỏi những gì chỉ owner biết.

| Id | Hỏi khi | English | Vietnamese | Lựa chọn | Mặc định |
|---|---|---|---|---|---|
| `source` | Sản phẩm được nêu tên nhưng chưa biết ở đâu | Where is the real product: a website, a repository, files you send? | Sản phẩm thật nằm ở đâu: trang web, kho mã, hay tệp anh/chị gửi? | Trang web (đề xuất khi công khai); repository; các file | Địa chỉ trong yêu cầu |
| `rights` | Luôn luôn, với logo, màn hình, font, ảnh, footage | Are these yours, and may they appear in the film? | Logo, ảnh chụp màn hình, font, ảnh và video này có phải của anh/chị không, và em được đưa chúng vào video không? | Có, tất cả là của tôi; một số không phải của tôi (những cái nào); hỏi chủ sở hữu | Hỏi |
| `figures` | Phim hiển thị con số | Which figures may be shown, and where do they come from? | Những con số nào được đưa lên màn hình, và lấy từ nguồn nào? | Chỉ những số liệu công bố trên site của bạn (đề xuất); những nguồn này; không có | Chỉ số liệu đã công bố, mỗi số kèm nguồn |
| `claims` | Một lần launch, một bản phát hành, một phép so sánh | Is there anything that must not be said: a feature not yet out, a version, a competitor? | Có điều gì không được nói không: tính năng chưa ra mắt, số phiên bản, so sánh với đối thủ? | Không có gì; những điều này | Chỉ những gì nguồn nói vào ngày đó |
| `signed-in` | Màn hình nằm sau đăng nhập | Can you send me the screens that need a sign-in? I will not sign in for you. | Anh/chị gửi em ảnh chụp các màn hình cần đăng nhập được không? Em sẽ không đăng nhập hộ. | Được, dưới dạng file (đề xuất); bỏ chúng ra | Bỏ chúng ra |
| `other-brand` | Yêu cầu làm phim về một thương hiệu không phải của owner | That brand is not yours. Is this a private study, or will it be published? | Thương hiệu này không phải của anh/chị. Đây là bài tập riêng, hay sẽ đăng công khai? | Một bài tập riêng (đề xuất); đăng công khai, có sự cho phép của chủ sở hữu; dùng sản phẩm của chính bạn thay thế | Một bài tập riêng, nói rõ ở cuối |

## 5. Đọc câu trả lời

| Owner nói | Nghĩa là | Làm gì |
|---|---|---|
| Chọn đề xuất của bạn | Chỉ đồng ý ở điểm đó | Sang điểm tiếp theo |
| "Khác", kèm một nhận xét | Bạn đã bỏ sót điều gì đó | Đọc nhận xét hai lần. Nó thường nêu một nguồn mà bạn lẽ ra phải đọc |
| Hỏi ngược lại | Các lựa chọn chưa rõ | Giải thích bằng một ví dụ, hỏi lại |
| "Khoan, tôi chưa chốt ..." | Bạn đã đi trước | Dừng lại. Đừng bảo vệ phần việc đã làm. Hỏi điều gì đã chốt |
| "Nhẹ quá", "chưa đã" | Gu | Làm các ứng viên khác. Đừng đo đạc để tranh luận |
| "Cái này là đủ" | Vấn đề đã khép lại | Khép lại. Không làm thêm ứng viên |
| "Thêm ..." | Thêm | Thêm. Đừng thay thế những gì đã có |
| "Tôi chưa định nghĩa rõ ..." | Một chỉnh sửa cho cách bạn hiểu | Nhắc lại cách hiểu mới trước khi hành động |

Từ thực tế: khi được hỏi về look, owner trả lời ngoài các lựa chọn: đừng khóa một phong cách, và hãy nhớ repository đã cho xem trước đó. Bước tiếp theo đúng đắn là nghiên cứu lại repository đó. Khi được yêu cầu các transition mạnh hơn thuộc một loại nhất định, lead định chuyển phần lớn các cú cắt sang loại đó; owner trả lời rằng mong muốn là thêm vài cái, ở những thời điểm quan trọng. Sau một nhận xét, hãy hỏi: thêm vào, hay thay thế?

## 6. Sau các vòng: brief

Viết một trang và cho owner xem.

```
BRIEF
Film        <working title>
Takeaway    <one sentence>
Audience    <who, what they know>
Parts       <list, in order>
Each part   <what it must contain: for example the problem, then the idea, then where it is used>
Words       <language; how much per part; names kept in ...>
Frame       <size, where shown, safe area>
Length      <limit>
Sound       <music: source, kind; voice: yes or no>
Look        <locked or free; reference; what is fixed>
Deliverable <page or file>
Machine     <what may run>
Money       <what may be spent, how to ask>
Gates       <where the work stops for approval>

Stated by the owner:   <list>
Inferred by the lead:  <list>
Open:                  <list>
```

Một bản sửa của brief không phải là sự xác nhận nó. Sau một thay đổi, hãy cho xem lại trang đó.

## 7. Không bao giờ tự giả định

| Vấn đề | Quy tắc |
|---|---|
| Tiêu tiền | Hỏi mỗi lần, kèm giá. Được duyệt cho một lần gọi không phải là được duyệt cho lần sau |
| Export một video | Chỉ khi được yêu cầu trong cuộc hội thoại này |
| Đăng bất cứ thứ gì ra ngoài máy | Chỉ khi được yêu cầu |
| Xóa | Xem những gì đang có, nói những gì sẽ bị xóa, rồi mới xóa. Khi được bảo xóa ảnh, hãy xóa ảnh, không phải mọi thứ có dung lượng lớn |
| Thay đổi câu chữ đã duyệt | Báo nó như một thay đổi, với bản cũ và bản mới đặt cạnh nhau |
| Thứ tự các phần | Của owner. Một thay đổi muộn trong công việc là có thể và tốn công: nói rõ tốn gì |
| Rằng một công cụ trên máy phải được dùng | Các công cụ trên máy là ứng viên |
| Trình duyệt của owner | Hỏi, hoặc tìm ra từ log server |
| Upload tài liệu của owner | Không bao giờ: không màn hình, logo, file hay code nào của owner được gửi tới bất kỳ dịch vụ nào, kể cả để "làm sạch" |
| Đăng nhập | Không bao giờ thay mặt owner. Màn hình sau đăng nhập do owner gửi dưới dạng file |
| Rằng một số liệu là đúng | Mọi số liệu trên màn hình đều có nguồn trong hồ sơ (`thinking-and-brainstorm.md`, mục 2) |
| Rằng "tự quyết đi" bao gồm cả tiền, export hay gửi ra ngoài | Không bao gồm. Xem chế độ tự động trong `short-pieces.md`, mục 4 |

## 8. Từ lời owner đến quyết định

| Owner nói | Quyết định |
|---|---|
| "Cho người không có nền tảng" | So sánh từ đời thường. Không có code trên màn hình. Mỗi câu một ý |
| "Hình ảnh thật chỉn chu, giàu chuyển động" | Nhiều shot ngắn. Mỗi shot một kiểu chuyển động khác. Dành ngân sách cho các vòng polish |
| "Khớp với beat" | Một grid đo được. Sự kiện nằm trên beat. Transition ở drop |
| "Giống repository tôi cho xem" | Nghiên cứu nó; mang theo phương pháp của nó, không phải hình ảnh của nó |
| "Đừng khóa một phong cách" | Mỗi phần một look |
| "Khó đoán" | Không có template cho các phần: độ dài, thứ tự, vị trí tên khác nhau |
| "Đừng export video, nó làm nặng máy tôi" | Trang studio là sản phẩm giao. Chỉ still |
| "Bạn quyết định, để model khác dựng" | Lead không viết shot nào, kể cả shot mẫu |
| "Một video 15 giây", "làm hết sức", "một sting", "một teaser" | Lane ngắn: `short-pieces.md` |
| "Đừng hỏi tôi, tự quyết mọi thứ", "tôi đi vắng một lúc" | Chế độ tự động: các gate trở thành quyết định được ghi lại và cho xem ở cuối; các quy tắc cứng vẫn giữ nguyên |
| "Dùng UI thật của chúng tôi, không phải component chung chung", "không bịa gì cả" | Phần research của `thinking-and-brainstorm.md`, mục 2, trước mọi ý tưởng |
| "Render ra MP4 và cho tôi biết nó ở đâu" | Một yêu cầu file video trong cuộc hội thoại này, chỉ cho đoạn phim này. Làm một lần, sau cùng, sau khi các still đã đạt |
| "Gửi vào Dropbox của tôi", "nhắn link cho tôi" | Không làm khi chưa có lời của owner trong cuộc hội thoại. Nêu ở cuối như một bước đang chờ |

## 9. Trong route HyperFrames

Skill đầu vào của nó có một cuộc phỏng vấn riêng, gồm tám bước: memory trước câu hỏi, phân loại (triage), route, một vòng pitch cho các yêu cầu chưa thành hình, những thứ bắt buộc của route, hai câu hỏi về hình dạng của lượt chạy (có storyboard hay không; tự động hay có người đi cùng), một đề nghị tùy chọn về các khả năng, và bàn giao. Nó suy ra khung hình từ nơi phim được chiếu và hỏi về độ dài và góc tiếp cận kèm một đề xuất và lý do.

Khi một phim đi theo hướng đó, hãy để skill đó hỏi. Mang theo những gì đã biết, để nó không hỏi gì hai lần.

## 10. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Owner nói "khoan" | Công việc chạy trước một lần duyệt | Dừng ở gate; hỏi một câu rõ ràng |
| Owner trả lời ngoài các lựa chọn | Các lựa chọn xuất phát từ hình dung của bạn về phim | Đọc lại những gì họ nêu; hỏi lại |
| Mười câu hỏi và owner mệt | Đã hỏi những thứ tra cứu được | Hỏi những gì thuộc về owner |
| Câu trả lời cho một câu hỏi về gu bị tranh luận bằng số đo | Lead tin con số hơn tai nghe | Đưa file; để owner nghe |
| Đã tiêu tiền khi chưa được phép | Được duyệt cho một lần gọi bị hiểu là cho tất cả | Hỏi mỗi lần |
| Mong muốn "thêm cái này" của owner biến thành "chỉ cái này" | Sửa quá tay | Hỏi: thêm vào, hay thay thế? |
| Một thứ lớn bị xóa mà không ai yêu cầu | "Làm cho nhẹ hơn" bị hiểu thành "xóa những gì lớn" | Xóa những gì được nêu tên; liệt kê phần còn lại và hỏi |
| Một phiên sau hỏi lại các câu hỏi | Các câu trả lời không được ghi lại | Trạng thái project, bằng lời của owner |
