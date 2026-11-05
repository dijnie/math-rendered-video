# Camera

Một catalogue những gì camera có thể làm trong một phim vẽ bằng code: nó đứng ở đâu, nó di chuyển ra sao, và mỗi lựa chọn khiến người xem cảm thấy gì. File cũng đưa ra các quy tắc giữ cho camera đa dạng, đúng beat và dễ đọc.

Nạp file này khi: viết trường `camera` của các shot trong storyboard, brief cho một builder, đánh giá vì sao một chuỗi shot cảm thấy phẳng lặng, hoặc thêm một move (chuyển động camera) vào kit dùng chung.

## 1. Mô hình

| Quy tắc | Ý nghĩa |
|---|---|
| Camera là dữ liệu | Một pose là một bản ghi nhỏ. Nó được tính từ thời gian và không từ thứ gì khác: cùng một beat luôn cho cùng một pose |
| Shot tự ghi ra các pose của nó | Builder đặt tên vài pose (rộng, vào chi tiết, từ trên xuống) và nói camera rời đi tới mỗi pose ở beat nào và move kéo dài bao lâu |
| Move được căn theo beat | Chúng bắt đầu trên một beat và kéo dài một số beat, đọc từ clock của shot |
| Các move cộng dồn | Camera của một shot là pose của nó ở beat này, nhân với một punch, cộng một shake, cộng một drift. Mỗi thứ là một hàm thuần nhỏ |
| Không có camera engine | Engine không biết gì về camera. Kit cung cấp các mảnh, và mỗi shot tự lắp camera của riêng nó. Đây là điều cho phép mỗi shot di chuyển khác nhau |

Hai loại camera:

| Camera | Pose | Dùng cho |
|---|---|---|
| Phẳng | Điểm của thế giới ở tâm màn hình, một mức zoom, một góc roll | Hình vẽ, chữ, giao diện, bản đồ: bất cứ thứ gì vẽ trên một mặt phẳng |
| Trong không gian | Một vị trí, điểm được nhìn tới, một field of view, một góc roll | Model, hình vẽ nét trong phối cảnh, shader ray marching |

Từ thực tế: phim tham chiếu mà owner khen về camera đa dạng hoàn toàn không có hệ thống camera nào. Mỗi cảnh tự viết các pose của nó. Sự đa dạng đến từ sự tự do đó, và từ một quy tắc rằng không có hai cảnh liên tiếp nào di chuyển giống nhau.

## 2. Camera đứng ở đâu

### Cỡ shot

| Cỡ | Cho thấy | Dùng |
|---|---|---|
| Cực rộng | Cả thế giới, chủ thể nhỏ bé trong đó | Quy mô, sự cô đơn, "tất cả những thứ này" |
| Rộng | Chủ thể và nơi chốn của nó | Cái nhìn đầu tiên vào một nơi mới; cái nhìn cuối cùng để tổng kết |
| Trung | Chủ thể, chiếm nửa khung hình | Hành động giữa hai thứ |
| Cận | Chủ thể lấp đầy khung | Thứ quan trọng lúc này |
| Cực cận | Một chi tiết: một cái ghim, một nút bấm, một chữ cái | Khoảnh khắc tiếp xúc; điểm bắt đầu của một cú kéo lùi |
| Insert | Một chi tiết hiện trong một hai beat, rồi quay lại | "Nhìn cái này" |

### Góc máy

