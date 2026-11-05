# Suy nghĩ và brainstorm

Làm sao đi từ một chủ đề đến một bộ phim có thể vẽ được: cần nghĩ thấu đáo những gì trước khi có bất kỳ ý tưởng nào, làm sao tìm phép so sánh và look, làm sao cho bộ phim một hình dạng theo thời gian, và làm sao đưa ra những phương án thực sự khác nhau cho owner.

Nạp file này khi: một brief đã được thống nhất mà chưa có concept nào, owner yêu cầu ý tưởng, ý tưởng của một section không hiệu quả, một shot yếu mà lý do không nằm ở tay nghề, hoặc bộ phim cho thấy một sản phẩm thật, một thương hiệu thật hay số liệu thật.

## 1. Suy nghĩ trước khi có ý tưởng

Trả lời năm câu hỏi bằng văn bản. Những ý tưởng đến trước câu trả lời thường là về một bộ phim sai.

| Câu hỏi | Một câu trả lời tốt | Một câu trả lời tồi |
|---|---|---|
| Ai xem? | "Những người làm app với một trợ lý AI và chưa từng học lập trình" | "Developer" |
| Họ mang về được gì? | "Tám cái tên, và với mỗi cái tên thì nó dùng để làm gì, để họ có thể gọi đúng tên khi nhờ trợ lý" | "Một sự hiểu biết về chủ đề" |
| Vì sao họ nên quan tâm? | "Không có cái tên, họ phải mô tả thứ đó bằng mười câu và nhận về một thứ khác" | "Nó quan trọng" |
| Cái gì có thể cho thấy mà không cần nói? | Một danh sách những thứ có hình dạng và có thể chuyển động | "Các khái niệm" |
| Hình dạng của nó theo thời gian là gì? | "Tám phần độ dài không đều trên một bản nhạc, tên của mỗi phần rơi vào chỗ nhạc rơi" | "Khoảng ba phút" |

Sau đó viết bộ phim trong một câu. Nếu câu đó cần "và" hai lần, thì đó là hai bộ phim.

## 2. Nghiên cứu thứ có thật

Một bộ phim về một sản phẩm thật, một thương hiệu thật hay số liệu thật bắt đầu từ chất liệu thật, không phải từ trí nhớ. Một phim ra mắt với một dashboard bịa ra, hay một explainer với một con số không ai truy được nguồn, đều thất bại dù nó chuyển động hay đến đâu. Làm phần nghiên cứu này trước bất kỳ ý tưởng nào, và trước khi storyboard viết bất kỳ một khẳng định nào.

Bỏ qua mục này cho một bộ phim về một ý tưởng không cần dữ kiện nào ngoài kiến thức phổ thông.

### Thu thập những gì

| Chất liệu | Từ một website | Từ một repository hoặc file của owner |
|---|---|---|
| Nó là gì và làm gì, bằng chính lời của nó | Trang chủ, các trang tính năng và bảng giá, tài liệu, changelog | README, mô tả package, thư mục tài liệu, changelog, release note |
| Các màn hình | Các trang đọc dưới dạng văn bản để lấy cấu trúc; các màn hình do lead capture từng cái một, dưới dạng still | Ảnh chụp màn hình và bản ghi màn hình của owner; chính mã nguồn của giao diện để lấy kích thước, độ bo góc và khoảng cách |
| Logo | File logo mà trang phục vụ (SVG nếu có), icon của trang | Các thư mục asset; xin owner file gốc |
| Màu sắc | Các custom property và theme color trong style của trang | Cấu hình theme hoặc style, các design token |
| Kiểu chữ | Các họ font mà style nêu tên và các font mà trang tải | Các file font và giấy phép của chúng |
| Nội dung chữ (copy) | Tiêu đề, lời hứa một dòng, nhãn nút bấm, đúng nguyên văn | Các chuỗi của giao diện và bản dịch của chúng |
| Số liệu | Những con số mà owner công bố (người dùng, nhà cung cấp, tốc độ), cùng trang chứa chúng | Fixture, benchmark, thống kê công khai mà owner chỉ tới. Không bao giờ dùng dữ liệu cá nhân |
| Số liệu cho một data explainer | Nguồn chính thức và nguồn gốc: cơ quan thống kê, các cơ quan nhà nước, bài báo khoa học đã đo nó | Một bộ dữ liệu owner đưa |

