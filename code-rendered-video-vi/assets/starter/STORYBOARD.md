# Storyboard: Starter Film

Được sinh ra từ `shots.json` và `copy.json` bởi `scripts/build-shot-files.py`. Đừng chỉnh sửa file này: hãy thay đổi dữ liệu và chạy lại script.

## 1. Tổng quan

| Phần | Bar | Độ dài tính theo bar | Bắt đầu | Số shot | Cách kể |
|---|---|---|---|---|---|
| Tiêu đề | 0 đến 1 | 2 | 0:00.0 | 1 | Hai bar của đoạn intro: tên phim rơi vào downbeat của bar thứ hai. |
| 01 Nước | 2 đến 8 | 7 | 0:04.0 | 3 | Vấn đề trước, trong những bar trước khi trống vào. Cái tên xuất hiện cùng câu trả lời, sau một bar. |
| 02 Ngâm | 9 đến 17 | 9 | 0:18.0 | 3 | Câu trả lời trước: cái tên rơi vào drop, và các shot sau đó giải thích vì sao. |
| Recap | 18 đến 19 | 2 | 0:36.0 | 1 | Cả hai cái tên thêm một lần nữa, mỗi cái một beat, rồi đến tách trà. |
| End card | 20 đến 23 | 4 | 0:40.0 | 1 | Một câu duy nhất để mang về, giữ đến hết bản nhạc. |

9 shot, bar 0 đến 24, 48.0 giây.

## 2. Transition

Một transition thuộc về shot mà nó dẫn vào. Phần dẫn (lead) của nó phát đè lên phần cuối của shot trước, phần đuôi (tail) của nó phát đè lên phần đầu của shot mà nó dẫn vào.

