# Hiệu ứng (Effects)

Một danh mục những gì có thể xảy ra bên trong một shot: mọi thứ chuyển động ra sao, xuất hiện và rời đi thế nào, đáp lại âm nhạc ra sao, và frame hoàn chỉnh được xử lý thế nào. Mỗi mục đều nói rõ nó dùng để làm gì, vì một hiệu ứng chẳng để làm gì thì chỉ là nhiễu.

Đọc file này khi: viết trường `move` của các shot trong storyboard, giao việc (brief) cho một builder, review một shot trông chết hoặc quá rối, hoặc mở rộng bộ kit dùng chung hay chuỗi hậu kỳ (post chain).

## 1. Hiệu ứng để làm gì

Một hiệu ứng xứng đáng có mặt khi nó làm một trong bốn việc.

| Việc | Câu hỏi nó trả lời | Ví dụ |
|---|---|---|
| Nó cho thấy một sự kiện | Vừa có chuyện gì xảy ra? | Một con dấu đập xuống, một đường liên kết chạm đích, một tấm thẻ bị cắt |
| Nó dẫn mắt người xem | Tôi nên nhìn vào đâu? | Một vòng tròn quanh bước đang làm, một điểm đánh dấu di chuyển, một vũng sáng |
| Nó cho thấy chất liệu | Thứ này làm bằng gì? | Hạt (grain) trên giấy, nét gạch bóng trên khối đặc, quầng sáng trên đèn |
| Nó giữ nhịp | Beat ở đâu? | Một cú đẩy trên tiếng kick, một cú giật trên tiếng snare |

Nếu nó không làm việc nào trong số đó, hãy cắt bỏ.

## 2. Phương pháp đòi hỏi gì ở mọi hiệu ứng

| Đòi hỏi | Nghĩa là |
|---|---|
| Nó là một hàm của thời gian | Với thời điểm của frame, nó cho ra đúng một hình, bất kể trước đó đã vẽ gì |
| Tính ngẫu nhiên của nó có seed | Lấy từ hash của các số cố định: một chỉ số, một số thứ tự frame, một seed. Không bao giờ dùng nguồn ngẫu nhiên của hệ thống |
| Mô phỏng của nó chạy một lần | Thứ gì cần lịch sử (ngọc trai chất đống, một bầy đàn, vải) thì được mô phỏng khi shot tải lên, sau đó tra theo thời gian |
| Các hạt (particle) của nó là chỉ số | Một hạt là số thứ tự của nó trong một đợt bắn (burst) hay một dòng (stream): nơi nó sinh ra, bay nhanh thế nào và sống bao lâu đều lấy từ hash của số đó, còn vị trí hiện tại là một công thức đóng (closed form) theo tuổi của nó. Không mang danh sách hạt từ frame này sang frame khác (mục 8) |
| Thứ gì nhảy bậc thì lấy từ frame | Một bộ đếm, một từ thay đổi, trạng thái của một công tắc: tính từ thời điểm của frame đầu ra, để không bao giờ bị in ra hai giá trị cùng lúc |
| Thứ gì di chuyển thì lấy từ khoảnh khắc | Vật thể, camera, một đường đang được vẽ |
| Vệt nhòe của nó được vẽ ra | Khi phát trực tiếp thì không có motion blur. Một thứ di chuyển nhanh được chính shot vẽ thành một vệt, nếu nó nên có vệt (`withMotion`, mục 7) |

## 3. Mọi thứ chuyển động ra sao

### Nguyên tắc

| Nguyên tắc | Trong một phim dựng theo nhạc |
|---|---|
| Thời điểm (timing) | Mọi thứ xuất hiện, va chạm và thay đổi trên một beat hoặc một phần chia của beat |
| Rời đi ngay, dừng lại từ từ | Kiểu ease mặc định. Nó tạo cảm giác dứt khoát |
| Chuẩn bị (anticipation) | Một chuyển động nhỏ lùi lại trước chuyển động chính. Chuyển động có lấy đà thì đánh mạnh hơn |
| Vượt quá rồi ổn định (overshoot and settle) | Thứ có trọng lượng đi quá vị trí của nó rồi quay lại. Một lò xo, với tần số và độ tắt dần (damping) chọn riêng cho từng thứ |
| Nén và giãn (squash and stretch) | Thứ mềm dẹt ra khi tiếp đất và dài ra khi bay. Thứ cứng thì không |
| Chuyển động theo đà (follow-through) | Những phần lủng lẳng (dây cáp, quai, tấm giấy) đến sau thân chính |
| So le (stagger) | Nhiều thứ xuất hiện lần lượt, cách nhau một phần nhỏ của beat, không bao giờ cùng lúc trừ khi "cùng lúc" chính là ý đồ |
| Đường cong (arcs) | Vật bị ném bay theo đường cong |
| Hành động phụ (secondary action) | Thứ nhỏ đáp lại thứ lớn: bụi khi tiếp đất, một bóng đổ tụ lại trước khi rơi |
| Giữ (hold) | Không có gì chuyển động. Sau một chuỗi sự kiện, việc giữ yên cũng là một sự kiện |
| Cường điệu (exaggeration) | Cặp được hoán đổi là thứ lớn nhất, sáng nhất trong frame vào khoảnh khắc nó hoán đổi |
| Nhảy bậc (steps) | Animate theo bậc hai hoặc ba frame tạo cảm giác làm bằng tay. Các bậc lấy từ số thứ tự frame |

### Các kiểu ease

| Ease | Cảm giác như | Dùng cho |
|---|---|---|
| Linear (tuyến tính) | Một cỗ máy, một sự trôi dạt | Băng chuyền, cuộn, camera trôi chậm |
| Out, mạnh (exponential, quintic) | Dứt khoát | Gần như mọi sự xuất hiện và mọi chuyển động camera |
| In, mạnh | Rơi, tăng tốc dần | Những thứ rời đi; đoạn dồn lên trước một cú đánh |
| In và out | Lịch sự | Đổi vị trí mà không muốn bị chú ý |
| Back, out | Hơi vượt quá một chút | Những thứ nhỏ bật vào |
| Elastic (đàn hồi) | Cao su | Hiếm khi; đồ chơi |
| Spring (lò xo) | Trọng lượng | Tiếp đất, các bước, thứ được bắt lấy sau một cú nhảy |
| Lò xo được thả ra | Một thứ đang bị giữ rồi được thả ra, giữ nguyên tốc độ | Một thao tác kéo được thả, mối nối của vòng lặp, một lần chuyển giao giữa hai shot |

Trong starter, các ease nằm trong `src/engine/util.ts` (`ease`, `springStep`, `settle`, `prog`, `keys`). `ease` chứa các họ thông dụng, mỗi họ có in, out và in-out: quad, cubic, quart, quint, sine, circ, expo và back, cộng thêm `outElastic` và `outBounce`. `settle(t, duration, from, to, v0, sharpness)` là một chuyển động không vượt quá, đáp chính xác vào `to` tại `duration` và ở yên đó, mọi đạo hàm bằng không; nó có thể bắt đầu với tốc độ `v0` tiếp nhận từ một chuyển động trước đó (`settleVel` cho biết tốc độ của nó). Các lò xo dưới đây tiến về trạng thái nghỉ mà không bao giờ chạm tới, nên một đoạn giữ cần thực sự đứng yên thì dùng `settle`.

### Lò xo (springs)

| Hàm (`src/engine/util.ts`) | Cho ra gì | Dùng cho |
|---|---|---|
| `springStep(t, freq, damping)` | 0 trước 0, rồi từ 0 đến 1 với một lần vượt quá. Nó đã chuyển động ngay từ đầu. Damping phải nhỏ hơn 1, nếu không nó trả về NaN | Bật lên, tiếp đất, một giá trị đổi đích nhiều lần (tổng của một bước cho mỗi lần đổi, `short-pieces.md`, mục 7) |
| `springRelease(t, x0, v0, freq, damping)` | Độ lệch khỏi vị trí nghỉ của một lò xo tắt dần thật được thả tại thời điểm 0 từ `x0` với vận tốc `v0` (đơn vị trên giây); `x0` trước 0. Mọi damping từ 0 trở lên: dưới 1 thì vượt quá, bằng 1 ổn định nhanh nhất mà không vượt quá, trên 1 thì bò dần về | Một tấm thẻ bị kéo rồi thả bật về từ chỗ ngón tay rời ra, với tốc độ nó đang có. Một con trỏ hay camera phải đến mối nối vòng lặp với đúng tốc độ lúc bắt đầu. Bước thực sự từ trạng thái nghỉ là `1 + springRelease(t, -1, 0)` |
| `springReleaseVel(t, x0, v0, freq, damping)` | Vận tốc của cùng lò xo đó, trên giây | Vệt nhòe của vật, tốc độ thả của lò xo kế tiếp trong một chuỗi, kiểm tra một mối nối có khớp không |