| Góc | Người xem cảm thấy | Dùng |
|---|---|---|
| Ngang tầm, nhìn thẳng | Trung tính, như một trang giấy | Giao diện, biểu mẫu, sơ đồ, chữ |
| Từ trên, nhìn thẳng xuống (plan) | Nắm quyền kiểm soát, một cái nhìn tổng quan | Bản đồ, mặt bằng, bàn, đám đông, lộ trình |
| Cao, nhìn xuống | Chủ thể nhỏ, hoặc được thấy trọn vẹn | Model trên bàn, một thành phố |
| Thấp, nhìn lên | Chủ thể lớn, mạnh mẽ | Một bức tường đổ xuống, một vật thể chính, một đám đông bóng đen |
| Ngôi thứ nhất | "Đây là tôi" | Một ngón tay trên màn hình, chờ đợi, thử nghiệm |
| Xuyên qua một thứ gì đó | Nhìn vào từ bên ngoài | Qua thành một chiếc cốc, một ô cửa sổ, một khe hở giữa hai tờ giấy |
| Mặt cắt | Vật bị cắt mở, nhìn từ bên cạnh | Ngôi nhà, máy móc, bên trong một đầu nối |
| Nghiêng (roll) | Bất an, năng lượng | Vấn đề, căng thẳng, đoạn build trước một drop |
| Ba phần tư | Có chiều sâu mà không kịch tính | Đồ vật, card trên bàn |
| Isometric | Một thế giới nhỏ, gọn gàng | Hệ thống nhìn trọn vẹn |
| Qua vai | Cùng một người, nhìn vào thứ họ nhìn | Hai nhân vật đối mặt nhau; một nhân vật trước màn hình. Bờ vai lớn, mềm và tối ở một góc khung |

### Ống kính

| Ống kính | Trông như | Dùng |
|---|---|---|
| Field of view rộng, ở gần | Phối cảnh mạnh, tiền cảnh lớn | Tác động mạnh, một thứ lao về phía người xem |
| Field of view hẹp, ở xa | Phẳng, xếp chồng, tĩnh lặng | Sản phẩm, so sánh đặt cạnh nhau |
| Orthographic | Hoàn toàn không có phối cảnh | Mặt bằng, thế giới isometric, bản vẽ kỹ thuật |
| Độ sâu trường ảnh nông | Một mặt phẳng nét | Một mô hình thu nhỏ; dẫn mắt. Tốn kém: dùng blur theo độ sâu một cách tiết kiệm |

Một thay đổi field of view được blend theo tiêu cự, vì đó là thứ mắt theo dõi. Blend trực tiếp góc nhìn trông không đều.

Khi một prompt nêu một ống kính tính bằng milimét, nó có nghĩa là field of view của ống kính đó trên một máy full-frame, có ảnh 36 x 24 mm. `Cam3` nhận field of view dọc tính bằng độ: hai lần arc tangent của nửa chiều cao khung tính bằng milimét chia cho tiêu cự. Trong khung ngang, chiều cao là 24 mm; trong khung dọc, máy đặt nằm nghiêng và chiều cao là 36 mm.

| Ống kính | Field of view dọc, 16:9 | Field of view dọc, 9:16 | Cảm giác |
|---|---|---|---|
| 24 mm | 53 độ | 74 độ | Rộng: không gian, một căn phòng, phối cảnh mạnh gần ống kính |
| 35 mm | 38 độ | 54 độ | Con mắt phim tài liệu, một người trong nơi chốn của họ |
| 50 mm | 27 độ | 40 độ | Tự nhiên, gần với mắt người |
| 85 mm | 16 độ | 24 độ | Chân dung: khuôn mặt, nền mềm và phẳng |

### Độ sâu trường ảnh mà không tốn kém

Một blur thật theo độ sâu trong cảnh 3D rất tốn kém và không có trong starter. Trong một hình vẽ trên các layer 2D ở những độ sâu được chọn, cách rẻ là cách mà một máy quay phim tự tạo ra: mỗi layer được blur theo khoảng cách của nó tới mặt phẳng lấy nét. Vẽ một layer ở xa vào một `Layer2D` tạo với backing scale thấp (tham số thứ ba của constructor, ví dụ 0.25): nó được vẽ ở một phần tư độ phân giải và trông mềm khi đặt lên khung. Một cú rack focus (chuyển nét) là mặt phẳng lấy nét được key theo beat, với hai phiên bản của các layer (nét và mềm) được blend theo nó. Điều này chưa được thử trong một still. Canvas filter (`filter = 'blur(...)'`) cũng làm blur, nhưng Safari không có, nên đừng dựa vào chúng cho một phim mà owner xem trên Safari.

## 3. Các move

Các cột: **Kit** nêu tên helper của starter (`src/scenes/parts/kit-camera.ts`, `kit-frame.ts`), hoặc nói rằng shot tự viết nó bằng các pose.

### 3.1 Tĩnh và gần như tĩnh