| Loại | Số lần dùng | Nó làm gì |
|---|---|---|
| Cắt thẳng (`cut`) | 0 | Không thêm gì cả. |
| Cắt kèm punch-in (`punch`) | 1 | Shot mới nhảy lại gần thêm một bước rồi lùi về ổn định. |
| Cắt kèm hai frame đảo màu (`invert`) | 1 | Hai frame đầu tiên của shot mới bị đảo màu, kèm một cú giật. |
| Cắt kèm chớp sáng (`flash`) | 0 | Một tia chớp tắt dần trong chưa tới nửa beat. |
| Whip (`whip`) | 1 | Shot cũ nhoè về một hướng và shot mới hiện ra từ vệt nhoè đó, trong vòng nửa beat. |
| Push (`push`) | 1 | Shot mới đẩy shot cũ ra khỏi khung hình, với một đường nối tối giữa chúng. |
| Caret wipe (`caret`) | 0 | Dấu caret của phim quét ngang khung hình; phía sau nó là shot mới. |
| Tiles (`tiles`) | 0 | Khung hình là một bức tường ô vuông lật lần lượt từ một góc. |
| Tắt tivi (`crt`) | 1 | Hình co lại thành một đường kẻ và một chấm; shot mới bật lên từ đường kẻ đó. |
| Tua băng (`rewind`) | 0 | Hình bị xé thành các dải, màu tách ra và khung hình cuộn đi. |
| Implode (`implode`) | 1 | VÀO MỘT DROP. Hình xoáy vào một điểm. Nhịp thở (breath): một chấm màu signal. Va chạm (impact): một sóng xung kích từ chấm đó. |
| Giật vào một khe (`stutter`) | 0 | VÀO MỘT DROP. Shot lặp lại chính nó theo các lát cắt giảm một nửa sau mỗi beat trong khi khung hình khép lại thành một khe hẹp. Nhịp thở: một đường ánh sáng. Va chạm: khe hẹp bung mở. |
| Đường hầm (`tunnel`) | 0 | VÀO MỘT DROP. Khung hình chứa một bản sao nhỏ hơn của chính nó, và bản đó lại chứa một bản khác; camera lao vào trong. Nhịp thở: trắng. Va chạm: một sóng xung kích. |
| Nín thở (`breath`) | 0 | VÀO MỘT DROP SAU MỘT KHOẢNG LẶNG. Hình mất màu, tối dần và khép lại quanh một điểm. Va chạm: ba sóng xung kích. |
| Kéo giãn (`stretch`) | 0 | VÀO MỘT DROP. Các cột pixel kéo giãn thành vệt và khung hình đảo màu theo hồi trống dồn (drum roll). Va chạm: các vệt rơi xuống, hai sóng xung kích. |
| Lát cắt (`slices`) | 1 | Khung hình bị cắt thành các dải trượt ra hai bên, so le nhau. |
| Xoay (`spin`) | 0 | Khung hình xoay quanh một điểm; shot mới đến khi nó vẫn đang xoay. |
| Zoom ba bước (`stepzoom`) | 0 | Ba cú punch-in mạnh trên các nốt móc kép, mỗi cú kèm tách màu và nghiêng; shot mới lùi ra hai lần. |
| Xuyên qua một chữ cái (`through`) | 0 | TRONG THẾ GIỚI PHIM (IN-WORLD). Một chữ cái lớn đứng trước camera, camera đi xuyên qua lỗ của nó; phía bên kia là shot mới. |
| Vỡ vụn (`shatter`) | 0 | TRONG THẾ GIỚI PHIM. Một vật của shot cũ bay vào ống kính; nơi nó chạm vào, khung hình vỡ ra và rơi xuống để lộ shot mới. |
| Đi vào một chi tiết (`zoom-in`) | 1 | TRONG THẾ GIỚI PHIM. Shot mới đã nằm sẵn trong một chi tiết của shot cũ; camera đi vào đó cho đến khi nó lấp đầy khung hình. |
| Đi ra khỏi một chi tiết (`pull-out`) | 0 | TRONG THẾ GIỚI PHIM. Shot cũ hoá ra là một chi tiết của shot mới; camera lùi lại và cho thấy thế giới lớn hơn. |
| Hành trình camera (`travel`) | 0 | TRONG THẾ GIỚI PHIM. Hai shot là hai nơi trong cùng một thế giới; camera di chuyển từ nơi này sang nơi kia. |
| Match cut (`match`) | 0 | TRONG THẾ GIỚI PHIM. Hình cuối của một shot và hình đầu của shot kế tiếp có chung một hình dạng. |

Các transition mà các shot tham gia vào, và những gì chúng yêu cầu ở builder:

| Bar | Thời điểm | Vào shot | Transition | Cần làm gì |
|---|---|---|---|---|
| 12 | 0:24.0 | Màu loang ra | Đi vào một chi tiết | Camera đi vào lớp kính của đồng hồ cát; shot kế tiếp là tách trà nhìn qua lớp kính đó. |

Các cú cắt vào một drop. Những beat cuối của shot trước thuộc về transition: những gì quan trọng trong shot đó phải xong trước khi phần dẫn của nó bắt đầu.

| Bar | Thời điểm | Vào shot | Transition | Dẫn, đuôi (beat) |
|---|---|---|---|---|
| 9 | 0:18.0 | Ba phút | Implode | 2, 1.5 |

## 3. Chữ trên màn hình

| Cách | Ai đặt chữ | Số caption |
|---|---|---|
| Plate | Overlay, trên một plate ở trên cùng, giữa hoặc dưới cùng | 4 |
| Shot tự đặt chữ | Builder, như một vật trong hình | 1 |
| Không chữ | Không ai cả: hình ảnh tự nói lên | 1 |

Khi một shot vẫn còn là storyboard card, studio hiển thị mọi caption của nó dưới dạng plate, để mọi câu chữ đều đọc được trong animatic. Một plate có viền đứt nét sẽ biến mất khi shot của nó được dựng.