Một thao tác kéo, như một hàm của thời gian: trong lúc đang kéo, vật đi theo con trỏ; tại thời điểm thả `tr`, đọc vị trí và vận tốc từ chính đường đi của con trỏ (`springPath` của `src/scenes/parts/kit-devices.ts` trả về cả hai), và từ đó trở đi vật là `rest + springRelease(t - tr, x - rest, vx)`, cho từng trục (`released` trong cùng file làm cả hai trục). Không có gì được mang từ frame này sang frame khác: mọi giá trị tại mọi thời điểm đều tính từ đường đi và thời điểm thả.

Với một nhân vật, các nguyên tắc tương tự được áp dụng cho các bộ phận của rig, với các tư thế key, độ trễ cho follow-through, squash and stretch, và sự sống khi đứng yên (idle life): `characters-and-story.md` và `src/scenes/parts/kit-rig.ts`.

## 4. Giữ nhịp

### Hàm trợ giúp (helpers)

Tất cả đều nhận beat theo đồng hồ riêng của shot, bắt đầu từ không ở frame đầu tiên của shot. Trong starter chúng nằm trong `src/scenes/parts/kit-frame.ts`, trừ `punch` và `pushOnBeat` nằm trong `kit-camera.ts`.

| Helper | Trả về | Dùng cho |
|---|---|---|
| `hit(beats, at, halfLife)` | 0 trước beat, rồi 1 giảm một nửa sau mỗi `halfLife` beat | Điểm nhấn của một sự kiện: một ánh lóe, một sự phồng lên |
| `over(beats, at, dur, ease)` | 0 đến 1 trong một số beat | Một chuyển động bắt đầu trên một beat |
| `during(beats, at, until)` | True giữa hai beat | Hiển thị một thứ trong một khoảng |
| `steps(beats, at, every)` | Đã qua bao nhiêu bước nguyên | Bộ đếm, danh sách dài dần, các cú cắt bên trong một shot |
| `groove(beats, every, offset, halfLife)` | Một điểm nhấn lặp lại | Kick (`every` 1), phách nghịch (`offset` 0.5), back-beat (`every` 2, `offset` 1) |
| `since(audio, frame, beats)` | Số giây kể từ một beat | Đầu vào cho một lò xo, một đợt bắn hạt, chữ chuyển động |
| `punch`, `pushOnBeat` | Một hệ số cho zoom | Cách camera đáp lại một cú đánh hoặc mỗi tiếng kick |

### Âm nhạc làm gì, và hình ảnh đáp lại ra sao

| Trong âm nhạc | Trong hình ảnh |
|---|---|
| Kick | Frame bị đẩy, một vòng tròn đập nhịp, một thứ tiếp đất |
| Snare, clap | Một ánh chớp, một cú giật, một sự đổi trạng thái |
| Hi-hat, nốt móc kép | Những thứ nhỏ lặp lại: tích tắc, chấm, viên đá, răng bánh răng |
| Phách nghịch (off-beat) | Câu đáp cho những gì beat vừa làm: món ăn ra sau khi phiếu gọi món vào |
| Bass phồng lên dưới kick | Những thứ thở: tỉ lệ, độ sáng |
| Build, trống dồn | Tăng tốc: sự kiện ở nửa beat, rồi một phần tư, rồi một phần tám beat; nghiêng, chen chúc, một con số chạy loạn |
| Beat cuối cùng trước drop | Mọi thứ dừng lại |
| Drop | Sự kiện lớn nhất của đoạn, trên beat đầu tiên |
| Break, trống tắt | Tĩnh lặng. Chữ |
| Im lặng | Chờ đợi. Một frame đứng yên, một thứ nhỏ lặp lại |
| Câu nhạc tám ô nhịp | Một ý |

Các sự kiện được đặt theo beat đọc từ lưới đã đo. Không bao giờ theo giây, không bao giờ từ một con số tempo.

## 5. Xuất hiện và rời đi

| Xuất hiện | Trông như | Hợp với |
|---|---|---|
| Tiếp đất (land) | Rơi xuống từ trên, vượt quá, ổn định; có bụi hoặc một cú giật | Vật có trọng lượng |
| Đập (slam) | Xuất hiện với kích thước đầy đủ trong một frame, kèm ánh chớp và rung | Tên, con dấu, phán quyết |
| Bật (pop) | Phóng to từ không có gì với một chút vượt quá | Thứ nhỏ, huy hiệu, nhãn |
| Trượt (slide) | Đi vào từ một cạnh và chậm dần đến chỗ nghỉ | Bảng, thẻ, mục kế tiếp |
| Trồi lên từ một đường | Đi lên từ dưới một đường mà bên dưới đó không nhìn thấy được, không mờ dần | Tiêu đề, chữ của một phim ra mắt (`riseFromLine`, mục 7) |
| Nghiêng vào (tilt in) | Đến trong phối cảnh, ngả ra sau, rồi nằm phẳng chính diện | Thẻ, ảnh chụp màn hình, poster (`tiltIn`, mục 14) |
| Vẽ ra (draw on) | Đường viền tự vẽ, rồi được tô | Sơ đồ, lộ trình, bản vẽ |
| Gõ ra (type on) | Từng chữ cái xuất hiện sau một con trỏ | Tiêu đề, prompt, câu cuối |
| In ra | Đi ra từ một khe, từng dòng một | Hóa đơn, vé, nhãn |
| Lật (flip) | Lật lại để lộ mặt | Thẻ, ô, chữ split-flap |
| Lắp ráp (assemble) | Các bộ phận bay vào và ghép lại | Logo, một hình tạo bởi nhiều thứ |
| Mở gấp (unfold) | Mở ra từ một nếp gấp | Giấy |
| Mọc lên (grow) | Trồi lên từ mặt đất, hoặc đầy dần từ dưới | Thanh (bar), chất lỏng, tháp |
| Sáng lên | Đã ở đó, tối; giờ thì sáng | Thiết bị khi đường liên kết tới, đèn |
| Được lộ ra | Thứ ở phía trước di chuyển đi | Hé lộ (reveal) |
| Tan vào (melt in) | Một giọt phồng lên, giãn ra và thành hình | Thanh công cụ bằng kính, pill, nút (`Liquid`, mục 15) |

| Rời đi | Trông như | Hợp với |
|---|---|---|
| Cắt (cut) | Biến mất cùng shot | Hầu hết mọi thứ |
| Rơi | Rơi ra khỏi frame | Thất bại, thứ bị từ chối |
| Bị ném | Bay ra, lộn nhào | Một tiêu đề bị cắt, một bưu kiện bị bật ra |
| Bị xé | Bị giật ra tại một đường xé | Hóa đơn, ghi chú |
| Bị gạch bỏ | Bị hai nét gạch ngang qua; vẫn ở đó, bị từ chối | Lựa chọn tồi |
| Thu nhỏ biến mất | Co lại thành không | Thứ nhỏ |
| Bị che phủ | Thứ kế tiếp đáp xuống lên nó | Chồng, đống |
| Tối đi | Ánh sáng rời khỏi nó | Những người đã rời đi; một liên kết bị cắt |
| Vỡ vụn (shatter) | Vỡ ra tại chỗ bị đánh; các mảnh bay, xoay và rơi, vẫn mang hình ảnh của nó | Một poster, một tấm kính, một phán quyết bị lật (`shatter`, mục 8) |
| Thoát ra khỏi khung | Rời khỏi hình chữ nhật đang chứa nó và bước vào thế giới phía trước | Một tính năng rời khỏi điện thoại, một poster bước ra khỏi khung (`transitions.md`, mục 5.8) |

