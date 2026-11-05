# Transition (chuyển cảnh)

Một danh mục các cách một shot có thể dẫn sang shot kế tiếp, kèm cảm giác mỗi cách mang lại, khoảnh khắc phù hợp và chi phí để dựng. Chương cũng đưa ra các quy tắc phân bổ transition trong một bộ phim, để vài transition mạnh rơi đúng nơi nhạc mạnh nhất.

Nạp chương này khi: viết trường `in` của các shot trong storyboard, lên kế hoạch cú cắt vào một drop, viết brief cho một builder có shot tham gia một transition, hoặc thêm một loại mới vào engine.

## 1. Mô hình

| Quy tắc | Ý nghĩa |
|---|---|
| Một transition thuộc về shot mà nó dẫn VÀO | Shot list ghi nó trên shot đến. Shot đầu tiên của phim không có |
| Nó có lead (phần dẫn) và tail (phần đuôi), đo bằng beat | Lead lấy từ cuối shot đi, tail lấy từ đầu shot đến. Một cú cắt thường không có cả hai |
| Bản thân cú cắt vẫn nằm trên beat | Lead và tail mọc ra hai phía từ cú cắt. Chúng không bao giờ dịch chuyển nó |
| Hai họ | **Screen-space** (không gian màn hình): engine làm việc trên hai hình đã hoàn chỉnh và các shot không biết gì về nó. **In-world** (trong thế giới): sự thay đổi xảy ra bên trong thế giới của các shot, và builder của chúng tham gia |
| Thời gian có thể bẻ cong | Vì mỗi shot là một hàm thuần theo thời gian, engine có thể hỏi một shot ở bất kỳ thời điểm nào nó muốn: giữ một frame, phát lại một lát, chạy ngược |
| Phần lớn cú cắt là cắt thường | Cắt nhanh đã là nhịp điệu của phim. Một transition là một điểm nhấn, và nhấn ở mọi cú cắt thì chẳng còn là nhấn |

Những gì builder của một shot phải biết về các shot láng giềng:

| Nếu | Thì |
|---|---|
| Shot kế tiếp có một transition có lead | `lead` beat cuối của shot này được phát dưới transition và có thể bị biến dạng. Những gì quan trọng phải xong trước đó |
| Shot này có một transition có tail | `tail` beat đầu của nó đến dưới một chớp sáng, một làn sóng hoặc một wipe. Frame đầu vẫn cần có sức nặng, và không chữ nào cần đọc được đặt ở đó |
| Transition bẻ cong thời gian | Các beat cuối của shot đi không được hiển thị như khi chúng được làm |

## 2. Một cú cắt vào drop có ba phần

Drop là nơi nhạc đánh mạnh nhất sau một đoạn build (dồn nén). Một cú cắt thường ở đó là phí phạm: nhạc đổ xuống còn hình ảnh không làm gì.

| Phần | Khi nào | Điều gì xảy ra |
|---|---|---|
| Build | 2 beat cuối trước drop | Căng thẳng tăng theo một đường cong tăng tốc. Khung hình bị đẩy vào ở mỗi nửa beat |
| Breath (hơi thở) | Một phần tư beat cuối | Gần như mọi thứ bị lấy đi: một chấm, một đường, hoặc màu trắng. Thời gian của shot đi bị giữ lại |
| Impact (va chạm) | 1.5 beat đầu của drop | Hai frame âm bản, rồi một chớp sáng, một sóng xung kích và một cú giật mạnh tắt dần |

Breath là thứ tạo nên impact. Im lặng trước cú đánh vang hơn chính cú đánh.

## 3. Lựa chọn

Đi qua các bước sau theo thứ tự.

1. **Cú cắt này có nằm trên một khoảnh khắc mạnh của nhạc không?** Một drop, cú bùng nổ sau im lặng, bar đầu của một phrase mới, đoạn kết của phim. Nếu không, dùng cắt thường hoặc cắt có nhấn.
2. **Hai hình có liên quan về không gian không?** Một hình chứa hình kia (một màn hình, một tấm thẻ, một cửa sổ), hoặc chúng là hai nơi của cùng một thế giới, hoặc chúng chung một hình dạng. Nếu có, một transition in-world là khả thi. Chỉ dùng nó nếu khoảnh khắc xứng đáng.
3. **Cú cắt mang ý nghĩa gì?** Mục kế tiếp của một danh sách, quay ngược thời gian, đi sâu hơn, lùi lại để thấy toàn cảnh, thất bại, thức dậy. Chọn loại có hình ảnh nói lên điều đó.
4. **Cú cắt trước đã làm gì?** Không bao giờ cùng một loại hai lần liên tiếp, trừ cắt thường. Không bao giờ cùng một loại ở hai ranh giới section liên tiếp.
5. **Chữ có sống sót qua nó không?** Nếu có caption trên màn hình trong lúc lead hoặc tail, chọn loại giữ khung hình đọc được, hoặc dời caption đi.

### Theo khoảnh khắc