Dựng lại giao diện dưới dạng hình khối từ những gì đã capture, để nó có thể chuyển động và biến hình (morph); chỉ dùng ảnh chụp màn hình làm hình ảnh ở chỗ mà chính hình thật là bằng chứng. Một màn hình đã capture là tham chiếu cho số đo và màu sắc, không phải một texture để dán vào.

### Bản ghi nguồn

Giữ một bảng trong file trạng thái của dự án, và giữ các số liệu mà scene vẽ trong một file JSON thuộc thư mục dữ liệu của phim, mà các scene import, để mỗi số liệu chỉ được viết một lần. Mọi số liệu, logo, màn hình, kiểu chữ và dòng chữ trên màn hình đều có một hàng:

| Cột | Chứa |
|---|---|
| Cái gì | Số liệu, asset hoặc dòng chữ, đúng như nó xuất hiện trên màn hình |
| Giá trị | Với một số liệu: con số, đơn vị của nó, và nó đếm cái gì |
| Nguồn | Địa chỉ trang hoặc đường dẫn file, và những câu chữ quanh số liệu ở đó |
| Đọc ngày | Ngày nó được đọc. Các trang có thay đổi |
| Độ bất định | Với một ước tính: khoảng mà nguồn đưa ra. Nói rõ trên màn hình ở chỗ quan trọng ("khoảng", "từ ... đến") |
| Quyền | Nó thuộc về ai, và được dùng theo điều kiện gì |
| Dùng dưới dạng | Hiển thị nguyên trạng, dựng lại thành hình khối, hay chỉ dùng để đo |

Một số liệu trên màn hình mà không có hàng nào thì bị gỡ bỏ hoặc được bổ sung một hàng trước khi storyboard được duyệt. Một khẳng định về một bản phát hành (ổn định hay chưa, đã ra mắt hay mới lên kế hoạch) được kiểm với nguồn vào đúng ngày đó, không phải với những gì lead nhớ.

### Quyền sử dụng

| Chất liệu | Quy tắc |
|---|---|
| Sản phẩm của chính owner: màn hình, logo, copy, số liệu | Họ được dùng. Hỏi một lần xem chúng có được xuất hiện trong phim không |
| Thương hiệu, logo hay giao diện của một công ty khác | Một bộ phim được trình chiếu như là của chính công ty đó cần sự cho phép của công ty đó. Làm như một bài nghiên cứu riêng thì được; hãy nói rõ, và không bao giờ trình bày nó như là của công ty đó |
| Kiểu chữ | Chỉ dùng font của thương hiệu nếu giấy phép của nó cho phép nhúng; nếu không, nêu tên một font miễn phí gần giống thay thế và nói rõ |
| Ảnh, footage, nhạc, hiệu ứng âm thanh | Của chính owner, hoặc theo một giấy phép cho phép việc sử dụng đó. Ghi lại giấy phép |
| Con người | Không dùng hình ảnh hay tên của một người thật như thể họ xác nhận/ủng hộ một điều gì đó |

### Không có gì rời khỏi máy

Phần nghiên cứu đọc các trang công khai và file của owner. Nó không gửi gì đi: không có màn hình, file, logo hay đoạn code nào của owner được upload lên bất kỳ dịch vụ nào (công cụ hình ảnh, công cụ xoá nền, công cụ nhận dạng font, công cụ chuyển đổi), không đăng nhập thay mặt owner, và không tạo tài khoản nào. Các màn hình nằm sau một lớp đăng nhập thì lấy từ owner dưới dạng file. Các bản capture màn hình là still, từng cái một, do lead thực hiện, như mọi lần capture khác.

Buổi phỏng vấn có một vòng cho việc này: `interview.md`, mục 4, vòng 6.

## 3. Từ một chủ đề đến hình ảnh

Làm theo từng phần. Điền một hàng cho mỗi phần trước khi vẽ bất cứ thứ gì.