Những thứ rời đi ở cuối một shot hiếm khi đáng để vẽ: cú cắt đã loại bỏ chúng.

## 6. Vẽ

| Hiệu ứng | Trông như | Dùng cho |
|---|---|---|
| Đường được vẽ ra | Một nét dài dần theo đường đi của nó | Lộ trình, đường nối, đường viền |
| Chữ viết tay | Các chữ được một cây bút viết từng nét | Ghi chú chen vào lề, chữ ký |
| Gạch bóng (hatching) | Bóng đổ tạo bởi các đường đi theo hướng sáng | Khối đặc trong phong cách in |
| Tô mặt cắt | Mặt cắt của một vật được lấp bằng các đường chéo đều | Hình cắt (cut-away) |
| Tràn màu (flood) | Màu lấp đầy một hình từ một phía hoặc từ một điểm | Dây dẫn mang dòng điện, thanh tiến trình |
| Bút dạ quang | Một nét rộng trong mờ phía sau một từ hoặc dọc một lộ trình | Lựa chọn được chọn giữa nhiều cái |
| Gạch xuyên (strike-through) | Hai nét mạnh gạch ngang | Từ chối |
| Vòng, ngoặc | Một vòng tròn hoặc dấu góc đánh dấu quanh một thứ | "Cái này, ngay bây giờ" |
| Đường dẫn và nhãn | Một đường mảnh từ một bộ phận tới một nhãn nhỏ | Gọi tên bộ phận |
| Đường viền đứt nét | Hình dạng của một thứ chưa có ở đó, hoặc đã rời chỗ | "Chưa làm"; một ô trống |
| Cắt | Một đường sáng chạy xuyên qua giấy, một khe tối mở ra phía sau, các mảnh tách rời | Một thứ trở thành nhiều thứ |
| Bấm lỗ (punch) | Một dụng cụ đóng lại; một lỗ xuất hiện; một mẩu bay ra | Vé |
| Đóng dấu (stamp) | Một bóng đổ áp xuống từ trên, rồi dấu in, ấn mạnh | Phê duyệt, một cái tên |
| Vò, xé, gấp | Giấy cư xử như giấy | Bản nháp bị vứt bỏ |
| Biến hình (morph) | Một đường viền biến thành đường viền khác | Cùng một ý tưởng dưới hai dạng |
| Rung nét (boil) | Các đường được vẽ lại với chút thay đổi mỗi hai hoặc ba frame | Sự ấm áp của nét vẽ tay |

## 7. Chữ chuyển động

Kỹ thuật và quy tắc nằm trong `type-and-captions.md`. Các hiệu ứng:

| Hiệu ứng | Trông như | Dùng cho | Trong starter (`src/scenes/parts/kit-type.ts`) |
|---|---|---|---|
| Máy đánh chữ có con trỏ | Từng chữ cái một; con trỏ nhấp nháy theo beat | Tiêu đề, prompt, câu kết | Do shot vẽ; `terminal` của `kit-devices.ts` gõ các dòng của nó |
| Đập (slam) | Từ hiện kích thước đầy đủ trên beat | Tên | Do shot vẽ |
| Đóng dấu | Từ hiện như một dấu in | Tên trên giấy | Do shot vẽ |
| Split-flap | Các chữ cái lách cách xoay tới từ đích | Bảng, menu | Do shot vẽ |
| Trồi lên từ một đường | Từng chữ cái đi lên từ dưới đường chân chữ (baseline), mỗi chữ một lò xo, cách nhau một chút; không có gì hiện dưới đường | Tiêu đề ra mắt, phong cách keynote cao cấp | `riseFromLine` |
| Chữ trên lò xo | Từng chữ cái bay vào từ một độ lệch, vượt quá rồi ổn định, có vệt nhòe dọc chuyển động và tách hai màu viền khi đang nhanh | Nhận diện động (kinetic identity), showreel, một từ phải có cảm giác vật lý | `springLetters`, xây trên `withMotion` |
| Vệt nhòe (smear) | Một thứ nhanh được vẽ thành các bản sao lùi về dọc đường đi, mờ dần, có thể kèm viền màu | Bất kỳ chữ hay hình nào chuyển động nhanh hơn mắt theo kịp | `withMotion` (vệt kéo phía sau), `blurY` (blur dọc canh giữa vật) |
| Bộ đếm | Các chữ số lăn như đồng hồ công-tơ-mét: mỗi chữ số một bánh xe, bánh cao hơn chỉ quay khi mọi bánh thấp hơn lăn qua, bánh quay nhanh bị nhòe | Số lượng tăng dần, số liệu lớn | `odometer`, trong một font có chữ số đều chiều rộng (giọng máy móc) |
| Cuộn máy đánh bạc (slot reel) | Các mục quay qua một ô cửa, nhòe khi nhanh, mờ và ép dẹt về phía mép trống, rồi dừng ở một mục với một tiếng cạch nhỏ | Chọn một trong nhiều, vòng quay tính năng | `reel` và lượt chạy `reelSpin` |
| Marquee | Các hàng chữ chạy ngang mãi mãi, nghiêng, lấp đầy frame, các hàng lần lượt tô đặc và viền rỗng, chạy ngược chiều nhau | Showreel, poster, danh sách kỹ năng | `marquee`; đường viền bằng `setWord` |
| Ticker | Một hàng mục chạy qua một dải băng, mờ ở hai đầu, trên một tấm nền | Tin tức, phim ra mắt, "ba từ" | `ticker` |
| Trộn giọng chữ trong một dòng | Tiêu đề sans với một từ serif, màu nhấn, nghiêng | Phong cách ra mắt: "Every *platform*." | `runs` (xem phần dưới về độ nghiêng) |
| Ép (crush) | Các dòng bị ép hẹp và sát dần đến khi va vào nhau | Quá nhiều, nói cùng lúc | Do shot vẽ |
| Xáo chữ (scramble) | Các chữ cái ngẫu nhiên lắng lại thành từ | Máy móc, giải mã | Do shot vẽ, chữ cái lấy từ hash của số thứ tự frame |
| Lớp (layers) | Từ có thêm hết đường viền này đến đường viền khác | Một cái tên tự quấn quanh mình | Do shot vẽ |
| Trên đường cong | Từ đi theo vòng tròn mà nó gọi tên; các chữ cái uốn theo | Nhãn của vòng tròn và cung | `bentText` với `onArc` |
| Trên sóng | Đường chân chữ là một con sóng đang lan | Nước, âm thanh, một tiêu đề vui nhộn | `bentText` với `onWave` |
| Vừa chiều rộng | Mỗi hàng đặt cỡ lớn nhất mà chiều rộng cho phép | Thẻ kết | `fitLines` |
| Từng từ một | Một từ mỗi beat | Câu được nói theo nhịp | Do shot vẽ, từ lấy từ `frameClock` |

Mọi hàm ở trên nhận số giây kể từ lúc bắt đầu (`since` của `kit-frame.ts`) hoặc một độ lệch tăng theo thời gian, để shot có thể tua (seek) tới bất kỳ đâu. Thứ gì nhảy bậc (từ nào, cuộn đã dừng ở mục nào) thì đọc từ đồng hồ riêng của frame; thứ gì di chuyển (một chữ cái trên lò xo, một bánh xe đang quay) thì từ khoảnh khắc.

### Vệt nhòe

`withMotion(c, vx, vy, motion, draw)` vẽ một vật đang chuyển động: hai bản sao viền màu tách dọc chuyển động (mặc định cyan và magenta, tách `fringe` px trên mỗi 1000 px/s), rồi các bản sao lùi về dọc đường đi trong `shutter` giây, mỗi bản đủ mờ để cộng lại chúng mờ dần từ `density` phía sau vật đến không, rồi đến chính vật. Số bản sao theo chiều dài vệt nhòe (một bản mỗi `spacing` px, tối đa `maxCopies`), nên vật chậm không tốn gì còn vật nhanh trông liền mạch. Shutter 0.03 s cho hiệu ứng blur; 0.08 s trở lên là một vệt nhòe được vẽ, như họa sĩ animation vẫn vẽ. Hãy truyền `extent`, kích thước của vật dọc theo chuyển động, để độ mờ đục ra đúng.