| Khoảnh khắc | Lựa chọn đầu tiên | Cũng tốt | Tránh |
|---|---|---|---|
| Bên trong một section, trên một phrase drop | Hard cut, punch, flash, invert, whip | Slices, spin | Wipe và dissolve dài |
| Bên trong một section, đoạn êm | Hard cut, push, match | Crossfade | Glitch, shake |
| Ranh giới giữa hai section | Motif wipe riêng của phim, tiles, push, screen off and on | Iris, cover | Loại đã dùng ở ranh giới trước |
| Vào một drop | Một trong các loại drop (mục 5.7) | Shatter trên drop | Cắt thường |
| Cú bùng nổ sau im lặng | Breath | Blackout rồi bật đèn | Bất cứ thứ gì có build dài: không có nhạc để chở nó |
| Vào một break, nơi trống dừng | Flash, push, cắt thường | Dip về một màu | Biến dạng: break là nơi chữ được đọc |
| Title vào shot đầu tiên | Through, zoom vào một chi tiết, match | Iris | Cắt thường: title xứng đáng một cú trao tay |
| Vào phần recap (tóm tắt) | Step zoom, một chuỗi punch cut | Tiles | Blend chậm |
| Vào end card | Cắt thường, flash, dip về đen | | Bất cứ thứ gì bẻ cong những chữ cuối |
| Kể lại mà không có ý tưởng | Rewind, reverse | Invert | |
| Từ ẩn dụ sang ứng dụng thật | Match, zoom vào một chi tiết | Push | |
| Một thất bại, một lỗi | Glitch, shake cut, gravity drop | Invert | Blend thanh lịch |

### Theo năng lượng và tâm trạng

| Năng lượng của nhạc | Độ dài transition | Các loại |
|---|---|---|
| Êm (pad, không trống) | 1 đến 2 beat, hoặc 1 đến 2 giây | Crossfade, blur dissolve, dip, slow push, iris |
| Trung bình (groove đều) | Nửa beat đến 1 beat | Push, tiles, slices, wipe, whip |
| Cao (drop, cắt nhanh) | Một phần tư đến ba phần tư beat | Hard cut, punch, flash, invert, whip, spin, step zoom |

| Tâm trạng mong muốn | Các loại |
|---|---|
| Vui tươi | Spin, squeeze, gravity drop, tiles, object wipe |
| Kỹ thuật, chính xác | Slices, push, linear wipe, match, zoom vào một chi tiết |
| Hoài niệm, analog | Film burn, screen off and on, rewind, iris, page turn |
| Căng thẳng | Strobe cut, stutter, glitch, freeze cut |
| Cao cấp, lặng lẽ | Blur dissolve, dip, match, slow pull back |
| Thủ công | Ink bleed, fold, page turn, cover bằng giấy cắt |

### Khi không có grid nhạc

Một phim dẫn dắt bằng giọng nói không có beat. Cho độ dài bằng giây, đặt cú cắt ở cuối câu hoặc trên từ được nhấn, và ưu tiên những cú cắt không bị để ý (match, cut on action, push). Các loại drop không có chỗ ở đó.

## 4. Phân bổ

| Quy tắc | Lý do |
|---|---|
| Cắt thường và cắt có nhấn chiếm đa số | Chúng giữ nhịp và không tốn gì |
| Mỗi drop một loại drop, và mỗi lần một loại khác | Drop là sự kiện hiếm; lặp lại hình ảnh của nó làm nó trở nên tầm thường |
| Transition in-world: vài cái mỗi phim, ở những khoảnh khắc quan trọng | Chúng là những hình ảnh mạnh nhất và đắt nhất. Đặt ở mọi cú cắt, chúng sẽ bóp nghẹt sức sống của các shot |
| Không loại nào hai lần liên tiếp, trừ cắt thường | Người xem không được học ra khuôn mẫu |
| Lead của một transition không được chạy vào tail của transition trước | Một shot cần vài beat là của riêng nó |
| Tail phải ngắn hơn shot | Nếu không shot không bao giờ xuất hiện mà không bị xáo trộn |

Từ thực tế: một phim 172 giây với 53 cú cắt đã dùng 22 loại. Số lượng: whip 7, push 7, punch 6, invert 4, cắt thường 4, motif wipe 3, flash 3, zoom vào một chi tiết 2, pull ra khỏi một chi tiết 2, tiles 2, slices 2, và mỗi loại một lần cho through, shatter, spin, screen off, rewind, step zoom và năm loại drop. Sáu cú cắt là in-world. Phản ứng đầu tiên của chủ sở hữu với một bản nháp đầu nhẹ nhàng hơn là các cú cắt "quá nhẹ nhàng và không chặt"; phản ứng thứ hai, sau khi mọi cú cắt đã được biến thành màn trình diễn trên giấy, là transition in-world nên là "một sự bổ sung, vài cái ở những khoảnh khắc quan trọng, không phải mọi cú cắt".

## 5. Danh mục

Các cột: **Beat** là lead cộng tail. **Engine** ghi tên loại trong starter (`src/engine/transition.ts`, danh sách `TRANSITION_KINDS`) hoặc ghi "chưa dựng". **HyperFrames** ghi mục gần nhất của framework đó, từ animation skill và registry của nó.

### 5.1 Cắt thường và cắt có nhấn

Những loại này không cần gì từ các shot. Điểm nhấn là một khoảnh khắc hiệu ứng post trên shot đến.