| Move | Người xem cảm thấy | Dùng | Kit |
|---|---|---|---|
| Khóa cứng (locked off) | Nghỉ ngơi; chú ý vào những gì chuyển động trong khung | Sau một chuỗi chuyển động; bất cứ khi nào cần đọc chữ; khi điểm mấu chốt là có thứ gì đó KHÔNG chuyển động | một pose |
| Drift (trôi) | Khung hình sống động | Bên dưới một shot dài mà nếu không sẽ đứng hình | một key với `over` dài và ease tuyến tính |
| Thở theo tiếng kick | Hình có nhịp đập | Các phrase drop | `pushOnBeat`, mức dưới 0.03 |
| Cầm tay | Có người đang cầm máy | Ngôi thứ nhất, tư liệu | noise có seed trên pose, nhỏ |

### 3.2 Tiến tới và lùi ra

| Move | Người xem cảm thấy | Dùng | Kit |
|---|---|---|---|
| Push in (đẩy vào) | Sự chú ý siết lại | Hướng tới thứ sắp trở nên quan trọng | các pose với `camAt` hoặc `cam3At` |
| Pull out (kéo ra) | Toàn cảnh hiện ra; nhẹ nhõm, hoặc sợ hãi trước quy mô của nó | Các màn tiết lộ; sự tăng trưởng vô tận | các pose |
| Punch | Một cái gật đầu trên beat | Một cú đánh, một cú đáp, một tên xuất hiện | `punch` |
| Step in (bước vào) | Camera lập tức chiếm một vị trí mới và lắng lại, như một vật có trọng lượng | Tiến gần thêm một bước mỗi beat hoặc mỗi mục | `stepIn` |
| Wind-up (lấy đà) | Camera ngả ra sau, rồi lao đi | Trước bất kỳ move nào cần đánh mạnh | `windUp` |
| Crash zoom | Báo động | Vào một chi tiết, một lần trong một phim | các pose, `over` ngắn, vệt nhòe do shot vẽ |
| Giật lùi | Bị hất văng ra | Một thất bại; bước từ một chi tiết ra một mớ hỗn độn | các pose, `over` rất ngắn |
| Dolly zoom | Mặt đất sụp xuống | Một lần, cho một khoảnh khắc nhận ra | vị trí và field of view di chuyển ngược nhau |
| Lao vào (dive) | Rơi vào trong một vật | Phần đầu của một cú zoom vào chi tiết | các pose, blend đều theo scale với `camMix` |

### 3.3 Ngang qua

| Move | Người xem cảm thấy | Dùng | Kit |
|---|---|---|---|
| Pan, truck | Đọc dọc theo | Dọc một đường, một băng chuyền, một cột, một hàng trạm | các pose |
| Tilt, rise (ngửa, nâng lên) | Nhìn lên hoặc xuống một vật | Xuống một tờ giấy dài, lên một tòa tháp | các pose |
| Rơi | Rơi xuống cùng chủ thể | Xuống một cuộn giấy không bao giờ hết | các pose |
| Whip | Giật phắt sang chỗ khác | Giữa hai trạm trong một shot | `whip`, cũng cho ra mức độ nhòe |
| Follow (bám theo) | Ở lại cùng chủ thể | Một thứ đang di chuyển: một chiếc cốc trên băng chuyền, một dòng điện trong dây cáp | `follow`: camera ở chỗ chủ thể vừa ở một lúc trước, nên chủ thể dẫn đầu |
| Lead (đi trước) | Đến trước chủ thể | Một marker di chuyển tới trạm tiếp theo nửa beat trước thứ nó đánh dấu | các pose đi trước chủ thể |
| Snap giữa các khung | Một cú cắt mà không cắt | Hai góc nhìn của một thế giới trong một shot, trên một beat mạnh | một key với `over: 0` |

### 3.4 Vòng quanh