Khi bộ kit được xây, các ảnh tĩnh (still) cho thấy với vài bản sao cách xa nhau thì vệt nhòe trông như một chồng chữ cái rời rạc; với một bản sao mỗi ba pixel thì nó trông như chuyển động. Viền màu khoảng 3 px trên mỗi 1000 px/s thì thấy được mà không chói, trên nền sáng hay tối.

### Đường viền chữ cái: để uốn, để làm mask

Các font được tải hai lần: bởi trình duyệt cho `fillText`, và bởi opentype.js để lấy đường viền (`src/engine/type.ts`). Đường viền là thứ mà shot uốn cong hoặc dùng làm mask.

| Nhu cầu | Cách làm, chỉ với starter |
|---|---|
| Đường viền của một từ dưới dạng path | `textPath2D(text, family, size, x, y)`, hoặc các lệnh của nó với `textPathCommands` |
| Chữ trên cung, trên sóng, ép vào một điểm, bị nhiễu kéo | `bentText(text, family, size, warp)`: đường viền được cắt thành các đoạn thẳng ngắn và mỗi điểm được dịch bởi `warp(x, y)`. `onArc` và `onWave` là hai warp; bất kỳ hàm nào của một điểm cũng là một warp |
| Một mask bằng chữ | `c.clip(textPath2D(...))`, rồi vẽ những gì hiện xuyên qua; hoặc vẽ chữ màu trắng trên một layer và dùng nó làm mask cho `Liquid` (mục 15) |
| Một mask suy ra từ từ đang ra, cho một cú wipe xuyên qua hình chữ | Transition `through` tìm lỗ lớn nhất của một từ; một cú wipe xuyên qua toàn bộ đường viền thì do shot vẽ, clip hình kế tiếp vào đường viền khi nó lớn dần |
| Chữ viền rỗng không có các đường ở chỗ contour chồng nhau | `setWord(..., outline: true)`: nét được vẽ rộng gấp đôi và phần bên trong bị cắt đi. Font hiển thị của starter có contour chồng nhau, và một `strokeText` thông thường cho thấy chúng thành các đường cắt ngang chữ |
| Chữ được vẽ từng nét | Font một nét của `src/engine/stroke.ts` |
| Chữ 3D, đùn khối (extruded) | Không có trong kit: three.js có text geometry, và các lệnh đường viền có thể được đùn khối. Chưa thử trong starter |

Font biến thiên (variable font — một trục độ rộng hoặc độ đậm thay đổi được) không có trong starter: nó đi kèm file tĩnh, opentype.js chỉ đọc đường viền tĩnh, và Canvas2D không đặt được trục biến thiên. `type-and-captions.md`, mục 5, nói một phim cần nó phải thêm gì.

## 8. Nhiều thứ nhỏ

| Hiệu ứng | Trông như | Dùng cho | Chi phí |
|---|---|---|---|
| Tia lửa | Các vệt sáng ngắn từ một điểm, nguội dần và rơi | Kim loại chạm kim loại, một cú va | Thấp |
| Bụi | Các làn bụi mềm khi tiếp đất | Trọng lượng | Thấp |
| Bụi trong ánh sáng | Các hạt nhỏ trôi, chỉ sáng bên trong một chùm sáng | Một căn phòng yên tĩnh, đèn spotlight, một lần hé lộ | Thấp |
| Giấy bay | Các tờ giấy lộn nhào | Hỗn loạn, một đám đông cầm tài liệu | Trung bình |
| Confetti | Các mảnh màu bắn lên, phanh lại, rung rinh và rơi | Ăn mừng, một lần | Thấp |
| Đồng xu, đá quý bay vào bộ đếm | Chúng bắn ra, lơ lửng, rồi bay theo đường cong vào bộ đếm lần lượt; bộ đếm nảy lên và lăn số | Phần thưởng, doanh số, điểm số | Thấp |
| Lửa | Các lưỡi lửa bốc lên, thu hẹp, nguội và tắt | Nhiệt, nguy hiểm, bếp lửa | Trung bình |
| Khói | Các cuộn khói bốc lên, phồng ra và trôi | Sau lửa, sau vụ nổ, ống khói | Trung bình |
| Vụ nổ | Một ánh chớp, một quả cầu lửa chuyển thành khói, một vòng áp suất, mảnh vỡ bay theo đường cong, tia lửa | Một cú va chạm có thể theo dõi được, một bước ngoặt | Trung bình |
| Vỡ vụn | Một hình ảnh vỡ ra tại chỗ bị đánh và các mảnh của nó bay đi | Kính, poster, phán quyết | Trung bình: hình được vẽ một lần cho mỗi mảnh |
| Vòng sóng | Các vòng tròn lan ra từ một điểm | Phát sóng, một cú sốc | Thấp |
| Liên kết | Các cung từ nhiều thứ về một, hoặc từ một ra nhiều | Kết nối. Hướng đi chính là ý nghĩa | Thấp |
| Đường dòng chảy | Hàng nghìn đường dọc theo một trường | Dòng chảy, giao thông | Cao |
| Bầy đàn (swarm) | Nhiều tác tử | Đám đông | Mô phỏng một lần |
| Chất đống | Những thứ rơi xuống và chất thành đống | Ngọc trai, đồng xu, bưu kiện | Mô phỏng một lần |
| Cánh đồng thiết bị | Hàng trăm màn hình nhỏ sáng lên khi một con sóng đi qua | Người đăng ký, khán giả | Instanced |
| Vệt đường đi (trails) | Đường mà một vật đã đi qua | Lộ trình, quỹ đạo | Vẽ từ đường đi, không từ các frame cũ |

### Bộ kit hạt (particle kit)

`src/scenes/parts/kit-particles.ts` tạo các đợt bắn (burst) và dòng (stream) trong đó mỗi hạt là một hàm thuần của thời gian. Một hạt là một chỉ số; thời điểm sinh, vị trí, hướng, tốc độ, tuổi thọ, kích thước, độ xoay và hai số ngẫu nhiên dự phòng của nó đến từ `hash(seed, index, k)`; vị trí của nó ở một tuổi là công thức đóng của chuyển động bay dưới trọng lực không đổi với lực cản tỉ lệ với tốc độ. Thời gian tính bằng giây kể từ đợt bắn hoặc lúc dòng bắt đầu, vì vật lý tính bằng pixel và giây: đặt một đợt bắn lên một beat bằng `since(audio, f, beat)`.

| Hàm | Cho ra |
|---|---|
| `burst(spec, since)` | Các hạt còn sống của một đợt bắn: `count` hạt (sức chứa của nó), phóng ra cùng lúc hoặc rải trong `spread` giây |
| `stream(spec, since)` | Các hạt còn sống của một dòng: `rate` hạt mỗi giây, hạt i sinh tại i / rate, dừng tại `until`. Sức chứa của nó là `streamCapacity(spec)`, bằng rate nhân tuổi thọ dài nhất |
| `particleAt(emit, i, born, t)` | Một hạt, cho shot tự sắp xếp thời điểm sinh |
| `flightAt(x, y, vx, vy, gx, gy, drag, age)` | Chuyển động bay dạng công thức đóng, kèm vận tốc |
| Các trường của emitter | `at`, `radius` (sinh trong một đĩa), `angle` và `cone` (hướng phóng), `speed`, `life`, `size`, `spin`, `gravity`, `drag`, `turbulence` và `turbScale` (một độ trôi theo value noise tăng theo tuổi). Trường nào là một cặp `[min, max]` thì được lấy ngẫu nhiên cho từng hạt |
| `pullTo(p, x, y, from)` | Hút vào: từ một phần tuổi thọ trở đi, hạt bị hút về một điểm và tới đó khi nó chết; vận tốc đi theo, nên các vệt chỉ đúng hướng. Một luồng năng lượng tụ lại, tia lửa bị hút vào logo |
| `curveFlight(a, b, k, bend)` | Một đường bay cong từ điểm này tới điểm kia, kèm hướng: đồng xu vào bộ đếm, một vật ném vào khe |
| `orbitAt(cx, cy, r, a0, w, age, tilt)` | Một vị trí trên quỹ đạo nhìn nghiêng, kèm độ sâu để tính kích thước và thứ tự vẽ |