| Loại | Người xem thấy | Cảm giác và cách dùng | Beat | Engine | HyperFrames |
|---|---|---|---|---|---|
| Hard cut | Một hình bị thay bằng hình kế tiếp, trên beat | Trung tính và nhanh. Mặc định bên trong một section | 0 | `cut` | mặc định |
| Punch cut | Shot mới đến gần hơn một bậc rồi lắng lại | Một cái gật đầu trên tiếng kick. Bên trong một phrase drop | 0 + 0.75 | `punch` | không có |
| Flash cut | Một chớp sáng tắt trong chưa đầy nửa beat | Đèn flash máy ảnh, một sự lộ diện. Trên tiếng snare, khi một cái tên xuất hiện | 0 + 0.75 | `flash` | `flash-through-white`, Color Dip |
| Invert cut | Hai frame đầu âm bản, kèm một cú giật | Một cú sốc, một tấm X-quang. Từ nền tối sang nền sáng; cùng một thứ ở trạng thái mới | 0 + 0.75 | `invert` | không có |
| Shake cut | Khung hình giật rồi dừng lại | Một cú đánh. Khi có thứ gì trong shot va vào thứ gì | 0 + 0.5 | một phần của các loại khác | không có |
| Smash cut | Từ ồn ào và chật chội sang im lặng và tĩnh, hoặc ngược lại | Tương phản, một câu đùa. Vào một break | 0 | một cú cắt thường đặt trên nhạc | không có |
| Jump cut | Cùng khuôn hình, thời gian đã nhảy cóc | Sốt ruột, lặp lại, hài hước. Chờ đợi, thử lại | 0 | bên trong một shot | không có |
| Match cut | Hình cuối và hình đầu chung một hình dạng ở cùng vị trí | Sự dí dỏm: hai thứ là một ý tưởng. Ẩn dụ sang ứng dụng thật | 0 | `match` | có tên, "no automatic matching-frame discovery" |
| Cut on action | Một chuyển động bắt đầu ở shot này kết thúc ở shot sau | Sự trôi chảy. Ném và bắt, nhấn và kết quả | 0 | bên trong các shot | không có |
| Strobe cut | Hai hình luân phiên trong một hai beat trước khi hình mới giữ lại | Căng thẳng, một hộp đêm. Những beat cuối của một build | 1 đến 2 + 0 | chưa dựng | không có |
| Freeze cut | Shot đi dừng lại ở frame cuối trong một khoảnh khắc, rồi cắt | Một hơi nín thở trước câu chốt | 0.25 đến 0.5 + 0 | breath của các loại drop | không hỗ trợ giữa nguồn |

### 5.2 Wipe, mask và cover

Screen-space. Engine cần cả hai hình cùng lúc.

| Loại | Người xem thấy | Cảm giác và cách dùng | Beat | Engine | HyperFrames |
|---|---|---|---|---|---|
| Push | Shot mới đẩy shot cũ ra ngoài, một đường nối tối giữa chúng | Một trang được lật, mục kế tiếp. Giữa các mục ngang hàng của một danh sách | 0.25 + 0.25 | `push`, kèm một hướng | Push Slide, Vertical Push |
| Linear wipe | Một cạnh thẳng quét ngang theo hướng di chuyển, shot mới phía sau nó, một đường mảnh trên cạnh | Gọn gàng, kiểu biên tập. Một kết quả được lộ ra | 0.5 | `wipe`, kèm một hướng | clip-path reveal |
| Motif wipe | Một hình dạng thuộc về phim (con trỏ của nó, dấu hiệu của nó) quét ngang với shot mới phía sau | Chữ ký của phim. Ranh giới section | 0.5 đến 1 | `caret` | không có |
| Iris | Một vòng tròn mở ra từ một điểm cho đến khi phủ hết khung hình, shot mới bên trong | Một ánh đèn sân khấu, một vòng tròn từ một nút bấm sang cảnh kế tiếp. Mở đầu hoặc kết thúc, một sự lộ diện từ một điểm | 0.5 đến 1 | `iris`, tại focus | Circle Iris, Diamond Iris, `sdf-iris` |
| Aperture | Sáu lá kim loại xoay vào và khép lại trên shot thành một điểm; chúng mở lại trên shot mới | Một máy ảnh, một màn trập, một cú dừng và khởi động gắt. Một tiếng tách đổi cảnh | 0.5 + 0.5 | `aperture`, tại focus | không có |
| Clock wipe | Một kim quét quanh khung hình | Thời gian trôi | 1 | chưa dựng | Clock Wipe |
| Slices | Khung hình bị cắt thành các dải trượt ra xa nhau, luân phiên | Cơ khí, một màn trập. Năng lượng trong một section kỹ thuật | 0.25 + 0.25 | `slices`, bảy dải | Horizontal Blinds, Vertical Blinds, Shutter |
| Tiles | Khung hình là một bức tường các ô lật, bắt đầu từ một góc | Một bảng, một bức khảm. Ranh giới section, dữ liệu | 0.25 + 0.5 | `tiles` | Grid Dissolve |
| Split | Khung hình tách làm hai nửa | Một sự mở ra, một phép so sánh | 0.5 | chưa dựng | Diagonal Split |
| Shape mask | Shot mới được thấy qua một hình đang lớn dần: một chữ cái, một logo | Branding | 1 | `through` làm việc này với chữ cái | Morph Circle |
| Cover | Ba tấm màu phẳng quét vào nối đuôi nhau và phủ khung hình tại cú cắt, rồi quét tiếp ra ngoài, tấm cuối vào thì ra đầu, để lại shot mới | Táo bạo, đồ họa. Look kiểu poster, tiêu đề section, số liệu lớn | 0.5 + 0.5 đến 1 + 1 | `cover`, kèm một hướng và một màu | Staggered Color Blocks |
| Ink bleed | Shot mới loang ra như mực thấm qua giấy | Hữu cơ, thủ công. Look giấy và sơn | 1 đến 2 | chưa dựng | `domain-warp-dissolve`, `ridged-burn`, Page Burn |
| Mosaic | Hình vỡ thành các pixel lớn và hiện ra thành shot mới | Kỹ thuật số, một game retro | 0.5 đến 1 | chưa dựng thành một loại; các shot ở hai bên có thể tăng `mosaic` của chuỗi post đến cú cắt và giảm sau đó | `grid-pixelate-wipe` |
| Fold | Khung hình là một tấm bản đồ giấy gồm 3 x 3 ô: các góc gập lên các cạnh, các cạnh gập lên phần giữa, gói giấy lật lại tại cú cắt, và shot mới mở ra, phần giữa trước, rồi các cạnh, rồi các góc | Giấy, bản đồ, bản vẽ, một bố cục tự sắp xếp lại | 1.5 + 1.5 | `fold` | không có |
| Page turn | Shot cũ gập đi như một tờ giấy | Ấn phẩm, một cuốn sách | 1 | chưa dựng | 3D Card Flip |