| Move | Người xem cảm thấy | Dùng | Kit |
|---|---|---|---|
| Orbit | Vật là thật; nó có mặt sau | Giới thiệu một vật thể | `orbit` |
| Một vòng xoay dừng phắt | "Nó đây rồi" | Sự xuất hiện của vật thể chính | `orbit` với một ease kết thúc gắt |
| Arc (vòng cung) | Di chuyển vòng quanh trong khi tiến lại gần | Từ mặt bên của một vật tới mặt chính của nó | các pose |
| Roll theo bậc | Bất an tăng dần | Một đoạn build; một vấn đề tệ hơn qua mỗi beat | `rollSteps` |
| Xoay quanh một điểm | Chóng mặt | Hài hước, một thay đổi góc nhìn | roll quanh tiêu điểm |
| Crane | Rời khỏi mặt đất | Từ bên trong một cảnh lên mặt bằng của nó | các pose; hình vẽ nghiêng phẳng ra |
| Nghiêng phẳng | Một góc nhìn biến thành một sơ đồ | Từ một bức tranh tới mặt bằng giải thích nó | các pose |

### 3.5 Xuyên qua

| Move | Người xem cảm thấy | Dùng | Kit |
|---|---|---|---|
| Fly-through (bay xuyên qua) | Hành trình | Qua một nhà kho, một đường hầm, một thành phố | các pose trong không gian; với shader dùng `rayUniforms` và `setRayUniforms` |
| Qua một lối mở | Đi vào | Qua một chữ cái, một cánh cửa, một khe hở: xem các transition trong thế giới | các pose, với transition của engine |
| Qua một mặt cắt | Đi vào bên trong | Vào mặt cắt của một vật đã bị xẻ ra | các pose |
| Hành trình qua các thang đo | Thế giới trong thế giới | Từ một chi tiết tới thứ chứa nó, và tiếp nữa | `scaleCam`; xem mục 3.7 |
| Rượt đuổi trên không | Bay cùng chủ thể | Một chiếc máy bay, một con chim, một con rồng, một trận không chiến trên biển | `follow` có độ trễ, một roll nghiêng vào mỗi khúc cua (roll theo gia tốc ngang của đường bay, trễ một beat), đường chân trời nghiêng theo, camera ở hơi cao và phía sau |
| Parallax slide | Chiều sâu trong một thế giới phẳng | Một phong cảnh vẽ theo layer, một diorama giấy | các pose của camera phẳng; mỗi layer di chuyển bằng camera nhân với hệ số độ sâu riêng (layer xa di chuyển ít hơn) |

### 3.6 Cú đánh

| Move | Người xem cảm thấy | Dùng | Kit |
|---|---|---|---|
| Shake (rung) | Một cú va | Khi thứ gì đó trong shot va vào thứ gì đó | `shake`, `shakes` |
| Jolt (giật) | Một lần dịch chuyển gắt | Mỗi nhát cắt của một lưỡi dao, mỗi cú dập | một shake ngắn |
| Freeze (đóng băng) | Thời gian ngừng lại | Khoảnh khắc tiếp xúc, trước khi vỡ | giữ beat |

Một shake giống nhau cho mọi sample của một frame, nên frame bị dịch chuyển chứ không bị nhòe.

### 3.7 Xuyên các thang đo trong một take

Shot "powers of ten" (lũy thừa của mười): từ một chiếc bàn xuống tới một nguyên tử của con chip bên trong máy tính, từ một sườn đồi ra tới vũ trụ quan sát được, trong một cú zoom liền mạch. Nó thường được yêu cầu và thất bại theo ba cách: cú zoom vội vàng hoặc bò chậm, các thế giới không nối được với nhau, và các con số hết độ chính xác ở đầu xa. Chưa thứ nào ở đây được dựng trong một phim.