Các công thức (recipe) vẽ trên một layer Canvas2D, hoặc vào một line batch cho tia lửa:

| Recipe | Vẽ | Ghi chú |
|---|---|---|
| `drawSparks(lines, particles, style)`, `drawSparks2D(c, ...)` | Các vệt từ chỗ mỗi hạt vừa ở một khoảnh khắc trước đến chỗ nó đang ở, từ nóng sang nguội, mảnh dần | Một `LineBatch` ở blend `add` với đủ chỗ cho mọi hạt; màu trên 1 sẽ bloom |
| `confetti(c, spec, since)` | Các mảnh bắn ra một lần từ một điểm, phanh gấp, rung rinh khi rơi, lật mặt (một mảnh lần lượt hiện mỏng rồi rộng) | `colours` là khóa của palette hoặc mã hex |
| `coinsToCounter(c, spec, since)` và `drawCoin` | Đồng xu hoặc đá quý tản ra, rồi bay theo đường cong vào bộ đếm, lần lượt từng cái | Trả về `landed` và `sinceLast`: giá trị bộ đếm nhảy theo `landed`, còn cú nảy của nó là sự tắt dần của `sinceLast` |
| `fire(c, spec, since)` | Các lưỡi lửa sinh dọc theo một chân đế, lao lên, thu hẹp, giãn dọc đường bay và nguội đi | Vẽ với `lighter`; bắt đầu nó nửa giây trước khi được nhìn thấy, để ngọn lửa kịp bùng lên |
| `smoke(c, spec, since)` | Các cuộn khói bốc lên, phồng ra và trôi, sáng ở phía hướng về nguồn sáng | Vẽ bình thường |
| `explosion(hot, spec, since, cool, lines)` | Ánh chớp, quả cầu lửa gồm các cuộn chuyển thành khói từ mép, vòng áp suất, mảnh vỡ, tia lửa | Ánh sáng nóng thì cộng thêm còn khói thì che phủ, nên nó cần hai bề mặt: một layer composite ở chế độ `add` cho phần nóng, và một layer composite bình thường, vẽ trước, cho khói và mảnh vỡ |
| `shatter(c, spec, since, source)` và `shardsOf` | Một hình chữ nhật vỡ dọc theo các tia và các vòng lởm chởm quanh điểm va chạm; các mảnh bay ra từ đó (càng gần càng nhanh), xoay, rơi và giữ phần hình của mình | `source` là một canvas (canvas của một `Layer2D`) hoặc một hàm vẽ hình; vết vỡ lan ra ngoài trong vài phần trăm giây |
| `lightBeam(c, beam)` và `dustInBeam(c, beam, t)` | Một nón sáng mềm, và một tập cố định các hạt bụi trôi theo noise, chỉ sáng bên trong nón | Chùm sáng dùng conic gradient, Safari có từ phiên bản 16.1 |
| `puff(c, x, y, r, rgb, alpha, hard, stretch, angle)` | Một đĩa mềm có lõi chắc | Viên gạch cơ bản của lửa và khói; các lõi chắc chồng lên nhau thành cuộn, còn các làn chỉ toàn mép thì tan thành một khối |

Một layer cần phát sáng (lửa, phần nóng của vụ nổ) được composite ở chế độ `add` với tint hơi trên 1, ví dụ `{ mode: 'add', tint: [1.3, 1.3, 1.3] }`: canvas chỉ chứa giá trị tới 1, và tint cho phép phần sáng nhất vượt ngưỡng bloom. Chữ không bao giờ nằm trên layer đó.

Một batch đường hoặc điểm có sức chứa. Nó được định cỡ cho frame nặng nhất của shot, và frame đó phải được kiểm tra bằng mắt. Vượt quá sức chứa, một phần hình bị thiếu mà không báo gì.

Khi bộ kit được xây, các ảnh tĩnh cho thấy lửa tạo bởi các làn tròn lớn trông như một quả trứng phát sáng, không phải ngọn lửa; các lưỡi nhỏ giãn dọc đường bay và kéo vào phía trục thì trông như ngọn lửa. Khói tạo bởi các làn chỉ có mép mềm trông như sương mù; lõi chắc và một mặt sáng hơn thì trông như cuộn khói. Một vụ nổ ở một phần mười giây đầu là một quả cầu ánh sáng, và thế là đúng; tính cách của nó đến trong nửa giây sau, khi các cuộn tối dần từ mép.

## 9. Ánh sáng

| Hiệu ứng | Trông như | Dùng cho |
|---|---|---|
| Glow (quầng sáng) | Thứ sáng tỏa sáng ra xung quanh | Đèn, tín hiệu, lộ trình. Không bao giờ dùng cho chữ |
| Lóe sáng khi va | Một sự phồng sáng ngắn | Lúc một sự kiện tiếp đất |
| Quét sáng (sweep) | Một dải sáng lướt ngang một bề mặt | Kính, kim loại, "mới" |
| Chập chờn (flicker) | Một bóng đèn bắt sáng | Điện có lại |
| Vũng sáng | Một vùng sáng mềm trên nền tối, dạng halftone | Giới thiệu một thứ |
| Chùm sáng có bụi | Một nón sáng từ cửa sổ cao, bụi trôi trong đó | Yên tĩnh, thời gian trôi, spotlight (`lightBeam`, `dustInBeam`) |
| Bóng tụ lại | Một bóng lớn dần trước khi một vật rơi | Báo trước, theo đúng nghĩa đen |
| Bóng cứng | Một hình đen, lệch ra | Giấy, một vật chủ đạo trên sân khấu |
| Bóng mềm | Một tấm thẻ nhấc khỏi trang: một bóng tiếp xúc sát và một bóng mềm rộng | Thẻ giao diện, cửa sổ, phong cách ra mắt (`softShadow`, mục 12) |
| Dòng điện | Ánh sáng chạy dọc một sợi cáp | Điện, dữ liệu |
| Bếp lửa, than hồng | Ánh sáng chuyển từ ấm sang nóng | Căng thẳng tăng dần |
| Raster bars | Các thanh ngang bóng lắc lên xuống, bước dần quanh vòng màu | Demo scene, tiêu đề retro (`rasterBars` trong `src/engine/glsl/common.ts`, gọi từ một pass toàn màn hình) |

## 10. Frame hoàn chỉnh

Chuỗi hậu kỳ (post chain) làm việc trên toàn bộ frame sau khi các shot được ghép lại. Một shot chỉ thay đổi những gì khoảnh khắc của nó cần.

| Hiệu ứng | Làm gì | Tham số trong starter (`src/engine/post.ts`) | Nền tối (`POST_DARK`) | Nền sáng (`POST_LIGHT`) |
|---|---|---|---|---|
| Exposure (phơi sáng) | Độ sáng tổng thể | `exposure` | 1 | 1 |
| Bloom | Ánh sáng tỏa ra từ những gì sáng hơn một ngưỡng | `bloom`, `bloomThreshold`, `bloomKnee`, `bloomRadius` | 0.7, ngưỡng 1.0 | tắt |
| Halation | Một quầng ấm quanh vùng sáng | `halation` | 0.25 | tắt |
| Viền màu | Các màu tách ra về phía mép | `ca`, tính bằng pixel ở mép | 0.4 | 0.25 |
| Grain (hạt) | Nhiễu mịn | `grain` | 0.045 | 0.05 |
| Vignette | Các góc tối đi | `vignette` | 0.4 | 0.18 |
| Fade | Về đen | `fade` | | |
| Flash | Ánh sáng thêm vào theo màu giấy | `flash` | khi va | khi va |
| Rung (shake) | Frame bị dịch chuyển | `shake`, tính bằng pixel | khi va | khi va |
| Zoom | Frame được phóng to | `zoom` | các cú punch | các cú punch |
| Đảo màu (invert) | Tối và sáng đổi chỗ | `invert` | một hoặc hai frame khi va chạm | như vậy |

Bloom bắt đầu hơi dưới ngưỡng của nó, bằng độ rộng của knee. Vì thế chữ màu giấy trên nền tối được giảm tông nhẹ, để nó tránh xa ngưỡng đó.

### Các look mà một shot yêu cầu