Một wipe quá gọn gàng bị đọc như một hàng phím đàn piano hoặc một bài trình chiếu. Từ thực tế: tiles cần khoảng hở giữa các ô và trục xoay luân phiên thì mới được đọc như một bức tường.

### 5.3 Blend và ánh sáng

| Loại | Người xem thấy | Cảm giác và cách dùng | Độ dài | Engine | HyperFrames |
|---|---|---|---|---|---|
| Crossfade | Một hình mờ dần sang hình kia | Êm, thời gian trôi. Phim chậm, phim dẫn bằng giọng nói | 1 đến 2 beat | mặc định của engine ở chỗ hai mục timeline chồng nhau | Crossfade |
| Dip | Mờ về đen, trắng hoặc một màu, rồi hiện lên lại; trộn theo cách màn hình hiển thị, để cú mờ không treo lơ lửng rồi tụt xuống | Một quãng nghỉ, một chương mới, đoạn kết | 0.5 + 0.5 | `dip`, kèm một màu (mặc định là ink); flash là một dip rất nhanh về trắng | Color Dip |
| Blur dissolve | Shot cũ mất nét, shot mới hiện vào | Mềm mại, cao cấp | 1 | chưa dựng | Blur Crossfade, Focus Pull, Blur Through |
| Film burn | Ánh sáng ấm tràn ngập khung hình | Hoài niệm, chất liệu phim nhựa | 1 | chưa dựng | Light Leak, Film Burn, Overexposure Burn |
| White-out | Hình sáng dần cho đến khi không còn gì | Sự đến nơi, lần lộ diện cuối cùng | 1 | breath của `tunnel` | không có |
| Double exposure | Cả hai hình nằm chồng lên nhau một lúc | Ký ức, hai trạng thái được so sánh | 2 trở lên | chưa dựng | không có |

### 5.4 Chuyển động

Khung hình hành xử như thể một camera đã di chuyển. Screen-space, nhưng được đọc như camera work.

| Loại | Người xem thấy | Cảm giác và cách dùng | Beat | Engine | HyperFrames |
|---|---|---|---|---|---|
| Whip pan | Shot cũ nhòe về một hướng và shot mới hình thành từ vệt nhòe | Tốc độ, "trong khi đó". Bên trong một phrase drop | 0.25 + 0.25 | `whip`, kèm một hướng | `whip-pan`, Directional Blur |
| Spin | Khung hình xoay quanh một điểm; shot mới đến khi vẫn đang xoay | Chóng mặt, vui tươi. Đổi điểm nhìn | 0.5 | `spin`, kèm một focus | `swirl-vortex` |
| Crash zoom | Một radial blur vào một điểm; shot mới bung ra từ đó | Khẩn cấp. Lao vào một chi tiết | 0.5 | một phần trong `stepzoom` và `tunnel` | `cinematic-zoom`, Zoom Through |
| Step zoom | Ba bước gắt tiến vào, theo nốt móc kép, mỗi bước tách màu và nghiêng; shot mới lùi ra hai bước | Ngông nghênh, hip-hop. Vào một recap hoặc một danh sách | 0.75 + 0.5 | `stepzoom` | không có |
| Zoom through | Shot cũ lớn dần cho đến khi shot mới hiện ra | Trực tiếp | 0.5 | thế chỗ cho zoom vào một chi tiết | Zoom Through |
| Pull back | Shot cũ thu nhỏ vào trong shot mới | Bối cảnh, toàn thể | 0.5 đến 1 | thế chỗ cho pull out | Zoom Out |
| Gravity drop | Shot cũ rơi ra khỏi khung hình | Sức nặng, thất bại, hài hước | 0.5 | chưa dựng | Gravity Drop |
| Squeeze | Shot mới ép shot cũ dẹt lại | Hoạt hình | 0.5 | chưa dựng | Squeeze, Elastic Push |

### 5.5 Biến dạng và lỗi tín hiệu