| # | Section | `hook` | `idea` | `use` |
|---|---|---|---|---|
| 1 | Nước | Nước sôi rót lên lá trà xanh / làm tách trà bị đắng. | Để ấm nước nghỉ / một phút sau khi sôi. | Trà xanh và trà trắng, / lần nào cũng vậy. |
| 2 | Ngâm | Để lá ngâm quá lâu / tách trà sẽ nhạt nhẽo. | Ba phút, / rồi nhấc lá ra. | Đặt hẹn giờ / khi bạn rót. |

Title card: `name` A Better / Cup (Một tách trà ngon hơn); `line` hai bước / để có một tách trà ngon

End card: `line` Để ý nước, / để ý thời gian.

## 4. Từng shot một

### Tiêu đề

Hai bar của đoạn intro: tên phim rơi vào downbeat của bar thứ hai.

| Bar | Thời điểm | Nền | Vào bằng | Shot | Trên màn hình | Theo nhạc | Camera | Look |
|---|---|---|---|---|---|---|---|---|
| 0 đến 1 | 0:00.0 | tối |  | Tên phim (`open-title-card`) | Một mặt bàn tối nhìn từ trên xuống, một tách trà rỗng ở giữa. Tên phim, A BETTER CUP, đứng sau tách trà bằng chữ cao bằng cả khung hình. | Bar đầu: chỉ có tách trà, hơi nước bốc lên theo mỗi beat. Bar thứ hai: mỗi từ của cái tên xuất hiện trên một trong ba beat đầu của nó. | Cố định (locked off), khung hình nhún nhẹ theo mỗi từ | Chữ toàn khung hình phía sau một vật được vẽ |

### 01 Nước

Vấn đề trước, trong những bar trước khi trống vào. Cái tên xuất hiện cùng câu trả lời, sau một bar.

Cái tên được hiển thị từ bar 3 (0:06.0). Trước đó bộ đếm hiện `???`.

| Bar | Thời điểm | Nền | Vào bằng | Shot | Trên màn hình | Theo nhạc | Camera | Look |
|---|---|---|---|---|---|---|---|---|
| 2 đến 3 | 0:04.0 | sáng | Whip | Quá nóng (`water-cold-kettle`) | Một ấm nước đang sôi sùng sục rót thẳng lên lá trà xanh trong một tách thuỷ tinh. Lá cuộn lại và chuyển nâu từ mép. | Việc rót bắt đầu ở beat một. Lá sẫm đi một bậc sau mỗi beat của bar thứ hai. | Đẩy chậm vào phía tách trà | Cắt dán màu phẳng, nhìn ngang |
| 4 đến 6 | 0:08.0 | tối | Cắt kèm punch-in | Để nó nghỉ (`water-rolling-boil`) | Ấm nước được nhấc khỏi bếp và đặt xuống. Một nhiệt kế bên cạnh tụt từ 100 xuống 80 khi bọt trong ấm ngừng sủi từng cái một. | Một bọt khí ngừng ở mỗi beat. Nhiệt kế giảm năm độ ở mỗi downbeat. | Quay vòng quanh ấm một lần | Nét vẽ đường với một màu signal |
| 7 đến 8 | 0:14.0 | sáng | Push | Cách rót đúng (`water-pour-off-boil`) | Nước đã nghỉ được rót lên lá mới. Lá nở ra chậm rãi và vẫn giữ màu xanh. | Việc rót ở beat một. Một chiếc lá nở ra ở mỗi beat sau đó. | Cố định, cận vào tách trà | Cắt dán màu phẳng, nhìn ngang |

| Caption | Bar | Câu chữ | Cách | Lý do |
|---|---|---|---|---|
| `hook` | 2.25 đến 3 | Nước sôi rót lên lá trà xanh / làm tách trà bị đắng. | Plate, trên cùng | Tách trà và lá chiếm nửa dưới. Nó bắt đầu sau một beat, khi cú whip đã ổn định. |
| `idea` | 4.5 đến 6 | Để ấm nước nghỉ / một phút sau khi sôi. | Plate, dưới cùng | Ấm nước và nhiệt kế đứng ở hai phần ba phía trên. |
| `use` | 7.25 đến 8 | Trà xanh và trà trắng, / lần nào cũng vậy. | Không chữ | Lá vẫn xanh: hình ảnh tự nói lên. |