Chúng tắt theo mặc định; một shot chỉ trả về tham số trong những frame cần nó, ví dụ `return { ...POST_DARK, crt: 1 }`. Mỗi cái chỉ là vài lệnh trong pass vốn đã hoàn thiện mọi frame, nên không cái nào tốn một pass riêng; khi tắt nó chỉ tốn một phép kiểm tra một con số. Những cái làm dịch chỗ một pixel nhìn vào (kaleidoscope, thấu kính, mosaic, kính, xé hình) sẽ dịch bloom theo hình.

| Look | Tham số | Làm gì | Phục vụ |
|---|---|---|---|
| Xoay sắc độ (hue rotation) | `hue` (radian) | Xoay mọi màu quanh vòng màu; xám vẫn là xám | Một điệp khúc chảy qua các màu, một palette bị lật cho verse thứ hai |
| Kaleidoscope (kính vạn hoa) | `kaleido` (số cung, 0 là tắt; 6 đến 12 trông như kính vạn hoa), `kaleidoTurn` | Frame bị cắt thành các cung đối xứng gương quanh tâm | Các đoạn ảo giác; xoay chậm bằng `kaleidoTurn` |
| Fisheye (mắt cá) | `fisheye` (-1 đến 0.9) | Phần giữa phồng ra (1 / (1 - fisheye) lần tại tâm), mép giữ nguyên; dưới 0 thì co lại | Một thấu kính, một giấc mơ, một cú đẩy mà không cần di chuyển camera |
| Bulge (phồng) | `bulge` (-1 đến 0.9), `bulgeAt` (px), `bulgeRadius` (px) | Cùng quy luật đó bên trong một vòng tròn: kính lúp trên một điểm | Kính lúp trên biểu đồ, các ô phồng lên khi thấu kính đi qua |
| Mosaic | `mosaic` (kích thước ô tính bằng px, 0 là tắt) | Frame thành các pixel lớn | Game, một hình rõ dần, một khuôn mặt bị che |
| Glitch | `glitch` (0 đến 1) | Các dải bị xé ngang với màu tách ra, vài khối nhảy, thay đổi mỗi frame cách một | Một lỗi, một cú đánh trên beat hồi phục ở beat kế tiếp |
| CRT | `crt` (0 đến 1) | Kính cong, scanline mỗi 3 px, mặt nạ phosphor ba sọc màu, góc bo tròn tối | Tivi, terminal, buổi ra mắt retro-futurist, demo scene |

Thêm hai lớp hoàn thiện nữa là pass của kit chứ không phải của chain, vì chúng cần một hình thứ hai (`src/scenes/parts/kit-post.ts`, mục 15):

| Hoàn thiện | Cách làm | Phục vụ |
|---|---|---|
| Difference | `Difference.render(renderer, layer, base, out)`: một layer blend kiểu difference lên hình của shot, tính trên các giá trị màn hình hiển thị | Một từ khổng lồ đảo màu bất cứ thứ gì nó đi qua |
| Blur theo độ sâu trên các layer phẳng | `Blur` trên mỗi layer bị mất nét, bán kính lấy từ `dofRadius(depth, focus)` | Các chip và thẻ lơ lửng phía trước và phía sau chủ thể |

Không có trong starter, và đáng thêm khi một look cần đến:

| Hiệu ứng | Look mà nó phục vụ |
|---|---|
| Lưới halftone phủ frame | In ấn |
| Ordered dither, ít màu | Máy tính đời đầu |
| Đường viền từ cạnh | Toon, bản vẽ kỹ thuật |
| Chỉnh màu (grade) bằng bảng | Phim nhựa |
| Letterbox | Điện ảnh |
| Light leaks (lọt sáng) | Phim nhựa |

## 11. Sơ đồ và hình minh họa

| Hiệu ứng | Trông như | Dùng cho |
|---|---|---|
| Bộ đếm trở thành chủ thể | Một nhãn giá lớn dần đến khi lấp đầy frame | Một con số vượt tầm kiểm soát |
| Thanh lớn dần | Từ đường gốc, tới giá trị của nó | So sánh |
| Tiến trình | Một thanh từ bước này đến bước cuối | Một quy trình |
| Điểm đánh dấu bước | Một điểm đánh dấu nhảy từ bước này sang bước khác, đôi khi đi trước nửa beat so với thứ nó đánh dấu | Chúng ta đang ở đâu |
| Xung trên dây | Một điểm sáng chạy dọc một kết nối | Một thông điệp. Một tới nhiều nghĩa là thông báo |
| Cùng nhãn trên mọi dây | Mỗi kết nối mang cùng một nhãn | Tất cả đều tới cùng một thứ |
| Yêu cầu bị từ chối | Một kẻ mới đến dạng đứt nét bị đóng dấu và dẫn tới cái đã tồn tại | Chỉ được có một |
| Các bộ phận định hình lại | Chân cắm hoặc ổ cắm đổi hình để vừa | Thích nghi |
| Hoán đổi trong một khe | Một thẻ ra, thẻ khác vào; mọi thứ xung quanh đứng yên | Có thể thay thế cho nhau |
| Nhãn "không đổi" | Các nhãn nhỏ trên những gì không di chuyển | Thứ ở lại chính là điểm mấu chốt |

## 12. Giao diện

| Hiệu ứng | Trông như | Dùng cho |
|---|---|---|
| Ngón tay nhấn | Một bàn tay có khớp: ngón tay cong lại, đầu ngón bè ra trên mặt kính | Màn hình cảm ứng |
| Click chuột | Di chuyển, nhấn, gợn sóng | Desktop |
| Vệt con trỏ | Các bản sao mờ dần của con trỏ ở chỗ nó vừa ở | Tốc độ, phong cách nhiều con trỏ của phim ra mắt |
| Kéo và thả | Vật đi theo con trỏ, và khi được thả thì bật về từ chỗ nó đang ở, với tốc độ nó đang có | Slider, thẻ, sheet (mục 3, "Lò xo") |
| Kéo để làm mới | Trang bị kéo xuống rồi bật về | Chờ đợi |
| Công tắc, dấu tick | Một điều khiển thay đổi và đích của nó thay đổi trong cùng beat | Nhân và quả |
| Gõ phím | Chữ xuất hiện sau một con trỏ | Form, prompt |
| Huy hiệu (badge) | Con số trên một icon lăn qua | Một số đếm đã thay đổi |
| Thứ đi ra từ một nút | Một yêu cầu đi vào, một thứ được tạo ra đi ra từ cùng chỗ | Sáng tạo |
| Màn hình trong thiết bị | Giao diện trên một chiếc điện thoại được vẽ, một cửa sổ trình duyệt, một terminal | Bối cảnh |
| Một cửa sổ mất nét phía sau | Một cửa sổ thứ hai, bị blur và hơi mờ, phía sau cửa sổ đang lấy nét | Chiều sâu trong một phim sản phẩm |

Một bàn tay, vẽ một lần, phục vụ mọi shot cần đến nó.

### Bộ kit thiết bị (devices kit)

`src/scenes/parts/kit-devices.ts` vẽ các khung mà một phim sản phẩm dùng để hiển thị màn hình. Mỗi hàm vẽ trên một context Canvas2D và trả về hình chữ nhật của màn hình bên trong; shot vẽ giao diện của nó ở đó sau `clipTo(c, screen)`. Một ảnh chụp màn hình thật được đưa vào bằng `loadBitmap` và `drawImageFit` của `src/engine/media.ts`.