| Loại | Người xem thấy | Cảm giác và cách dùng | Beat | Engine | HyperFrames |
|---|---|---|---|---|---|
| Screen off and on | Hình sụp thành một đường, rồi thành một chấm; shot mới bật lên từ đường đó | Một chiếc TV, kết thúc một ý nghĩ. Cuối một section, look màn hình | 0.5 + 0.5 | `crt` | không có |
| Tape rewind | Hình bị xé thành các dải, màu tách ra, khung hình cuộn | Quay ngược. Kể lại mà không có ý tưởng | 1 + 0.5 | `rewind` | VHS Tape |
| Glitch | Các dải xé ngang và tách màu, các khối nhảy, vài dải mất hình thành màu signal; ngày càng nhiều dải hiện shot mới, đổi mỗi hai frame | Một lỗi, áp lực | 0.25 + 0.25 đến 0.5 + 0.5 | `glitch`; bên trong một shot, `glitch` của chuỗi post xé một hình | Glitch, `glitch`, Chromatic Aberration |
| Colour split hit | Ba màu bay tách ra rồi bật về | Một cú đánh trên tiếng kick | 0.25 | trong các điểm nhấn post của nhiều loại | `chromatic-radial-split` |
| Ripple | Các vòng lan ra từ một điểm và bẻ cong hình | Nước, một cú sốc | 0.5 đến 1 | sóng xung kích của các loại drop | Ripple, `ripple-waves` |
| Column stretch | Các cột pixel bị kéo thành vệt | Dữ liệu tan rã | 1 đến 2 | `stretch` | Pixel Sort |
| Heat, lens | Hình gợn sóng hoặc cong quanh một điểm | Một giấc mơ, lực hấp dẫn | 1 | chưa dựng thành một loại; một shot có thể tăng `bulge` hoặc `fisheye` của chuỗi post | `thermal-distortion`, `gravitational-lens` |

### 5.6 Thời gian

Chỉ khả thi vì một shot có thể được hỏi ở bất kỳ thời điểm nào.

| Loại | Người xem thấy | Cảm giác và cách dùng | Beat | Engine | HyperFrames |
|---|---|---|---|---|---|
| Stutter | Shot đi lặp lại những khoảnh khắc đầu của chính nó trong các lát ngày càng ngắn | Một đĩa nhạc bị DJ chặt. Vào một drop | 2 + 0 | `stutter` | không có |
| Hold | Frame cuối đứng yên | Một hơi thở | 0.25 | breath | hạn chế |
| Speed ramp | Shot cũ tăng tốc vào cú cắt, shot mới giảm tốc ra khỏi nó | Đà | 1 + 1 | chưa dựng thành một loại; một shot có thể làm bằng clock riêng của nó | lane `rate` |
| Reverse | Shot cũ chạy ngược | Hoàn tác | 1 | chưa dựng | không có |
| Loop | Shot cũ lặp một bar cho đến cue | Chờ đợi | bar | chưa dựng | không có |

Trail và echo (vệt và dư ảnh) cần các frame đã có trước đó. Một shot là hàm thuần theo thời gian không có chúng, nên một echo được vẽ bằng cách render lại các thời điểm trước, làm chi phí tăng gấp bội. Dùng nó cho một khoảnh khắc, không phải cho cả một đoạn.

### 5.7 Vào một drop

Tất cả đều theo ba phần của mục 2, với lead 2 beat và tail 1.5.

| Loại | Build | Breath | Impact | Phù hợp | Engine |
|---|---|---|---|---|---|
| Implode | Hình xoáy và bị hút vào một điểm | Một chấm màu signal của phim | Một vòng màu đó lan ra từ chấm | Drop đầu tiên; sự xuất hiện của thứ duy nhất | `implode` |
| Stutter squeeze | Shot lặp lại trong các lát ngắn dần trong khi khung hình khép thành một khe | Một đường sáng | Khe bật mở | Một drop sau một build nặng chữ | `stutter` |
| Tunnel | Khung hình chứa các bản sao nhỏ hơn của chính nó, lồng nhau, và camera lao vào | Trắng | Một sóng xung kích | Một drop sau sự tăng trưởng hoặc lặp lại vô tận | `tunnel` |
| Breath | Hình mất màu, tối dần, khép quanh một điểm | Tối | Ba vòng, nối tiếp nhau | Cú bùng nổ sau nhiều bar im lặng | `breath` |
| Stretch | Các cột bị kéo lên thành vệt, khung hình đảo ngược theo hồi trống | Vệt được giữ | Các vệt rơi xuống, hai làn sóng | Drop cuối | `stretch` |
| Collapse to a line | Khung hình bị ép dẹt từ trên và dưới | Một đường | Đường mở ra thành shot mới | Chưa dựng | |
| Countdown | Các con số trên những beat cuối, mỗi lần lớn hơn | Con số cuối được giữ | Một chớp sáng | Chưa dựng. Phim vui tươi | |
| Blackout | Đèn tắt từng cái một | Tối, im lặng | Mọi đèn cùng lúc | Chưa dựng | |

### 5.8 In-world

Mạnh nhất và đắt nhất. Builder của ít nhất một trong hai shot tham gia, và storyboard mang một ghi chú nói rõ điều được yêu cầu.