| Phần | Quy tắc |
|---|---|
| Các thế giới lồng nhau | Hành trình là một chuỗi thế giới (bàn, vỏ máy, chip, die, lõi, dây dẫn, transistor, mạng tinh thể, nguyên tử), mỗi thế giới vẽ theo đơn vị riêng của nó để các con số giữ gần 1. Nó không phải một model khổng lồ: mỗi thế giới là một hình vẽ riêng, được đi vào ở thang đo mà nó cần |
| Góc nhìn là một con số | Hành trình đang ở đâu là một số `m`: log10 của số mét mà chiều cao khung bao phủ. Một chiếc bàn khoảng 0, một con chip -2, một transistor -7, một nguyên tử -10; Trái Đất 7, hệ Mặt Trời 13, thiên hà 21, vũ trụ quan sát được khoảng 27 |
| Di chuyển theo thập phân | Key `m` theo beat với `keys` của `src/engine/util.ts` và một ease tuyến tính: cùng một số bậc thập phân trên mỗi beat đọc như tốc độ không đổi. Blend chính cú zoom, không phải logarit của nó, sẽ vội ở một đầu. Để dừng ở một thế giới, key cùng một `m` hai lần: hành trình dừng lại trong khi có gì đó xảy ra ở đó, rồi đi tiếp |
| Trên beat | Một bậc thập phân mỗi beat hoặc mỗi bar, theo tempo và số lượng thế giới. Đến các thế giới ở downbeat; thế giới cuối cùng, hoặc màn tiết lộ, ở drop |
| Mỗi thế giới ở thang đo riêng | `scaleCam(m, world)` (`src/scenes/parts/kit-camera.ts`) cho camera phẳng của một thế giới ở góc nhìn `m`, và độ mờ đục của nó; `null` khi thế giới không được vẽ. Một `ScaleWorld` chứa `size`, log10 của số mét mà một đơn vị của nó bằng, khoảng `from` và `to` của các góc nhìn mà nó được vẽ, và một `fade` tính theo bậc thập phân. Vẽ mỗi thế giới với điểm mà hành trình hướng tới đặt ở gốc tọa độ |
| Bàn giao | Các thế giới cạnh nhau chồng lên nhau khoảng một bậc thập phân. Trong vùng chồng, thế giới ngoài hiển thị thế giới trong như một chi tiết, vẽ đủ tốt để đọc được ở cỡ đó, và thế giới trong bắt đầu tự vẽ khi chi tiết đó lấp một phần đáng kể của khung. Vào lúc bàn giao, hai thế giới phải khớp về vị trí, hình dạng và màu sắc. Ở chỗ không thể (một bức ảnh vào một hình vẽ, một khối đặc vào một mạng tinh thể), hãy fade qua vùng chồng, hoặc giấu sự thay đổi: qua một thấu kính, kính, một khe hở, một tia sáng lóe, sương mù, một khoảnh khắc tối |
| Độ chính xác | Card đồ họa tính với single float, khoảng bảy chữ số. Một thế giới dựng theo mét, nhìn bởi một camera cách một điểm một nanomet và điểm đó cách gốc một mét, sẽ rung và rách. Giữ mỗi thế giới theo đơn vị riêng gần 1, đặt gốc tọa độ ở điểm của hành trình, cho mỗi thế giới 3D near plane và far plane riêng (near khoảng một phần nghìn far), và trong shader tính vị trí tương đối với camera |
| Trong 3D | Mỗi thế giới là một scene hoặc group three.js riêng, được scale để nó trải khoảng 1 đến 100 đơn vị khi ở trên màn hình. Khoảng cách của camera tới điểm của hành trình là một số cố định các đơn vị của thế giới đó nhân 10 mũ (`m` trừ `size` của thế giới). Chỉ vẽ các thế giới của lần bàn giao hiện tại |
| Một thước đo | Một chỉ số thang đo (1 m, 10 cm, 1 mm, ...) đi theo `m` cho người xem biết chuyện gì đang xảy ra, và là thứ duy nhất đứng yên. Bước giá trị của nó theo frame clock |
| Chia thành shot | Một take, nhiều builder: cắt nó thành các shot vài bar, mỗi shot sở hữu một thế giới hoặc một cặp. Mọi shot đọc cùng một đường cong `m` từ một file của lead, key theo beat của track (`f.beat`), không phải của shot. Việc bàn giao giữa hai thế giới xảy ra bên trong một shot, do builder của nó vẽ; cú cắt giữa hai shot rơi vào chỗ chỉ có một thế giới trên màn hình, với loại `travel` trong danh sách shot, để engine không làm gì ở cú cắt và các frame ở hai bên phải khớp nhau. Kiểm tra bằng một still ở mỗi bên của mọi cú cắt |
| Một vòng lặp | Một cú zoom vô tận có lặp kết thúc ở một thế giới chính là thế giới đầu tiên, ở thang đo mà phim bắt đầu |
| Thế giới trong che phủ chi tiết | Vào lúc thế giới trong bắt đầu vẽ, nó phải phủ ít nhất diện tích của chi tiết đại diện cho nó trong thế giới ngoài, cùng màu. Trong một lần thử, một mạng tinh thể nguyên tử chỉ vẽ rộng vài nanomet bên trong một transistor vẽ rộng một trăm nanomet hiện ra như một mảng nhỏ trong một ô vuông màu phẳng cho đến khi nó được làm cho lấp đầy cả ô vuông |
| Mức độ chi tiết | Một thế giới chỉ vẽ những gì có trên màn hình và chỉ những gì lớn hơn vài pixel. Một mạng tinh thể nhìn từ xa là màu trung bình của nó; các nguyên tử của nó xuất hiện, fade in, khi mỗi nguyên tử lớn hơn khoảng tám pixel. Nếu không, một thế giới sẽ vẽ hàng trăm nghìn dấu mà không ai thấy |