| Hàm | Vẽ |
|---|---|
| `browserWindow(c, box, style)` | Bóng mềm của nó, khung (chrome) với ba đèn, thanh địa chỉ với `url`, các tab, `tone` sáng hoặc tối; trả về trang |
| `phone(c, cx, cy, h, style)` và `phoneGlass(c, screen, island)` | Một chiếc điện thoại cao `h`: khung kim loại chiếu sáng từ trên bên trái, nút bên cạnh, viền đen; rồi, phủ lên app, là island (0 đến 1 mở rộng nó thành một live activity) và một ánh bóng trên kính |
| `terminal(c, box, lines, style)` | Một cửa sổ tối có tiêu đề; các dòng bắt đầu bằng `$ ` hoặc `> ` có ký hiệu màu nhấn, dòng bắt đầu bằng `! ` là lỗi; `typed` ký tự trải qua các dòng, một caret dạng khối mà shot cho nhấp nháy theo beat |
| `softShadow(c, box, r, elevation, darkness, fill)` | Một tấm thẻ nhấc khỏi trang: một bóng mềm rộng và một bóng tiếp xúc sát, với màu nền của thẻ. Dùng shadow của context, thứ mọi trình duyệt đều có |
| `cursor(c, x, y, size, press)` | Một con trỏ với đầu nhọn tại điểm; `press` ép nó lại |
| `clickRipple(c, x, y, since, colour)` | Vòng lan ra từ một cú click trong nửa giây |
| `springPath(t, keys, freq, damping)` | Vị trí của một con trỏ bật như lò xo từ đích này sang đích khác, và vận tốc của nó. Damping gần 0.8 cho cú vượt quá nhỏ của một bàn tay biết mình đang đi đâu |
| `released(since, x, y, vx, vy, rest)` | Một vật được thả tại (x, y) đang di chuyển với (vx, vy), bật về `rest` |
| `cursorTrail(c, at, t, count, every, size)` | Con trỏ được vẽ ở chỗ nó đã ở 1, 2, ... bước trước, mỗi lần mờ hơn |

Một cửa sổ mất nét phía sau: vẽ nó trên một layer riêng, blur layer đó bằng `Blur` của `kit-post.ts` (bán kính khoảng 8 đến 12 px), và composite kết quả với `premult: false` và opacity hơi dưới 1 trước cửa sổ đang lấy nét. Không bao giờ dùng thuộc tính `filter` của canvas cho việc này: Safari không có nó.

## 13. Thời gian bên trong một shot

| Hiệu ứng | Trông như | Dùng cho |
|---|---|---|
| Đóng băng (freeze) | Mọi thứ dừng lại trong một beat | Khoảnh khắc trước break |
| Tua ngược | Mọi thứ đi lùi dọc theo đường đi của chúng | "Khi không có nó" |
| Lặp lại | Cùng một hành động lặp đi lặp lại, mỗi lần mạnh hơn một chút | Cố gắng, thất bại |
| Giữ trước khi kết | Tĩnh lặng từ một beat trở đi | Để phần cuối shot cho transition kế tiếp |
| Cắt theo bước | Shot cho thấy một cách sắp xếp khác trên mỗi beat | Bảy thẻ trong bảy beat |

## 14. Khối đặc (solids)

| Hiệu ứng | Trông như | Dùng cho | Lưu ý |
|---|---|---|---|
| Bàn xoay (turntable) | Vật xoay một vòng rồi dừng | Giới thiệu | |
| Hình tách lớp (exploded view) | Các lớp tách ra dọc một trục, mỗi lớp có nhãn | Một thứ được làm từ những gì | |
| Cắt đôi | Một mặt phẳng cắt qua vật, bên trong được tô bằng đường mặt cắt | Bên trong hoạt động thế nào | |
| Rót đầy | Chất lỏng dâng lên theo bậc, với một đợt dâng và lắng | Làm ra, trong một lượt | Một chiếc cốc thêm một lớp mỗi beat sẽ bị hiểu là thêm vào, không phải làm ra |
| Nhìn xuyên | Bên trong nhìn thấy qua thành | Bình chứa | Vật đặc bên trong được vẽ trước vật trong suốt và biến mất: đánh dấu chúng là trong suốt và sắp xếp thứ tự |
| Đường viền | Một đường đều quanh khối | Phong cách in | |
| Khắc (engraving) | Gạch bóng đi theo ánh sáng | Phong cách bằng sáng chế | Bước nét cố định trên màn hình |
| Bao bọc | Một lớp khép quanh vật và mang hình của nó | Thêm vào mà không thay đổi | Bản thân vật giữ màu trung tính |

### Thẻ trong không gian

Thẻ, ảnh chụp màn hình và poster đứng trong phối cảnh là three.js: Canvas2D có thể xoay và xiên một hình nhưng không cho nó phối cảnh được. `CardStage` của `src/scenes/parts/kit-devices.ts` chứa chúng.

| Phần | Làm gì |
|---|---|
| `new CardStage({ width, height, floor, reflect, fade, back, shade })` | Các thẻ cùng một kích thước. Với một mức `floor`, mỗi thẻ được vẽ lần thứ hai, phản chiếu trên sàn và mờ dần xuống dưới trong khoảng `fade`, như một sàn bóng phản chiếu |
| `setFace(i, texture)` | Thẻ i hiển thị một texture: mặt của nó vẽ một lần trên một `Layer2D` cùng kích thước thẻ (góc bo tròn là các góc trong suốt của nó), hoặc một hình từ `src/engine/media.ts` |
| `place(i, pose)` | Thẻ i đứng ở đâu trong frame này: vị trí, góc xoay quanh trục đứng và trục ngang, tỉ lệ, opacity. Mọi thẻ được đặt ở mỗi frame |
| `render(renderer, cam)` | Render vào target riêng của stage, có anti-alias; composite nó với `premult: false`. Camera mặc định thấy một đơn vị là một pixel ở độ sâu 0; một `Cam3` của `kit-camera.ts` di chuyển nó |
| `carouselPose(i, n, turn, r)` | Thẻ i trong n thẻ trên một vòng, thẻ phía trước nằm phẳng chính diện ở độ sâu 0 |
| `wallPose(col, row, cols, rows, gap, ry, rx)` | Một bức tường thẻ xoay như một khối |
| `tiltIn(since, from, to)` | Một thẻ đến từ một tư thế nghiêng, thấp hơn, xa hơn, được một lò xo mang tới từ trạng thái nghỉ |

Hình phản chiếu là một bản sao lật gương của mỗi thẻ, không phải một tấm gương được render: chính xác với các thẻ đứng trên sàn, rẻ, và không bao giờ hiển thị gì ngoài các thẻ. Mặt sau của thẻ là màu trơn (`back`, một màu tuyến tính); với `back: null`, một thẻ nhìn từ phía sau sẽ hiện mặt trước bị lật gương. Các mặt được nhân với `shade`, mặc định 0.86, giữ một thẻ trắng dưới ngưỡng bloom của preset tối: không có nó thì thẻ trắng phát sáng trên nền tối.

## 15. Chất liệu chuyển động

Các pass của kit (`src/scenes/parts/kit-post.ts`) mà một shot chạy trên các layer của riêng nó trước khi frame được hoàn thiện. Chúng chạy trên GPU trong ánh sáng tuyến tính (linear light) và giống nhau trên mọi trình duyệt.

| Pass | Làm gì | Chi phí |
|---|---|---|
| `Blur` | Một bản sao mềm của texture: Gaussian hai pass trên một target nhỏ hơn `down` lần. `render(renderer, texture, radius, premultiply)` trả về nó ở dạng premultiplied; composite với `premult: false`. Truyền `premultiply: true` cho một `Layer2D`, vốn có alpha dạng thẳng (straight) | Hai pass trên một phần tư frame khi `down` bằng 2 |
| `dofRadius(depth, focus, aperture, max)` | Bán kính blur của một layer phẳng ở một độ sâu, cho độ sâu trường ảnh trên layer 2D: mỗi layer mất nét đi qua `Blur` | Một `Blur` cho mỗi layer mất nét |
| `Liquid.goo(renderer, mask, out, style)` | Goo (chất nhầy): các hình vẽ trắng trên một layer mask tan vào nhau khi chúng đến gần nhau trong khoảng `radius`, và một giọt bị kéo ra thì giãn và đứt ra. Màu phẳng với điểm sáng ở phía hướng về nguồn sáng, vẽ lên `out` | Một blur và một pass toàn màn hình |
| `Liquid.glass(renderer, mask, behind, out, style)` | Kính lỏng: hình ảnh phía sau (thế giới của shot, render trước vào một target riêng) nhìn qua các hình của mask, bị bẻ cong ở viền (`refraction`), tách màu ở đó (`chroma`), mờ đục (`frost`), với một đường sáng nơi viền gặp ánh sáng (`rim`) và một bóng mềm bên ngoài. Với `goo` trên 0 thì các hình kính cũng tan vào nhau: một giọt kính giãn ra thành thanh công cụ. Nó ghi toàn bộ `out`, và target đó không được là `behind` | Một blur và một pass toàn màn hình, thêm một blur thứ hai khi mờ đục |
| `Difference.render(renderer, layer, base, out)` | Một layer blend kiểu difference lên một hình | Một pass toàn màn hình |