| Loại | Người xem thấy | Các builder làm gì | Engine |
|---|---|---|---|
| Through | Một chữ cái lớn, một cánh cửa, một cửa sổ hoặc một lỗ khóa đứng trước camera. Camera đi qua lỗ mở của nó, và phía sau là shot kế tiếp | Shot đi có thể hiển thị cùng chữ cái đó và trao nó đi ở đúng kích thước và vị trí mà engine tiếp nhận. Chữ cái không được co lại trước khi bị ném đi | `through` (chữ cái; lỗ lớn nhất được tìm bằng flood fill) |
| Zoom vào một chi tiết | Shot kế tiếp nằm bên trong một chi tiết của shot này: một màn hình, một tấm thẻ, một ô trên một biểu mẫu. Camera lao vào cho đến khi chi tiết là toàn bộ khung hình | Shot ĐI hiển thị frame đầu của shot kế tiếp trên chi tiết đó và lái camera vào, để cuối cùng chi tiết lấp đầy khung hình chính xác | `zoom-in` |
| Pull ra khỏi một chi tiết | Shot trước hóa ra là một chi tiết của shot này. Camera lùi lại và thế giới lớn hơn hiện ra | Shot ĐẾN bắt đầu với frame cuối của shot trước lấp đầy khung hình, ghim vào chi tiết, rồi lùi lại | `pull-out` |
| Travel | Hai shot là hai nơi của cùng một thế giới. Camera đi từ nơi này sang nơi kia không cắt | Một thế giới được vẽ, và camera của shot đầu kết thúc chính xác ở nơi camera của shot sau bắt đầu | `travel` (engine không làm gì tại cú cắt) |
| Match | Hình cuối và hình đầu chung một hình dạng ở cùng vị trí | Hai hình được căn chỉnh tới từng pixel | `match` |
| Shatter | Một thứ trong shot lao thẳng vào người xem. Chỗ nó va vào, khung hình vỡ thành các mảnh rơi xuống, và phía sau là shot kế tiếp | Vật thể phải lớn trong những frame cuối và chạm ống kính trên cú cắt, tại điểm focus. Nếu không thấy thứ gì va vào kính, cú vỡ không có nguyên nhân | `shatter` |
| Object wipe | Một thứ băng qua sát ống kính và mang shot kế tiếp vào phía sau nó | Vật thể được canh giờ để che khung hình trên cú cắt | chưa dựng |
| Hand-off | Một thứ bị ném ra khỏi shot này rơi vào shot sau | Hai builder thống nhất điểm, tốc độ và beat | chưa dựng |
| Flood | Chất lỏng, mực hoặc màu của cảnh tràn ngập khung hình, và nền của shot kế tiếp là màu đó | Shot đi tràn ngập; shot đến bắt đầu trên màu phẳng đó. `flood` của engine làm việc này không cần các shot: một màu phình ra từ focus vượt qua mọi góc và, sau cú cắt, co lại vào focus và để lại shot kế tiếp | `flood`, tại focus, kèm một màu; in-world bởi các shot |
| Fold | Thế giới gập lại như giấy, và mở ra thành thế giới kế tiếp | Cả hai shot được vẽ trên các tờ giấy. `fold` của engine gập các hình hoàn chỉnh như một tấm bản đồ 3 x 3 ô | `fold` cho phiên bản screen-space; in-world bởi các shot |
| Break out of the frame (thoát khỏi khung) | Một thứ được giữ trong một hình chữ nhật (một poster trong khung, một tính năng trên màn hình điện thoại) rời khỏi nó: nó vượt qua cạnh và đi vào thế giới phía trước, và khung nó rời đi giờ là một phần của hình kế tiếp | Shot vẽ khung, nội dung bị clip theo khung, và thứ thoát ra sau phần clip, không bị clip, ở phía trước (xem bên dưới) | không phải loại của engine: shot tự làm, và theo sau là một cú cắt thường, một `push` hoặc một `zoom-in` |
| Lights | Đèn tắt ở một nơi và bật ở nơi khác | Shot đi tối dần từ chính các ngọn đèn của nó; shot đến sáng lên từ đèn của chính nó | chưa dựng |
| Scale journey (hành trình tỉ lệ) | Một cú zoom liền mạch qua các tỉ lệ: pixel trở thành thành phố | Mỗi chặng được vẽ để đọc được vừa như một tổng thể vừa như một phần. Các shot chung một đường cong zoom và gặp nhau bằng `travel`: xem `camera.md`, mục 3.7 | `travel`, với `scaleCam` trong các shot |
| Turning solid | Khung hình là một mặt của khối lập phương hoặc lăng trụ xoay để lộ mặt kế tiếp | Mỗi shot được vẽ phẳng trên mặt của nó | chưa dựng |
| Morph | Chủ thể của shot này biến hình thành chủ thể của shot sau | Cả hai hình được dựng từ cùng số điểm | chưa dựng |
| Hidden cut | Một thứ đi qua sát ống kính và làm đen khung hình trong một khoảnh khắc | Cú cắt được thực hiện trong bóng tối | chưa dựng |

Khi một trong hai shot vẫn còn là một storyboard card, engine phát một bản thế chỗ: một zoom thường cho hai loại dùng chi tiết, một whip cho travel, một punch cho match. Nó chạy được nhưng nhạt nhẽo so với bản thật. Đừng đánh giá một transition in-world qua bản thế chỗ của nó.

Một transition in-world nảy sinh từ hình ảnh. Nếu storyboard có hai shot mà một cái rõ ràng chứa cái kia, hãy đề xuất nó. Nếu không có, đừng bẻ cong các shot cho đến khi có.