Đã kiểm tra trong các still của một cảnh thử: bốn thế giới (một chiếc bàn tính theo centimet, một con chip theo phần mười milimet, một lõi theo micromet, một mạng tinh thể theo ångström) đi từ khoảng 2 m tới khoảng 6 Å ngang khung trong mười ba beat. Các kích thước khớp nhau ở mọi lần bàn giao và các frame ở chỗ bàn giao không có đường nối khi giữ đúng quy tắc trên. Chưa được thử trong 3D.

## 4. Bên trong một shot

Một shot hai hoặc ba bar có chỗ cho một chuỗi nhỏ. Các pattern hiệu quả:

| Pattern | Beat | Dùng |
|---|---|---|
| Mở cận, kéo lùi | Cận ở beat 0, cú kéo lùi chạy suốt shot | Shot đầu tiên của một section: khung đầy ngay từ frame đầu |
| Đáp, rồi lắng | Chủ thể đáp xuống lớn, rồi lùi lại để nhường chỗ | Một tên hoặc một vật xuất hiện ở drop rồi phải chia sẻ khung |
| Bám theo, rồi đứng lùi | Ở cùng chủ thể khi nó di chuyển, rồi rộng ra khi nó đến nơi | Nhân và quả |
| Một bước mỗi mục | Tiến gần một bước, hoặc một roll, ở mỗi mục của danh sách | Những thứ chồng chất |
| Hai khung | Một thay đổi khung gắt trên một beat mạnh | Trước và sau, trong một thế giới |
| Đứng yên từ một beat trở đi | Mọi thứ dừng vài beat trước khi kết thúc | Khi transition tiếp theo có phần đầu (lead): phần cuối của shot thuộc về nó |
| Kết thúc ở chỗ shot sau bắt đầu | Pose cuối của shot này là pose đầu của shot sau | Di chuyển giữa hai shot của một thế giới; một cú zoom vào chi tiết |
| Thấp và chậm trong một thế giới lớn | Camera gần mặt đất, đường chân trời thấp, drift chậm sang ngang hoặc về trước trong khi bầu trời đổi màu | Phong cảnh cách điệu, giờ trong ngày thay đổi bên trong một shot (`art-styles.md`, mục 3.8) |
| Nghiêng về chính diện | Một card, một màn hình hoặc một poster xuất hiện xoay theo phối cảnh và lắng lại vuông góc với camera | Các đoạn launch, card của một danh sách. Vẽ card trên một `Layer2D` và hiển thị nó như một mặt phẳng trong một scene three.js với `setThreeCamera`; key góc xoay của nó về không với một ease out mạnh. Transform của canvas không vẽ được phối cảnh thật; một góc xoay nhỏ giả bằng cách bóp và skew chỉ đủ khi dưới khoảng 15 độ |

## 5. Quy tắc