| Cột | Chứa | Phép thử |
|---|---|---|
| Ý tưởng, trong một câu đơn giản | Phần đó dạy gì, không dùng thuật ngữ chuyên ngành nào | Một người ngoài ngành có thể nhắc lại được |
| Vấn đề | Điều gì hỏng khi không có ý tưởng đó | Nó gây đau, và có thể cho thấy được |
| Phép so sánh | Một thứ trong chính đời sống của người xem hoạt động theo cùng cách | Xem mục 4 |
| Sự vật | Một vật duy nhất trong phép so sánh CHÍNH LÀ ý tưởng | Có thể chỉ tay vào nó. Nó sẽ mang màu signal |
| Nơi họ gặp nó | Ý tưởng trong chính công việc của người xem | Họ đã từng thấy màn hình này |
| Phải cho thấy | Những gì hình ảnh phải làm rõ | Một dòng |
| Không bao giờ được cho thấy | Những gì sẽ biến nó thành hình ảnh của một ý tưởng lân cận | Một dòng cho mỗi ý tưởng lân cận |

Hai cột cuối là hai cột hay bị bỏ qua nhất, và cũng là hai cột gây tốn kém nhất khi bị bỏ qua. Một hình ảnh có thể đẹp mà lại dạy ý tưởng của hàng xóm. Xem phần kiểm nội dung trong `quality-gates.md`.

## 4. Tìm phép so sánh

Một phép so sánh là tốt khi nó vượt qua tất cả các phép thử này.

| Phép thử | Vì sao |
|---|---|
| Nó đến từ đời sống hằng ngày của người xem | Không có gì phải giải thích trước |
| Nó có cùng cấu trúc với ý tưởng, không chỉ cùng bề mặt | "Các lớp ốp quanh một chiếc điện thoại mà để nguyên chiếc điện thoại như cũ" có cấu trúc của việc bọc lại. "Topping thêm vào một ly đồ uống" có cấu trúc của việc thêm vào, vốn là một ý tưởng khác |
| Nó vẽ được, và nó chuyển động được | Một phép so sánh chỉ là một câu nói thì là một caption |
| Nó có một trạng thái không có ý tưởng và một trạng thái có ý tưởng | Vấn đề và câu trả lời đều là hình ảnh |
| Một vật trong đó chính là ý tưởng | Cái adapter, cái đòn bẩy, cái cửa sập. Nếu không có gì để chỉ tay vào, phép so sánh chỉ là một bầu không khí |
| Không phần nào khác dùng thế giới của nó | Hai phần cùng gọi món ở một quầy sẽ bị nhầm lẫn với nhau |
| Nó đúng | Một hình vẽ được tin theo đúng những gì nó vẽ. Một sợi dây nối sai chỉ vì bức hình sẽ dạy điều sai |
| Owner nhận ra nó | Owner biết họ giải thích chủ đề như thế nào. Hãy hỏi các phép so sánh của chính họ trước |

Cách tìm một phép so sánh:

1. Hỏi owner họ giải thích nó thế nào khi đi dạy. Phép so sánh của họ đã được kiểm chứng.
2. Nêu cấu trúc bằng những từ trần trụi: "một thứ, nhiều người dùng", "một yêu cầu vào, một thứ được làm ra", "một thay đổi được báo cho mọi người đã đăng ký".
3. Liệt kê mười nơi trong đời sống hằng ngày có cấu trúc đó. Ba cái đầu tiên là những gì ai cũng nghĩ tới. Hãy nhìn vào những cái còn lại.
4. Với mỗi cái, nêu tên sự vật, trạng thái có vấn đề và trạng thái đã được giải quyết. Bỏ những cái thiếu một trong ba thứ đó.
5. Đối chiếu những cái còn lại với phép so sánh của các phần khác.

## 5. Tìm look

Look đi theo phép so sánh. Mỗi phép so sánh sống trong một thế giới có những vật in ấn, màn hình và chất liệu riêng của nó: xem `art-styles.md`. Thế giới của một nhà bếp có phiếu gọi món và bảng thực đơn. Thế giới của một thợ may có rập giấy. Hãy lấy ngôn ngữ hình ảnh từ đó, mỗi phần một cái.