#### Thoát khỏi khung

Hình ảnh một cái khung với nội dung của nó, nơi một thứ không chịu ở yên bên trong. Nó được vẽ thành ba layer, theo thứ tự này, mỗi layer là một hàm theo thời gian:

| Layer | Vẽ | Ghi chú |
|---|---|---|
| Cái khung và những gì ở lại trong nó | Cái khung (viền giấy của poster, một chiếc điện thoại từ `phone`, một cửa sổ từ `browserWindow`), rồi nội dung của nó sau `clipTo(c, screen)` | Nội dung có thể tiếp tục chuyển động bên trong |
| Bóng của thứ thoát ra | Trên khung và trên mặt đất phía sau nó, lệch ra xa nguồn sáng, càng mềm khi thứ đó càng ra xa | Không có bóng, thứ đó trông như bị dán lên; bóng nói rằng nó đã rời khỏi mặt phẳng |
| Thứ thoát ra, không bị clip | Phía trước mọi thứ, lớn lên một chút khi tiến về phía camera, vượt qua cạnh khung trên một beat | Phần còn bên trong khung được vẽ có clip cho đến khi vượt qua, rồi vẽ toàn bộ |

Hai lỗi: thứ đó vượt qua cạnh trong một frame (nó phải được thấy là đang vượt qua, trong một hai beat), và không có gì trong khung phản ứng (nội dung phía sau có thể tối đi, hoặc khung có thể uốn, khi thứ đó rời đi). Sau cú thoát, shot có thể lùi lại, hoặc cắt bằng một `push` sang thế giới mà thứ đó đi vào.

### 5.9 Âm thanh đi kèm một cú cắt

Trong một phim cắt theo một bản nhạc hoàn chỉnh, âm thanh đã có sẵn và cú cắt được đặt lên nó. Ở chỗ có thể thêm hiệu ứng âm thanh, những âm sau đi cặp với các hình ảnh ở trên.

| Âm thanh | Đi kèm |
|---|---|
| Riser, reverse cymbal | Build của một loại drop, một crash zoom |
| Impact, low boom | Impact của một loại drop, shatter, gravity drop |
| Whoosh | Whip, push, object wipe |
| Click, tick | Hard cut trong một danh sách, tiles |
| Im lặng | Breath. Âm thanh hữu ích nhất trong tất cả |

## 6. Tham số

| Trường | Đơn vị | Ý nghĩa |
|---|---|---|
| `kind` | tên | Một trong các loại mà phim khai báo |
| `lead` | beat | Lấy từ cuối shot đi |
| `tail` | beat | Lấy từ đầu shot đến |
| `focus` | pixel của master frame, y hướng xuống; chuyển sang format khác theo tỉ lệ | Điểm mà transition xoay quanh: tâm của một iris, điểm va chạm, lỗ của một chữ cái. Mặc định: giữa sân khấu |
| `dir` | vector đơn vị trong khung hình | Hướng di chuyển cho push, whip, slices, spin, wipe, cover |
| `colour` | khóa palette | Cho `dip`, `cover` và `flood`: màu lấp đầy khung hình. Mặc định: `ink` cho dip, `signal` cho các loại khác. `cover` vẽ ba tấm: một sắc nhạt của màu, chính màu đó, và màu đặt tương phản với nền (sáng trước shot tối, tối trước shot sáng) |
| `text` | chuỗi | Cho `through`: các chữ cái đứng chắn đường |
| `size` | pixel | Cho `through`: kích thước các chữ cái khi chúng mới đứng chắn đường |
| `note` | câu | Cho các loại in-world: điều được yêu cầu ở các builder |

Màu của bất cứ thứ gì engine tự vẽ (chữ cái, tấm khối, đường nối) được đặt tương phản với nền của shot mà nó đứng trước: sáng trước shot tối, tối trước shot sáng.

### Các loại được thêm sau các phim tham chiếu

`iris`, `aperture`, `dip`, `wipe`, `cover`, `flood`, `fold` và `glitch` được dựng sau hai phim tham chiếu và mới chỉ được thấy trong still của một phim thử, chưa bao giờ trong một phim hoàn chỉnh. Một phim dùng một loại khi `shots.json` của nó ghi tên loại đó trong dictionary `transitions` (bộ sinh từ chối một `in` có loại không có ở đó). Các mục, để chép vào dictionary đó:

```json
"iris": {"label": "Iris", "what": "The new shot is seen through a circle that opens from the focus until it clears the frame."},
"aperture": {"label": "Aperture", "what": "Six blades close over the old shot to a point, and open again on the new one."},
"dip": {"label": "Dip to a colour", "what": "The old shot fades to a flat colour and the new one rises out of it."},
"wipe": {"label": "Linear wipe", "what": "A straight edge sweeps across in the direction of travel; behind it is the new shot."},
"cover": {"label": "Colour panels", "what": "Three flat panels of colour sweep in and cover the frame, then sweep on out and leave the new shot."},
"flood": {"label": "Flood", "what": "A colour swells from a point past every corner; after the cut it shrinks back into the point and leaves the new shot."},
"fold": {"label": "Folded map", "what": "The old shot folds up like a paper map, the packet turns over, and the new shot unfolds: the middle, the sides, the corners."},
"glitch": {"label": "Glitch", "what": "The frame breaks into bands that tear sideways and split their colours, showing more of the new shot as it goes."}
```