| Quy tắc | Lý do |
|---|---|
| Hai shot liên tiếp không làm cùng một move theo thói quen | Người xem không còn thấy một move lặp lại không có lý do. Storyboard có một cột camera và trình sinh cảnh báo về hai mục giống nhau liên tiếp. Khi sự lặp lại chính là ý tưởng, đánh dấu shot sau `"repeat": true` (`storyboard.md`) |
| Một move có nguyên nhân | Camera đi vì có thứ gì đó để xem. Một move vì chính nó là nhiễu |
| Move bắt đầu trên một beat | Cú cắt và camera đều là nhạc cụ của bản nhạc |
| Rời đi ngay, lắng lại chậm | Ease mặc định đi ra gắt và vào êm. Nó đọc như dứt khoát. Một ease kiểu spring trên camera cảm thấy sai, trừ khi ở một bước (step) |
| Một thay đổi zoom lớn được blend theo scale | Ở giữa move, mức zoom là trung bình nhân, và vị trí đi theo zoom. Một blend thẳng sẽ vội ở một đầu |
| Frame đầu tiên có sức nặng | Một shot mở bằng một khung trống lãng phí cú đánh của cú cắt. Mở bằng chủ thể |
| Khung hình được tận dụng | Trong khung dọc, chủ thể chạy hết chiều cao của vùng an toàn. Một phần ba dưới trống trơn hết shot này đến shot khác là layout làm cho một định dạng khác |
| Camera không đánh bại chữ | Caption do overlay đặt và không di chuyển. Chữ bên trong hình phải giữ cỡ tối thiểu ở mức zoom nhỏ nhất của shot |
| Đứng yên cũng là một move | Sau ba shot bay lượn, một khung khóa cứng là thứ mạnh nhất có được |
| Một màn trình diễn mỗi section | Một dolly zoom, một orbit trọn vòng, một crash zoom: mỗi thứ một lần |

## 6. Lên kế hoạch camera cho một section

Cho mỗi shot một cỡ, một góc và một move, và nhìn cả cột như một tổng thể.

| Shot | Cỡ | Góc | Move |
|---|---|---|---|
| 1, vấn đề bắt đầu | Cận | Ngang tầm | Rơi dọc theo chủ thể |
| 2, nó tệ hơn | Cực cận | Ngang tầm | Trượt sang ngang, sát trên bề mặt |
| 3, nó vượt tầm kiểm soát | Rộng | Cao | Lùi lại, một bước mỗi bar |
| 4, ý tưởng xuất hiện | Trung | Từ trên xuống | Khóa cứng, một jolt mỗi sự kiện |
| 5, ý tưởng hoạt động | Rộng | Từ trên xuống | Bay, đổi hướng với mỗi thay đổi |
| 6, phần đền đáp | Cận, rồi rộng | Ba phần tư, rồi plan | Bám theo, rồi nâng lên |
| 7, nơi bạn gặp nó | Trung | Ngang tầm | Khóa cứng |

Không cỡ, không góc và không move nào đứng hai lần liên tiếp. Các shot khóa cứng là nơi chữ được đọc.

## 7. Hình dạng khung hình

| Khung | Chủ thể phù hợp | Layout | Camera |
|---|---|---|---|
| Dọc 9:16 | Những thứ cao: điện thoại, nhân vật, tòa tháp, danh sách, cuộn giấy, một chiếc cốc, một tờ phiếu | Xếp chồng; chủ thể này trên chủ thể kia; chữ ở dải trên hoặc dải dưới của vùng an toàn | Chuyển động lên xuống là tự nhiên; một cú pan rộng có ít chỗ |
| Ngang 16:9 | Những thứ rộng: phong cảnh, timeline, các hàng, hai thứ đặt cạnh nhau | Cạnh nhau; chữ bên cạnh hình | Pan và truck là tự nhiên |
| Vuông | Một chủ thể ở giữa | Căn giữa | Push và orbit |

Trong phim dọc, các app che phía trên, phía dưới và một bên. Hình có thể chạy ra mọi mép. Bất cứ thứ gì phải đọc được thì nằm trong vùng an toàn: xem `type-and-captions.md`.

Khi một phim ngang cũng sẽ được cắt xuống thành phim dọc bằng crop, hãy giữ những gì quan trọng trong phần 9:16 ở giữa của khung 16:9 (32 phần trăm ở giữa chiều rộng), và di chuyển camera sao cho chủ thể ở lại đó. Khi phim được làm cho cả hai khung, thay vào đó hãy dàn layout riêng cho mỗi khung: xem `short-pieces.md`.