### Một phong cách lấy từ một ảnh tham chiếu

Owner thường đính kèm một ảnh và nói "chỉ dùng cái này làm phong cách thôi". Hãy đọc nó thành những quy tắc mà builder có thể làm theo, và cho owner xem các quy tắc đó trước khi dựng, vì một cách đọc là một sự diễn giải.

| Đọc từ ảnh | Viết thành |
|---|---|
| Màu sắc | Một bảng màu năm đến bảy màu, mỗi màu có vai trò của nó (nền, mực, nhấn, sáng, bóng), lấy từ ảnh, không phải đoán |
| Ánh sáng và phần hoàn thiện | Ánh sáng đến từ đâu, cứng tới mức nào, grain, glow, halation, viền màu: các thiết lập của post chain |
| Nét và bề mặt | Độ dày nét và nét có rung hay không; tô phẳng, có đổ bóng hay có texture |
| Chữ | Họ font và nhóm độ đậm của nó, kiểu chữ hoa/thường, tracking; font miễn phí gần nhất nếu font trong ảnh không miễn phí |
| Bố cục | Đối xứng hay không, bao nhiêu khoảng trống, đường chân trời nằm ở đâu |
| Chuyển động, nếu tham chiếu là một bộ phim | Tốc độ cắt, kiểu easing, cách mọi thứ xuất hiện |

Lấy cách thể hiện, không lấy nội dung: chủ thể, nhân vật và chữ trong ảnh không được sao chép vào phim. Một tham chiếu là tác phẩm nghệ thuật của ai đó chỉ là nguồn của cách thể hiện; hãy nói rõ điều này trong bản ghi về look.

## 6. Hình dạng theo thời gian

Nhạc cho bộ phim bộ khung của nó. Đọc `music-and-beat.md` để biết về bản đồ của một bản nhạc. Sau đó:

| Quyết định | Dựa theo |
|---|---|
| Mỗi phần dài bao lâu | Các câu nhạc (phrase). Các phần có độ dài không đều, phần ngắn nhất khoảng một nửa phần dài nhất |
| Vấn đề của một phần đặt ở đâu | Chỗ nhạc đang dồn lên (build) hoặc không có trống |
| Ý tưởng rơi vào đâu | Vào một drop, hoặc vào bar đầu tiên của một câu nhạc |
| Câu chữ được đọc ở đâu | Chỗ trống ngừng |
| Phần nào đặt ở đâu | Owner quyết định thứ tự. Đề xuất thứ tự mà các phần dễ theo dõi nhất, và nói rõ nhạc mang lại gì cho mỗi vị trí |

### Đừng kể mọi phần theo cùng một cách

Người xem nhận ra khuôn mẫu ở phần thứ ba. Các cách để phá nó:

| Cách | Ví dụ |
|---|---|
| Độ dài không đều | Tám bar cho phần này, mười bốn cho phần khác |
| Thứ tự kể khác | Mở đầu bằng ý tưởng đang vận hành, rồi tua lại về cuộc sống khi chưa có nó |
| Mở đầu bằng một câu đùa | Một cỗ máy chia ra sai tổ hợp |
| Một góc nhìn khác | Ngôi thứ nhất: chính ngón tay của người xem trên màn hình |
| Dời cái tên | Ở đầu, cùng với ý tưởng, hoặc là từ cuối cùng |
| Để nhạc quyết định | Hai bar im lặng trở thành hai bar chờ đợi |
| Một nhịp độ cắt khác | Một phần với các shot dài, một phần mỗi bar một shot |
| Có chữ ở đây, không chữ ở kia | Một ý tưởng được cho thấy mà không có câu nào |

Những gì mỗi phần chứa thì giữ nguyên. Cách kể và thứ tự thì thay đổi.

## 7. Brainstorm

### Phân kỳ (diverge)

Tạo ít nhất ba hướng đi cho cả bộ phim. Chúng phải khác nhau theo một trục, không phải ở chi tiết.