| Loại | Lead và tail đã hoạt động trong still | Ghi chú |
|---|---|---|
| `iris` | 0.5 + 1 | Cần cả hai hình. Một đường mảnh màu tương phản với nền chạy theo cạnh |
| `aperture` | 1 + 1 | Hiển thị một hình mỗi lúc; các lá khép kín tại cú cắt. Một cú giật nhỏ khi chúng mở |
| `dip` | 1 + 1 | Khung hình là màu phẳng tại cú cắt |
| `wipe` | 0.5 + 0.5 | `dir` [1, 0] quét từ trái; hướng nào cũng được |
| `cover` | 1 + 1 | Khung hình được phủ kín hoàn toàn tại cú cắt |
| `flood` | 0.625 + 1 ở 120 beat mỗi phút | Lead khoảng 0.3 giây: chậm hơn bị đọc như một cú mờ chậm, nhanh hơn thì nửa màn hình đổi trong một frame. Vòng tròn scale vượt góc xa nhất thêm một phần tám, nên không góc nào bị bỏ trống tại cú cắt |
| `fold` | 1.5 + 1.5 | Các góc gập trong hai phần năm đầu của lead, các cạnh trong hai phần năm tiếp theo, gói giấy lật trong một phần năm cuối; sau cú cắt thì ngược lại. Cần một tail đủ dài cho ba bước |
| `glitch` | 0.5 + 0.5 | Mạnh nhất tại cú cắt; thêm viền màu và một cú rung nhỏ vào cài đặt post |

## 7. Thêm một loại vào engine

1. Viết ra những gì người xem thấy trong build, tại cú cắt và sau đó, mỗi phần một câu.
2. Quyết định nó cần gì: một hình hay cả hai, một focus, một hướng, một mask.
3. Thêm nó vào danh sách các loại và vào dictionary trong shot list, kèm một label và một mô tả mà chủ sở hữu đọc được.
4. Viết nhánh shader hoặc phần vẽ mask. Giữ trạng thái là một hàm thuần của vị trí bên trong lead và tail.
5. Thêm khoảnh khắc hiệu ứng post của nó: push, flash, shake, tách màu, frame âm bản.
6. Quyết định bản thế chỗ được phát khi một shot vẫn còn là card.
7. Xem nó giữa hai storyboard card trước, rồi giữa hai shot thật. Một transition tinh chỉnh trên card thường quá yếu hoặc quá mạnh trên hình thật.
8. Xem nó từng frame qua cú cắt. Frame trước cú cắt và frame sau nó là nơi lỗi ẩn nấp.

## 8. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Nhạc drop còn hình chỉ thay đổi | Drop có một cú cắt thường | Cho nó một loại drop với build, breath và impact |
| Mọi cú cắt trông như preset của một phần mềm dựng phim | Chỉ dùng các loại screen-space | Thêm vài transition in-world ở những khoảnh khắc quan trọng |
| Transition chen chúc các shot | Các loại in-world ở hầu hết cú cắt | Giữ chúng ở một nhúm; hầu hết cú cắt là cắt thường |
| Cú cắt có cảm giác mềm và lỏng | Blend dài trên một bản nhạc nhanh | Rút ngắn còn nửa beat hoặc ít hơn; dùng cắt có nhấn |
| Một caption không đọc được ở đầu một shot | Nó bắt đầu dưới tail của một transition | Bắt đầu caption sau tail |
| Đoạn cuối của một shot bị mất | Builder không biết về lead của transition kế tiếp | Đưa lead và tail vào brief của mọi builder |
| Chữ cái của một `through` co lại trước khi bay | Chữ cái của shot đi lớn hơn kích thước mà engine bắt đầu | Đặt `size` và `focus` trong shot list và để shot đọc vị trí mà chữ cái của engine bắt đầu đứng |
| Không tìm thấy lỗ của một chữ cái | Font dựng chữ cái từ các contour chồng nhau | Tìm lỗ trên một bản vẽ nhỏ bằng flood fill, không phải từ các contour |
| Cú vỡ của một shatter không có nguyên nhân | Không thấy thứ gì chạm tới ống kính | Làm vật thể lớn trong những frame cuối và để nó đến trên cú cắt |
| Hai hình không khớp nhau trong một zoom vào chi tiết | Camera đi không kết thúc trên hình chữ nhật của chi tiết | Đóng khung hình chữ nhật chính xác ở cuối lead; blend camera đều theo tỉ lệ |
| Một still chụp tại cú cắt hiện một frame đỏ | Shot láng giềng không được nạp khi capture | Nạp cả hai shot khi kiểm tra một cú cắt |
| Một flood bị đọc như cú mờ chậm, hoặc nửa khung hình đổi cùng lúc | Lead của nó xa 0.3 giây | Đặt lead sao cho nó kéo dài khoảng 0.3 giây ở tempo của phim |
| Một "flood" in-world và `flood` của engine xung đột | Cả hai đều được yêu cầu | Chọn một: shot tự tràn ngập và cú cắt là cắt thường, hoặc engine tràn ngập trên các shot không biết gì về nó |
| Một thứ thoát khỏi khung trông như bị dán lên | Không có bóng, không có phản ứng trong khung | Cho nó một cái bóng trên khung và để khung đáp lại |