### 02 Ngâm

Câu trả lời trước: cái tên rơi vào drop, và các shot sau đó giải thích vì sao.

Cái tên được hiển thị từ bar 9 (0:18.0). Trước đó bộ đếm hiện `???`.

| Bar | Thời điểm | Nền | Vào bằng | Shot | Trên màn hình | Theo nhạc | Camera | Look |
|---|---|---|---|---|---|---|---|---|
| 9 đến 11 | 0:18.0 | tối | Implode | Ba phút (`steep-leaves-drop`) | Một đồng hồ cát lật ngược đúng vào drop. Chữ STEEP (ngâm) lấp đầy khung hình phía sau nó. | Đồng hồ lật ở beat đầu tiên của drop. Cát rơi theo nhịp tiếng kick. | Punch-in vào drop, rồi trôi lùi lại | Chữ đậm và một vật được vẽ, tương phản cao |
| 12 đến 13 | 0:24.0 | sáng | Đi vào một chi tiết | Màu loang ra (`steep-colour-spreads`) | Nhìn từ trên xuống, màu loang từ lá trà qua nước thành từng vòng, từ nhạt đến hổ phách đậm. Một nhãn nhỏ trên tách ghi câu chữ. | Một vòng ở mỗi beat. | Hạ chậm từ trên xuống phía mặt nước | Gradient mềm, nhìn từ trên xuống |
| 14 đến 17 | 0:28.0 | tối | Cắt kèm hai frame đảo màu | Nhấc ra đúng giờ (`steep-timer-rings`) | Đồng hồ hết giờ và reo. Lá trà được nhấc ra khỏi tách trong một động tác. | Tiếng reo ở beat đầu tiên của bar thứ ba. Động tác nhấc ở downbeat sau đó. | Tilt lên theo lá trà được nhấc | Nét vẽ đường với một màu signal |

| Caption | Bar | Câu chữ | Cách | Lý do |
|---|---|---|---|---|
| `hook` | 9.5 đến 11 | Để lá ngâm quá lâu / tách trà sẽ nhạt nhẽo. | Plate, dưới cùng | Bắt đầu sau cú va chạm của drop, để có thể đọc được. |
| `idea` | 12 đến 13 | Ba phút, / rồi nhấc lá ra. | Shot tự đặt chữ | Nhãn trên tách trà mang câu chữ. |
| `use` | 14.5 đến 17 | Đặt hẹn giờ / khi bạn rót. | Plate, giữa | Lá trà được nhấc lên để trống phần giữa khung hình. |

### Recap

Cả hai cái tên thêm một lần nữa, mỗi cái một beat, rồi đến tách trà.

| Bar | Thời điểm | Nền | Vào bằng | Shot | Trên màn hình | Theo nhạc | Camera | Look |
|---|---|---|---|---|---|---|---|---|
| 18 đến 19 | 0:36.0 | tối | Lát cắt | Nước, ngâm (`recap-both-names`) | Hai cái tên, WATER (nước) và STEEP (ngâm), mỗi cái trên một beat của bar đầu, rồi đến tách trà hoàn chỉnh. | Mỗi beat một cái tên, tách trà ở downbeat của bar thứ hai. | Bước ngang một lần cho mỗi cái tên | Chữ toàn khung hình |

### End card

Một câu duy nhất để mang về, giữ đến hết bản nhạc.

| Bar | Thời điểm | Nền | Vào bằng | Shot | Trên màn hình | Theo nhạc | Camera | Look |
|---|---|---|---|---|---|---|---|---|
| 20 đến 23 | 0:40.0 | sáng | Tắt tivi | Mang về (`end-card`) | Câu kết, dàn chữ lớn, và tách trà bên cạnh. | Mỗi dòng của câu trên một downbeat. | Cố định | Chữ trên giấy |