| Trục | Một đầu | Đầu kia |
|---|---|---|
| Điều gì giữ bộ phim liền một khối | Một thế giới xuyên suốt | Mỗi phần một thế giới, giữ lại với nhau bằng bảng màu, chữ và nhịp điệu |
| Điều gì mang ý nghĩa | Đồ vật và phép so sánh | Chỉ chữ; sơ đồ; một nhân vật |
| Quan hệ với nhạc | Mọi sự kiện đều trên grid | Nhạc như một lớp nền |
| Giọng điệu | Khô và chính xác | Vui đùa, hài hước |
| Góc nhìn | Nhìn sự vật từ bên ngoài | Ngôi thứ nhất |
| Hình thức | Tiểu luận | Một hình thức vay mượn: một công thức nấu ăn, một sách hướng dẫn, một phi vụ trộm, một phim thiên nhiên |

Cố ý làm một trong các hướng đi trở nên khó xảy ra. Nó hiếm khi được chọn và thường cho hướng được chọn mượn ý tưởng hay nhất của nó.

Các cách đẩy một ý tưởng đi xa hơn:

| Cách | Câu hỏi |
|---|---|
| Lấy nó đi | Cuộc sống trông thế nào khi không có nó? |
| Đẩy nó cho đến khi vỡ | Sẽ ra sao nếu có một nghìn cái như vậy? |
| Đổi thang tỉ lệ | Sẽ ra sao nếu nó to bằng một thành phố, hoặc nhỏ bằng một cây kim? |
| Hiểu phép so sánh theo nghĩa đen | Sẽ ra sao nếu các lớp thực sự bọc lấy từ ngữ? |
| Bắt đầu từ nhạc | Điều gì xảy ra ở drop? Làm ngược lại từ đó |
| Bắt đầu từ poster | Nếu bộ phim là một still duy nhất, đó sẽ là still nào? |
| Mượn một hình thức | Một chương trình dạy nấu ăn sẽ giải thích điều này thế nào? |
| Thêm một quy tắc | Chỉ một hình khối. Không chữ. Mọi thứ trên giấy |

### Mô tả

Mỗi hướng đi có cùng một mô tả ngắn, để có thể so sánh chúng.

```
DIRECTION <letter>: <name>
In one sentence   <what the film is>
The first ten seconds   <what is seen and heard>
One part, told    <the part that shows the direction best, in four lines>
Held together by  <what stays the same>
Music             <kind, tempo, relation>
Strong at         <what it does best>
Risk              <where it may fail>
Cost              <what is dear to build>
```

### Hội tụ (converge)

Chấm điểm các hướng đi theo những gì brief yêu cầu. Thêm một dòng lý do cho mỗi điểm số; một con số đơn thuần không thuyết phục được ai.

| Tiêu chí | Hỏi |
|---|---|
| Rõ ràng với khán giả này | Người xem trong brief có theo kịp không? |
| Các phần tách biệt nhau | Có hai phần nào có thể bị nhầm lẫn không? |
| Hợp với nhạc | Nó có dùng các đoạn build, drop và break không? |
| Vẽ được bằng code | Không cần footage, không cần vẽ tay |
| Mới mẻ | Người xem đã từng xem bộ phim này chưa? |
| Chi phí | Số vòng của builder, shader, mô phỏng |

Đưa các hướng đi cho owner dưới dạng các lựa chọn, hướng được khuyến nghị đứng đầu kèm lý do. Lựa chọn của owner là một cổng kiểm: không có gì được dựng trước nó.

Sau khi chọn, các phép so sánh được đưa cho owner dưới dạng một bảng, từng phần một. Một bảng đã được duyệt là giấy phép để viết storyboard. Nó không phải là giấy phép để dựng.

## 8. Bản mẫu

Trước khi bộ phim được dựng, một phần được dựng làm bản mẫu, và owner xem nó.

| Chọn phần mà | Vì |
|---|---|
| Owner hiểu rõ nhất | Họ có thể đánh giá nó chỉ trong một cái nhìn. Phép so sánh của chính họ là lựa chọn tự nhiên |
| Có dải hình ảnh rộng nhất | Nó kiểm tra được nhiều nhất phần kit |
| Không phải phần đầu tiên của phim | Phần đầu tiên mang phần chuyển giao từ tiêu đề, vốn là một nhiệm vụ riêng |