## 8. Trong route HyperFrames

Ở đó camera di chuyển một wrapper bên trong một clip, không bao giờ di chuyển chính clip đã căn thời gian.

| Move | Quy tắc hoặc pattern của nó |
|---|---|
| Punch in, punch out | Keyframe trên scale và vị trí của một wrapper bên trong |
| Push chậm trên một still | Một tween tuyến tính của scale và vị trí trong nhiều giây |
| Zoom tới một mục tiêu lệch tâm | `coordinate-target-zoom` |
| Một camera ảo trên một thế giới | `viewport-change` |
| Các phase có drift | `multi-phase-camera` |
| Bay qua các card theo chiều sâu | `3d-camera-flight`: pose chỉnh bằng mắt |
| Rack focus | `depth-of-field-blur` |
| Whip | Khối `whip-pan`, hoặc `nudge-curve` với `motion-blur-streak` |
| Bám theo một con trỏ đang gõ | `camera-cursor-tracking` |

Luật ease cho camera của nó khớp với quy tắc 4 ở trên: ease out gắt cho các cú lao vào và đáp xuống, ease in và out khi đổi vị trí.

## 9. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Mọi shot trông nhìn thẳng và đứng yên | Storyboard không có cột camera | Thêm một cột; kiểm tra từng cặp liền kề |
| Một chuỗi shot cảm thấy như nhau dù mỗi shot đều di chuyển | Tất cả đều push in | Thay đổi cỡ, góc và move, không chỉ tốc độ |
| Một shot mở ra trên khoảng trống | Chủ thể vào sau cú cắt | Mở bằng chủ thể, lớn |
| Một cú zoom vội ở cuối | Zoom được blend theo đường thẳng | Blend theo scale |
| Một cú zoom sâu rung hoặc rách ở thang đo nhỏ nhất | Một bộ đơn vị cho nhiều bậc thập phân; float hết chữ số | Mỗi thế giới theo đơn vị riêng với gốc tọa độ ở điểm của hành trình (mục 3.7) |
| Một hành trình qua các thang đo lộ đường nối giữa hai thế giới | Chi tiết của thế giới ngoài và thế giới trong không khớp ở chỗ bàn giao | Vẽ chi tiết trong thế giới ngoài đúng như thế giới trong trông ở cỡ đó, hoặc giấu chỗ bàn giao sau kính, ánh sáng hoặc bóng tối |
| Một mảng chi tiết nhỏ nằm trong một ô vuông phẳng ở chỗ bàn giao | Thế giới trong được vẽ nhỏ hơn chi tiết đại diện cho nó | Thế giới trong phủ toàn bộ chi tiết từ frame đầu tiên của nó (mục 3.7) |
| Một ống kính nêu bằng milimét trông sai | Tiêu cự bị dùng như field of view | Quy đổi bằng bảng ở mục 2, theo hướng của khung |
| Chữ nhỏ không đọc được trong một pose rộng | Cỡ tối thiểu được kiểm tra ở pose cận | Kiểm tra ở mức zoom nhỏ nhất của shot |
| Hình bơi bồng bềnh trên mỗi beat | Cú push trên beat quá lớn | Giữ dưới ba phần trăm |
| Một frame bị rung trông nhòe | Shake khác nhau giữa các sample của một frame | Seed nó từ số frame |
| Chủ thể của một cú follow nằm ngay chính giữa | Không có độ trễ | Để camera đi theo sau, để chủ thể dẫn đầu |
| Các vật nhìn xuyên qua nhau trong một hình vẽ nét nhìn trong không gian | Không có đường khuất nào bị loại bỏ | Chấp nhận nó như phong cách của một bản vẽ, hoặc vẽ khối đặc phía sau các nét |
| Vật ở cận và vật ở rộng không phải cùng một hình vẽ | Hai model của một thứ | Một model, hoặc một lần bàn giao được che bởi một cú cắt hay một tia lóe |
| Một shot ba chiều có cạnh răng cưa | Target mà nó vẽ vào không có anti-aliasing | Vẽ vào một target có nhiều sample và đặt nó lên khung |