Mask của goo và kính là bất kỳ hình vẽ nào: vòng tròn, hình chữ nhật bo góc, một từ, các icon của thanh công cụ. Trường mà các hình được đọc ra là mask đã blur, chính là phương pháp blur-và-ngưỡng của web, làm trên GPU. Chữ bằng kính là một từ vẽ trên mask.

Khi bộ kit được xây, các ảnh tĩnh cho thấy kính trông như kính khi thứ phía sau có chi tiết gần viền (chữ, sọc); trên một màu phẳng thì không thấy được sự khúc xạ. Đường viền sáng gánh phần lớn hiệu ứng.

## 16. Trong route HyperFrames

Skill animation của nó bao quát cùng phạm vi dưới dạng các quy tắc (rule), nhóm như sau:

| Nhóm | Rule |
|---|---|
| Chữ | `hacker-flip-3d`, `vertical-spring-ticker`, `counting-dynamic-scale`, `kinetic-beat-slam`, `gradient-text-sweep`, `chromatic-glitch`, và các rule khác |
| Dữ liệu | `stat-bars-and-fills`, `chart-scrub-readout` |
| Bố cục | `center-outward-expansion`, `depth-scatter-assemble`, `orbit-3d-entry`, và các rule khác |
| Vẽ | `svg-path-draw`, `svg-icon-enrichment`, các mẫu đánh dấu (highlight, circle, burst, scribble) |
| Không khí (ambient) | `sine-wave-loop`, `ambient-glow-bloom` |
| Giao diện | `cursor-click-ripple`, `cursor-drag`, `press-release-spring`, `control-target-sync` |
| Xuất hiện | `spring-pop-entrance`, `waterfall-entry`, `particle-burst` |

Hai giới hạn nêu ở đó ảnh hưởng tới việc chọn route: các hạt vẽ bằng phần tử trang bị giới hạn khoảng bốn mươi, và các hiệu ứng cần các frame trước đó không được khuyến khích.

## 17. Những gì tốn kém

| Tốn kém | Vì sao | Nên làm gì |
|---|---|---|
| Vẽ lại chữ lớn hoặc canvas lớn mỗi frame | Toàn bộ layer bị upload mỗi lần | Vẽ một lần những gì không đổi, và chỉ phần chuyển động mỗi frame |
| Định dạng số mỗi frame | Định dạng theo locale thì chậm | Một hàm định dạng đơn giản |
| Dựng hình chữ ở lần dùng đầu tiên | Một cú khựng giữa shot | Dựng chúng khi shot tải lên |
| Một shader toàn màn hình với nhiều octave noise | Mọi pixel đều trả giá | Nửa độ phân giải cho các trường mềm |
| Ray marching | Mọi pixel, nhiều bước | Chỉ dành cho một shot |
| Khúc xạ, blur theo độ sâu | Thêm pass | Chỉ dành cho shot chủ đạo (hero) |
| Một layer vẽ thứ hai cỡ bằng frame | Thêm một lần upload | Nửa độ phân giải cho glow |
| Hàng trăm làn mềm (lửa, khói, vụ nổ) | Mỗi làn là một radial gradient tô trên canvas | Ít làn hơn, lớn hơn, có lõi chắc; một layer cho tất cả thứ nóng |
| Vệt nhòe trên nhiều chữ cùng lúc | Một lần vẽ cho mỗi bản sao | Chỉ chữ chuyển động nhanh mới có vệt nhòe; một chữ đứng yên tốn một lần vẽ |
| Vỡ vụn | Hình được vẽ một lần cho mỗi mảnh, qua một clip | Vài chục mảnh; hình vẽ một lần trên canvas riêng và truyền vào làm `source` |
| Thẻ trong three.js | Một lần render riêng, có anti-alias, cộng một lần composite | Một stage mỗi shot, thẻ vẽ một lần khi tải |

Mục tiêu là một frame vẽ trong khoảng tám mili giây, để sáu mươi frame một giây chạy được trên laptop. Hãy đo, và biết con số bao gồm những gì: một phép đo thực hiện qua công cụ capture có bao gồm việc đọc pixel về, thứ mà studio không làm. Chưa phần nào của kit ở các mục 7, 8, 12, 14 và 15 được đo thời gian frame.

## 18. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Một shot rối mà chẳng nói gì | Hiệu ứng không có việc | Một sự kiện mỗi beat; cắt phần còn lại |
| Một chữ số hiện hai giá trị cùng lúc | Một giá trị nhảy bậc lấy từ khoảnh khắc, khi lấy mẫu (sampling) | Lấy nó từ thời điểm của frame |
| Glow ở chỗ nhiều đường cắt nhau, trên những thứ không nên phát sáng | Ánh sáng cộng thêm bị cộng dồn vượt ngưỡng | Vẽ các đường như vậy với blend maximum; giữ alpha trong phạm vi một |
| Một phần hình bị thiếu ở frame đầy nhất | Batch quá nhỏ | Định cỡ cho frame nặng nhất; kiểm tra frame đó |
| Một shot khựng một lần, ở đầu | Thứ gì đó được dựng ở lần dùng đầu | Dựng khi tải |
| Hình khác nhau giữa hai lần chạy | Một số ngẫu nhiên không có seed, hoặc đồng hồ hệ thống | Seed mọi thứ |
| Những thứ bên trong một chiếc kính biến mất | Thứ tự vẽ của vật trong suốt và vật đặc | Đánh dấu phần bên trong cũng là trong suốt, và sắp xếp thứ tự |
| Các lớp thêm vào mỗi beat bị hiểu là "thêm thắt" trong khi ý là "các bước làm ra" | Hình ảnh của việc thêm vào | Thể hiện các lựa chọn trên một bản kế hoạch; làm ra thứ đó trong một lượt ở cuối |
| Một yêu cầu tỏa ra nhiều bên nhận trong khi ý là "tạo ra một thứ" | Hình ảnh của thông báo | Một vào, một ra |
| Một shot không hiện gì trên trình duyệt của chủ sở hữu | Một tính năng canvas mà trình duyệt đó không có | Tránh thuộc tính `filter` của canvas; đọc lỗi của trình duyệt |
| Một thứ nhanh trông như trình chiếu slide | Không có vệt nhòe | Vẽ vệt (`withMotion`) |
| Một vệt nhòe trông như một chồng bản sao | Quá ít bản sao, quá xa nhau | Một bản sao mỗi vài pixel; `withMotion` làm điều này qua `spacing` |
| Chữ viền rỗng có các đường cắt ngang | Contour của font chồng nhau bên trong một chữ cái | `setWord` với `outline`, cắt bỏ phần bên trong |
| Lửa trông như quả trứng phát sáng, khói như sương mù | Các làn lớn chỉ có mép mềm | Lưỡi lửa nhỏ giãn dài cho lửa; lõi chắc và một mặt sáng cho khói |
| Khói của vụ nổ biến mất hoặc làm nền sáng lên | Nó được vẽ trên layer cộng thêm | Khói trên một layer composite bình thường (`explosion` nhận hai bề mặt) |
| Thẻ trắng trong không gian phát sáng | Màu trắng nằm trên ngưỡng bloom của preset tối | Giữ `shade` của `CardStage` khoảng 0.86 |
| Một thẻ nhìn từ phía sau hiện chữ bị lật gương | Mặt sau của nó hiện mặt trước | Một màu `back` (mặc định) |
| Một layer bị blur có viền tối | Alpha thẳng bị blur nguyên như vậy | `Blur` với `premultiply: true`, composite với `premult: false` |
| Kính không hiện gì hoặc hiện một khung đen | `behind` và `out` là cùng một target, hoặc thứ phía sau không có chi tiết | Render thế giới vào target riêng trước; đặt chi tiết gần viền |
| Tấm nền của ticker mờ ở hai đầu | Lớp fade đã xóa nó | Truyền tấm nền vào `ticker`, hàm này đặt nó phía sau chữ sau đó |
| Một chùm sáng hiện bậc thang | Nhiều layer mờ ở 8-bit | `lightBeam`, một layer với conic gradient |