Bản mẫu chốt look, mật độ sự kiện, cỡ chữ, và cường độ của các transition. Nó cũng cho thấy các builder làm được gì, điều này thay đổi những gì có thể yêu cầu ở họ.

## 9. Khi một shot yếu

Trước khi gửi trả một shot để sửa tay nghề, hãy hỏi xem lỗi có nằm ở ý tưởng không.

| Câu hỏi | Nếu câu trả lời là không |
|---|---|
| Có một sự kiện mỗi beat, và không nhiều hơn không? | Bỏ bớt sự kiện |
| Mắt có biết phải nhìn vào đâu không? | Một thứ mang màu signal; phần còn lại lùi ra sau |
| Frame đầu tiên có sức nặng không? | Mở đầu vào chủ thể |
| Nó có thể bị gọi bằng tên của một phần lân cận không? | Nội dung sai. Tay nghề sẽ không giúp được |
| Nó có đáp lại những gì nhạc làm ở đây không? | Dời sự kiện tới beat đòi hỏi nó |
| Khung hình có được tận dụng không? | Bố trí nó cho khung hình này, không phải cho một khung hình khác |
| Owner có nhận ra cái họ đã duyệt không? | Có gì đó đã mất trong một lần làm lại. Mang nó trở lại |
| Có thứ gì có thể bỏ đi không? | Bỏ nó đi |

## 10. Trong route HyperFrames

Skill điểm vào của nó chạy một vòng pitch cho những yêu cầu chưa thành hình: năm concept trên năm hướng khác nhau, ít nhất hai trong số đó cố ý khó xảy ra. Skill creative của nó có hướng dẫn về xương sống của một câu chuyện, về lời dẫn và về việc điều phối beat. Khi một bộ phim đi theo hướng đó, hãy dùng vòng pitch của nó thay cho mục 7, và giữ các mục 1 đến 4 của file này: chúng nói về chủ đề, không phải về công cụ.

## 11. Lỗi thường gặp

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Ba hướng đi thực ra là một hướng đi với ba màu | Chúng khác nhau ở chi tiết | Làm cho chúng khác nhau theo một trục |
| Phép so sánh giải thích bề mặt chứ không phải ý tưởng | Nó được chọn vì vẻ ngoài | Nêu cấu trúc bằng những từ trần trụi trước |
| Hai phần bị nhầm lẫn | Chúng dùng chung một thế giới, một đạo cụ hay một ví dụ | Mỗi phần một thế giới; kiểm bảng ranh giới |
| Mọi phần đều có cảm giác giống nhau | Một khuôn mẫu | Đổi độ dài, thứ tự, góc nhìn, vị trí của cái tên |
| Owner dừng công việc lại | Việc dựng bắt đầu sau bảng, trước storyboard | Bảng, storyboard, animatic, bản mẫu, rồi mới đến phần còn lại |
| Một shot được trau chuốt hai lần mà vẫn sai | Lỗi nằm ở nội dung | Nội dung được kiểm trước tay nghề |
| Bộ phim nói về chủ đề chứ không dành cho người xem | Hai câu hỏi đầu tiên bị bỏ qua | Trả lời chúng bằng văn bản |
| Ý tưởng là cái đầu tiên mà ai cũng nghĩ ra | Danh sách dừng ở ba | Mười, rồi mới chọn |
| Một phim ra mắt cho thấy một dashboard mà sản phẩm không có | Giao diện được tưởng tượng ra, không phải được capture | Mục 2: thu thập các màn hình thật trước |
| Một số liệu trên màn hình không truy được nguồn | Nó đến từ trí nhớ hoặc từ một bản tóm tắt | Bản ghi nguồn, mục 2 |
| Bộ phim sao chép ảnh tham chiếu thay vì cách thể hiện của nó | Chủ thể và bố cục của nó bị lấy đi, chứ không phải các quy tắc của nó | Mục 5: đọc ảnh thành bảng màu, ánh sáng, nét, chữ và bố cục |
