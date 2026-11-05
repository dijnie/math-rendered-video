# Nhân vật và câu chuyện

Cách làm một bộ phim trong đó có ai đó làm một việc gì đó: thiết kế một nhân vật mà code vẽ được, rig (dựng khung chuyển động) nó thành một hàm theo thời gian, tạo dáng và diễn xuất nó theo nhạc, cho nó đi bộ, đặt nhiều nhân vật trong cùng một shot, giữ mỗi nhân vật nhất quán qua các shot và các builder, và kể một câu chuyện dài từ 20 giây đến 4 phút mà không cần lời. Chương kết thúc bằng các lỗi cần tìm trong still (khung hình tĩnh).

Nạp chương này khi: một yêu cầu nhắc tới một nhân vật, một mascot, một người hùng, hai đấu sĩ, người que, một con vật, hoặc "một phim ngắn", "một câu chuyện", "một trailer"; khi viết storyboard cho một bộ phim có một hình nhân diễn xuất; khi viết brief cho một builder có shot chứa nhân vật; hoặc khi review những shot như vậy.

Chưa có gì trong chương này được thử trên một bộ phim thật. Hai phim tham chiếu chỉ dùng hình nhân như đạo cụ. Chương được viết từ phương pháp, từ bộ rig của starter, và từ một tập prompt yêu cầu nhân vật và câu chuyện. Rig đã được xem qua still của một hình nhân thử gồm mười phần: đường viền, thứ tự vẽ, bàn chân được `reach` đặt xuống đất khi ngồi xổm và khi đi, một cái vẫy tay có spring, và một cú nhảy có squash and stretch (nén và giãn). Hãy đọc phần còn lại như một kế hoạch sẽ được sửa bởi bộ phim nhân vật thật đầu tiên.

## 1. Yêu cầu nói gì, và thực sự cần gì

| Yêu cầu nói | Cần gì từ chương này | Coi chừng |
|---|---|---|
| "Làm một phim ngắn 90 giây về một con bug không muốn bị sửa", "tự nghĩ ra câu chuyện" | Một khung truyện (mục 10), một hoặc hai nhân vật, một cast file, diễn xuất | Câu chuyện chính là tác phẩm. Viết nó và được duyệt trước khi vẽ bất kỳ nhân vật nào |
| "Một phim ngắn câm, nơi âm thanh kể một nửa câu chuyện" | Mục 10, và âm thanh viết theo hình | Âm thanh được lên kế hoạch trong storyboard, theo từng shot, không thêm vào lúc cuối |
| "Dùng con gấu đính kèm làm nhân vật chính; giữ cho nhận ra được" | Một cast file vẽ từ tham chiếu của chủ sở hữu, turnaround và biểu cảm được duyệt trước | Nhân vật của chủ sở hữu không được thiết kế lại. Các dấu hiệu của nó (tai, vòng mắt, dấu trên ngực) là checklist của mọi still |
| "Một trận đấu giữa A và B, có người thắng rõ ràng" | Hai nhân vật không thể nhầm lẫn, dàn dựng trên một đường thẳng, đòn đánh trúng beat | Hai nhân vật cùng một khuôn mặt. Một trận đấu chỉ toàn ánh chớp |
| "Người que trong một trận thủy chiến" | Người que trên rig: ít phần, nét đậm, dáng hành động | Người que vẫn cần một silhouette (bóng hình) cho mỗi dáng |
| "Một samurai thực hiện một chuỗi dáng ấn tượng tại chỗ" | Một thư viện dáng, các hold (giữ dáng), anticipation (lấy đà), hiệu ứng trên các đòn chém | Các dáng xuyên qua nhau mà không có hold sẽ bị đọc như nhiễu |
| "Một chú heo gửi thư tình; dùng asset heo trên branch của tôi" | Bản vẽ của chủ sở hữu được cắt thành các phần và rig | Các phần asset phải được cắt tại khớp và có chồng lấn, nếu không khớp sẽ hở khi xoay |
| "Trailer kiểu anime", "hoạt hình thập niên 90", "chất lượng ngang Pixar" bằng three.js | Một look (`art-styles.md`), có thể là nhân vật 3D (mục 8) | "Ngang Pixar" là lời hứa mà code với các phần cứng không giữ được. Nói rõ điều đó trong brief, và đề xuất look đồ chơi hoặc đất sét mà code làm tốt |
| "Một music video dẫn dắt bằng câu chuyện với một cô gái và một chàng trai, một character sheet, vũ công phụ họa" | Một dàn nhân vật, một character sheet, nhảy theo beat | Lip-sync theo giọng hát: xem mục 7 |
| "Một game chơi được có nhân vật" | Không phải phim. Xem `route-selection.md` | |

## 2. Thiết kế một nhân vật mà code vẽ được

Một nhân vật trong phương pháp này là một số ít hình khối xoay quanh các pivot (điểm xoay). Nó được code vẽ lại ở mọi frame, nên phải đủ đơn giản để được vẽ giống hệt nhau hàng nghìn lần và đủ mạnh để đọc được trong một phần ba giây trên điện thoại.

| Bước | Quy tắc | Vì sao |
|---|---|---|
| Silhouette trước tiên | Tô nhân vật màu đen trên nền trắng. Nó vẫn phải nói được nó là ai và đang làm gì | Silhouette là thứ được đọc trong nháy mắt, khi chuyển động, ở kích thước nhỏ |
| Ít hình khối | Năm đến mười hai phần: thân, đầu, hai tay, hai chân, và một hai thứ chỉ nhân vật này có (tai, mũ, đuôi, chỏm tóc) | Mỗi phần là một pivot phải key. Càng nhiều phần càng nhiều việc trong mọi shot, cho mọi builder |
| Một thứ chỉ nhân vật này có | Một hình mà mắt tìm thấy ở mọi kích thước: tai tròn có lòng xám, một chiếc mũ cong, một cái ăng-ten duy nhất | Nó phân biệt các nhân vật và vẫn còn đó trong một khung hình nhỏ |
| Tỉ lệ cho điện thoại | Đầu lớn (một phần ba đến một nửa chiều cao cho nhân vật dễ thương), mắt to, tay chân ngắn | Khuôn mặt chỉ đọc được khi đủ lớn. Một cái đầu tỉ lệ thật trên điện thoại chỉ là một chấm |
| Một hệ thống khuôn mặt | Mắt, lông mày và miệng là các channel (kênh) của dáng (`blink`, `look`, `brow`, `mouth`), được vẽ bởi một hàm cho mỗi nhân vật | Khi đó mọi builder có cùng biểu cảm từ cùng các con số |
| Độ dày nét | Một độ dày đường viền cho bên ngoài, một độ dày mảnh hơn cho bên trong, giống nhau ở mọi shot cùng kích thước | Độ dày nét thay đổi giữa các shot là dấu hiệu đầu tiên của một nhân vật bị vẽ lại |
| Màu sắc | Hai hoặc ba màu phẳng cho mỗi nhân vật, cộng một tông bóng cho mỗi màu. Mỗi nhân vật sở hữu một hue (sắc màu) trong các hue chính của palette | Người xem phân biệt nhân vật bằng màu trước hình dạng |
| Một turnaround | Mặt trước, ba phần tư, mặt bên và mặt sau, vẽ từ cùng các phần | Các shot sẽ cần nhiều góc nhìn. Quyết định phim cần những góc nào; nhiều phim chỉ cần mặt bên và ba phần tư |
| Một expression sheet (bảng biểu cảm) | Sáu đến tám khuôn mặt câu chuyện cần: bình thường, vui, buồn, giận, sợ, ngạc nhiên, và biểu cảm mà câu chuyện xoay quanh | Khuôn mặt được thiết kế một lần, không phải chế ra trong một shot |
| Thay đổi theo cuộc đời | Khi nhân vật già đi trong phim, tỉ lệ của nó là hàm của một channel, `age`: đầu so với thân, độ dài tay chân, chiều cao, một chiếc mũ hay bộ râu xuất hiện. Cast file ghi các giai đoạn thành key của channel đó | Người xem phải thấy cùng một sinh thể ở mọi tuổi. Những gì giữ nguyên (thứ chỉ nhân vật này có, màu sắc) mang theo danh tính |

Kiểm tra một thiết kế trước khi rig: chụp một still với turnaround và expression sheet đặt cạnh nhau, ở kích thước nhân vật sẽ có trong một medium shot (cỡ cảnh trung) của khung hình phim. Nếu không phân biệt được các khuôn mặt ở kích thước đó, làm khuôn mặt to hơn hoặc biểu cảm đậm hơn.

Độ dày nét và tỉ lệ: rig vẽ một phần trong không gian riêng của nó và context scale nó, nên độ rộng nét scale theo nhân vật. Điều đó đúng khi nhân vật được vẽ ở vài cỡ shot của phim. Với một nhân vật zoom rất xa trong một shot, truyền tỉ lệ vào các hàm vẽ và chia độ rộng nét cho nó, nếu không đường viền sẽ phình ra ở cận cảnh và biến mất ở toàn cảnh.

Tay chân kiểu rubber-hose (ống cao su), như hoạt hình thập niên 1930, không có khuỷu hay đầu gối: mỗi chi là một đường cong từ vai đến bàn tay. Dựng nó bằng `reach` để lấy vị trí khớp và vẽ một đường cong trơn duy nhất qua ba điểm, cùng độ rộng suốt chiều dài và một chiếc găng trắng ở cuối. Lớp hoàn thiện mang dấu thời kỳ (film grain, khung hình lắc một hai pixel, nhấp nháy, bụi) thuộc về chuỗi post: xem `effects.md`.

## 3. Cast file, dùng chung cho mọi builder

Một nhân vật được thiết kế một lần, bởi lead, và sống trong một file mà mọi builder import: cast file, mỗi nhân vật một file hoặc một file cho cả dàn, trong thư mục kit (với con gấu, `parts/cast-bear.ts` dưới `src/scenes/`).

| Cast file chứa | Builder được phép |
|---|---|
| Các phần, pivot, tỉ lệ, màu sắc và độ dày nét của chúng | Dùng chúng. Không bao giờ chép chúng vào một shot |
| Khuôn mặt: cách vẽ mắt, lông mày và miệng từ các channel | Đặt giá trị các channel |
| Các dáng có tên: `stand`, `crouch`, `reach`, `cheer`, `slump`, ... | Key chúng, trộn chúng, thêm layer |
| Các chu kỳ có tên: walk, run, idle, mỗi cái có chu kỳ tính bằng beat | Phát chúng bằng `loopAt` |
| Kích thước nhân vật ở mỗi cỡ shot của phim | Đặt nhân vật ở các kích thước đó |
| Seed của nó, cho nháy mắt và sự sống lúc idle | Không gì cả: seed tạo nên chính nhân vật |

Lead sở hữu file. Một builder cần một dáng hay một biểu cảm mà sheet chưa có thì hỏi lead, người sẽ thêm nó vào sheet để builder kế tiếp cũng có. Builder không bao giờ sửa cast file, và không bao giờ tự tay vẽ nhân vật trong một shot, kể cả "chỉ lần này thôi ở hậu cảnh". Quy tắc này giống với phần còn lại của kit (`orchestration.md`, quyền sở hữu file), và đó là thứ duy nhất giữ một nhân vật nhất quán qua mười builder.

Một shot character sheet đáng làm trước shot thật đầu tiên: một still với hàng dàn nhân vật ở cùng một tỉ lệ, mỗi nhân vật kèm turnaround và vài biểu cảm. Chủ sở hữu duyệt các nhân vật trên đó, và mọi still sau này được so với nó.

## 4. Rig: nhân vật như một hàm theo thời gian

Kit của starter có một rig 2D nhỏ: `src/scenes/parts/kit-rig.ts`. Nó theo mô hình của camera (`camera.md`, mục 1): một dáng là một bản ghi nhỏ, các key nói khi nào chuyển sang dáng nào và chuyển ra sao, và mọi thứ là một hàm thuần theo thời gian.

### Các phần và dáng

| Tên | Là gì |
|---|---|
| `Part` | Một mảnh: `id`, `parent`, pivot `at` trong không gian của parent, thứ tự vẽ `z`, một `lag` tùy chọn tính bằng beat với `tip` và `drag` cho follow-through, và một `draw(c, s)` vẽ nó trong không gian riêng với pivot ở gốc tọa độ |
| `PartPose` | Một phần nằm thế nào: góc xoay `r` quanh pivot, độ lệch `x`, `y`, tỉ lệ `sx`, `sy`. Trường bị bỏ trống là ở trạng thái nghỉ |
| `Pose` | `parts` theo id, và `ch`, các channel tự do dạng số: `blink`, `look`, `mouth`, `brow`, một công tắc trang phục |
| `Rig` | Tạo từ danh sách các phần, parent đứng trước. `pose(t, src)` tính dáng từ key hoặc từ một hàm theo thời gian (một bước đi tính tay), `draw(c, pose, place, t)` vẽ nó lên một context 2D, `point(pose, id, x, y)` cho biết một điểm của một phần nằm ở đâu, `plant(pose, soles, groundY)` cho biết cần dịch nhân vật bao xa để đế chân thấp nhất chạm đất |
| `Place` | Nhân vật đứng ở đâu trên layer, tỉ lệ của nó, và `flip` để quay mặt sang hướng kia |

Quy ước: trục y hướng xuống, góc tính bằng radian, góc xoay dương là theo chiều kim đồng hồ trên màn hình, và một chi ở trạng thái nghỉ thì buông thẳng xuống từ pivot. Transform riêng của context được giữ lại, nên một nhân vật vẽ sau `applyCam` sẽ đứng trong thế giới của camera.

### Key và in-between (khung trung gian)

| Tên | Làm gì |
|---|---|
| `rigAt(t, keys)` | Dáng tại `t` từ các key, giống `camAt`. Mỗi key là một chuyển động từ vị trí hiện tại của cơ thể sang dáng của key, bắt đầu ở beat `at` và kéo dài `over` beat với `ease` của nó. `over: 0` là chuyển tức thì. Một phần hay channel mà key bỏ qua thì được giữ nguyên, nên key chỉ cần ghi những gì thay đổi |
| `springEase(over, freq, damping)` | Một ease vượt quá rồi lắng lại: một cơ thể có trọng lượng đang đến nơi. `over` phải là `over` của chính key đó |
| `mixPose(a, b, k)` | Nằm giữa hai dáng; `k` có thể vượt quá 1 |
| `addPose(base, ...layers)` | Các layer chồng lên: góc xoay, độ lệch và channel được cộng, tỉ lệ được nhân. Thở, lắc lư, một ánh nhìn, một cái nháy mắt |
| `loopAt(t, period, keys)` | Một chu kỳ: các key bao một vòng và được phát lặp đi lặp lại. Dáng cuối phải bằng dáng đầu |

Một hold không phải là một key: nó là khoảng trống trước key kế tiếp. Viết dáng, rồi để yên nó một hai beat.

Các key của một shot được viết bằng beat của scene clock (`sceneClock` trong `kit-frame.ts`), để các dáng rơi đúng nhạc. Một dáng là dữ liệu: viết các key của một màn diễn thành một bảng gần đầu shot, không phải code rải khắp `render()`.

```ts
const ACT: PoseKey[] = [
  { at: 0,    pose: BEAR.stand },
  { at: 3.5,  pose: { parts: { armR: { r: 0.4 } } }, over: 0.5, ease: ease.inOutQuad },           // lấy đà
  { at: 4,    pose: { parts: { armR: { r: -2.6 } }, ch: { mouth: 1 } }, over: 1, ease: springEase(1) }, // cái vẫy tay
  { at: 7.25, pose: BEAR.crouch, over: 0.75 },
  { at: 8,    pose: BEAR.leap, over: 0.5, ease: ease.outQuad },                                      // trên drop
];
const pose = addPose(BEAR_RIG.pose(k.beats, ACT), { ch: { blink: blink(f.t, BEAR_SEED) } });
BEAR_RIG.draw(c, pose, { x: 540, y: 1300, scale: 3 }, k.beats);
```

### Sự sống chồng lên các key

| Nguyên tắc | Trong kit | Cách dùng |
|---|---|---|
| Overlap và follow-through (chồng lấn và theo đà) | `lag`, `tip` và `drag` trên một phần | Tóc, tai, đuôi, khăn quàng, áo choàng: phần đó lấy dáng được key của chính nó từ `lag` beat trước, nên nó đến sau cơ thể và tiếp tục chuyển động khi cơ thể dừng (0.1 đến 0.3 beat). Cho nó một `tip`, điểm ở đầu tự do, thì nó còn đung đưa ngược lại hướng pivot đã di chuyển trong khoảng đó, nên một chỏm tóc vẫn kéo theo sau khi đầu quay dù bản thân chỏm tóc không có key; `drag` đặt mức độ. Một chuỗi các phần, mỗi phần trễ hơn một chút, làm một cái đuôi vẫy |
| Squash and stretch (nén và giãn) | `squash(amount)` | Cơ thể nén lại trước khi nhảy và khi tiếp đất, giãn ra khi bay. Giữ nguyên diện tích: helper làm việc đó. Vật cứng (mũ bảo hiểm, thanh kiếm) không nén |
| Chuyển động thứ cấp | `lag`, `wander`, hoặc một mô phỏng | Một thứ nhỏ đáp lại thứ lớn: cái bụng sau khi tiếp đất, chiếc mũ sau khi xoay người. Vải và tóc dài phải va chạm thì được mô phỏng một lần trong `init()` và tra theo thời gian (`effects.md`, mục 2) |
| Sự sống lúc idle | `wander(t, amount, rate, seed)` | Trôi dạt có seed cho một cái lắc lư, một cái đầu nghiêng, đôi mắt nhìn quanh. Một nhân vật đứng yên tuyệt đối giữa các key trông như bị tắt máy |
| Thở | một tỉ lệ trên thân theo beat | Mỗi bar một hơi thở, 1 đến 2 phần trăm. Dưới mọi hold |
| Nháy mắt | `blink(t, seed, every, dur)` | Truyền giây (`f.t`) để mắt nháy lệch beat, như mắt thật. Mỗi nhân vật một seed riêng. Nháy mắt khi đổi ý nghĩ: một key của màn diễn có thể thêm một cái nháy mắt riêng |
| Với tới và đặt chân | `reach(ax, ay, tx, ty, l1, l2, bend)` | Hai xương tới một điểm: chân tới bàn chân đặt trên mặt đất, bàn tay tới tay nắm cửa. Nó trả về góc xoay trên và dưới. Đầu gối của nhân vật quay mặt sang phải dùng `bend` -1 |
| Bám đất | `Rig.plant` | Với chân được key bằng góc xoay thay vì bằng `reach`: dịch nhân vật để đế chân thấp nhất chạm đất |

Chân nhân vật chỉ chạm đất nếu code nói vậy. Key phần hông, và để `reach` đặt hai chân giữa hông và bàn chân vẫn ở chỗ đã đặt. Điều tương tự áp dụng cho bàn tay trên lan can, móng vuốt trên chiếc bánh trung thu, hai bàn tay trên một thanh kiếm.

### Một phần được phép vẽ gì

`draw` của một phần nhận `s.pose` (dáng của chính nó), `s.ch` (các channel) và `s.t` (thời gian). Khuôn mặt đọc các channel; miệng có thể cong theo `s.ch.mouth`; trang phục có thể đổi theo một channel. Mọi thứ một phần vẽ phải đến từ những giá trị này và từ hằng số của cast file, không bao giờ từ đồng hồ hệ thống hay từ một nguồn ngẫu nhiên không có seed.

## 5. Diễn xuất

### Một dáng cho mỗi beat của câu chuyện

Diễn xuất là một chuỗi dáng, mỗi dáng là một lời tuyên bố đọc được, với chuyển động giữa chúng. Tìm các dáng trước, rồi mới đến timing.

| Nhân vật cảm thấy | Cơ thể | Đầu và khuôn mặt |
|---|---|---|
| Vui | Hướng lên và mở: tay giơ lên hoặc dang ra, trọng lượng trên mũi chân, một cú nhún nhảy | Đầu ngẩng, mắt mở to hoặc nheo lại khi cười, miệng mở |
| Buồn | Hướng xuống và khép: vai đổ về trước, tay buông thõng, trọng tâm thấp | Đầu cúi, mi khép hờ, lông mày nhướng ở giữa, miệng trễ xuống |
| Giận | Hướng tới: chồm về trước, nắm tay, chân dạng ra | Cằm cúi, lông mày hạ và chau vào, miệng vuông |
| Sợ | Lùi lại và thu nhỏ: ngả ra xa, tay khép vào, một chân lùi | Mắt mở to với con ngươi nhỏ, lông mày nhướng, miệng mở và căng |
| Ngạc nhiên | Một cú take: nén xuống, rồi giãn lên, và một hold | Mắt mở to hết mức thiết kế cho phép, lông mày cao, miệng tròn |
| Tự hào | Ưỡn ngực, hếch cằm, trọng tâm lùi ra sau | Mắt khép hờ, một nụ cười nhỏ |
| Khao khát | Nghiêng về phía vật đó, một bàn tay với tới | Mắt nhìn vật đó, không bao giờ nhìn camera |
| Quyết định | Đứng yên. Rồi một chuyển động nhỏ | Nhìn đi rồi nhìn lại; một cái nháy mắt khi đổi ý |

### Timing theo nhạc

| Nguyên tắc | Quy tắc |
|---|---|
| Dáng chính trên beat | Dáng nói lên điều cần nói rơi đúng một beat. Drop là dáng quan trọng nhất trong section |
| Anticipation (lấy đà) | Một chuyển động nhỏ theo hướng ngược lại, nửa beat trước chuyển động chính. Hành động càng lớn, lấy đà càng lớn |
| Hold | Sau một dáng quan trọng, giữ nó một hai beat, chỉ có sự sống idle chuyển động. Người xem cần hold để đọc được dáng |
| Mỗi lúc một hành động | Hành động chính dẫn đầu; các hành động khác chờ hoặc theo sau. Một nhân vật có mọi phần chuyển động cùng lúc bị đọc như nhiễu |
| Đường cung | Bàn tay, đầu và vật bị ném di chuyển theo đường cong. Một phép xoay quanh pivot tự cho ra đường cung; một phép dịch bằng `x`, `y` thì không |
| Nhanh hơn đời thật | Chuyển động tốn ít frame hơn đời thật, hold thì nhiều hơn. Trên một bản nhạc nhanh, chuyển động nửa beat đã là chậm |
| Phản ứng sau hành động | Người bị đánh phản ứng một phần nhỏ của beat sau cú đánh, trên off-beat (phách lệch) |

### Đọc khuôn mặt theo kích thước khung hình

| Khuôn mặt trong khung hình | Thứ gì diễn được |
|---|---|
| Đầu bằng một phần mười cạnh ngắn của khung hình hoặc nhỏ hơn | Chỉ cơ thể. Chi tiết khuôn mặt không thấy; nháy mắt không thấy |
| Một phần năm | Mắt, hướng nhìn, một cái miệng lớn |
| Một phần ba trở lên (một close shot) | Lông mày, mí mắt, một nụ cười nhỏ, một giọt nước mắt |

Một beat câu chuyện nằm trên khuôn mặt cần một close shot (cận cảnh). Lên kế hoạch cho nó trong cột camera của storyboard. Một khuôn mặt phải được đọc trong một wide shot (toàn cảnh) thì sẽ không được đọc.

Nhân vật nhìn đâu, người xem nhìn đó. Mọi nhân vật không phải trung tâm chú ý đều nhìn vào nhân vật là trung tâm, hoặc vào thứ quan trọng. Đôi mắt nhắm vào hư không làm nhân vật trông như đã chết.

## 6. Chu kỳ

| Chu kỳ | Các dáng | Trên grid | Lỗi |
|---|---|---|---|
| Đi bộ | Contact (chạm), down (hạ), passing (bước qua), up (nâng), cho mỗi chân: tám dáng một sải chân | Một bước mỗi beat ở khoảng 100 đến 130 beat mỗi phút; trên bản nhạc nhanh hơn, một bước mỗi hai beat | Chân trượt: mặt đất (hoặc camera) phải chuyển động đúng bằng tốc độ bàn chân đang đặt lùi về sau |
| Chạy | Như đi bộ, với một khoảnh khắc trên không và người đổ về trước | Một bước mỗi nửa beat hoặc mỗi beat | Không có khoảnh khắc trên không thì bị đọc là đi nhanh |
| Rón rén | Gối nâng cao, hold dài ở mỗi bước | Bước trên off-beat | |
| Idle | Một hơi thở, một lần dồn trọng lượng, một ánh nhìn | Mỗi bar một hơi thở; dồn trọng lượng mỗi hai hoặc bốn bar | Một vòng lặp lộ rõ vì quá ngắn |
| Nhảy múa | Các dáng của biên đạo | Dáng trên beat, chuyển động giữa chúng | Mọi vũ công đồng loạt không chút lệch bị đọc là sao chép |

Đặt chu kỳ của một cycle là một số nguyên beat, để nó rơi đúng grid dù bắt đầu ở đâu. Một bước đi ngang khung hình dịch vị trí nhân vật bằng tốc độ mặt đất nhân thời gian; một bước đi tại chỗ dịch mặt đất hoặc camera đúng lượng đó. Ghi tốc độ mặt đất trong cast file cùng với cycle, bằng độ dài sải chân chia cho thời gian một bàn chân được đặt xuống.

Trên không, chân buông về phía mặt đất; trên mặt đất, bàn chân đang đặt không di chuyển so với mặt đất. Cả hai có sẵn miễn phí khi chân được đặt vào chỗ bằng `reach`.

## 7. Nhiều nhân vật trong một shot

| Quy tắc | Vì sao |
|---|---|
| Mỗi nhân vật một seed riêng | Nếu không chúng nháy mắt cùng lúc và lắc lư cùng lúc, bị đọc như một cỗ máy |
| Độ lệch giữa chúng | Hai nhân vật làm cùng một việc thì làm lệch nhau một phần nhỏ của beat, trừ khi "cùng nhau" chính là ý đồ |
| Một nhân vật là trung tâm chú ý | Những người khác nhìn vào họ, giữ dáng, hoặc phản ứng. Hai nhân vật diễn cùng lúc làm chia mắt người xem |
| Giữ hướng màn hình | Nếu A đứng bên trái B trong một shot, A đứng bên trái B ở shot kế tiếp. Storyboard ghi mỗi nhân vật đứng ở đâu và quay mặt hướng nào, theo từng section, và việc vượt qua đường đó được thể hiện trên màn hình |
| Tiếp xúc được tính toán | Một bàn tay trên vai người khác lấy điểm từ `point` của rig kia, rồi dùng `reach` |
| Thứ tự theo chiều sâu | Nhân vật được vẽ từ sau ra trước; một nhân vật băng qua phía trước nhân vật khác đổi thứ tự tại một thời điểm ghi trong các key |
| Đám đông được tạo ra, không phải vẽ ra | Vũ công phụ họa và đám đông đến từ cast file với một bộ sinh có seed tạo các biến thể nhỏ: kích thước, một màu từ danh sách ngắn, độ lệch pha. Không bao giờ là các bản sao chuyển động đồng loạt |

Một trận đấu là một cuộc đối thoại: hành động, phản ứng, một hold, lặp lại. Đặt mỗi đòn trên một beat và mỗi phản ứng trên nửa beat kế tiếp, dàn hai đấu sĩ trên một đường ngang khung hình, và cho các cú đánh điểm nhấn từ `effects.md` (impact frame, rung, chớp sáng) cùng một smear (vệt nhòe) do shot vẽ cho các chi chuyển động nhanh. Chọn người thắng trong storyboard và để mọi pha trao đổi trước đoạn kết hướng về nó.

### Lip-sync, nói thật

Starter không có lip-sync. Một cái miệng mở và đóng theo lời của một giọng nói là khả thi nhưng chưa được dựng. Những gì cần có:

| Cần | Từ đâu |
|---|---|
| Thời điểm của các âm trong lời nói (phoneme, âm vị), hoặc ít nhất là của các từ | Thời điểm từ có sẵn khi một file lời được nạp: `ctx.lyrics` (`src/engine/lyrics.ts`) chứa các từ với thời gian bắt đầu và kết thúc, và cả âm tiết khi dữ liệu có. Thời điểm phoneme cần một công cụ forced-alignment không thuộc starter |
| Một bộ nhỏ hình dạng miệng | Sáu đến chín cho mỗi nhân vật: đóng (m, b, p), mở (a), bè (e, i), tròn (o, u), răng chạm môi (f, v), và nghỉ, vẽ trong cast file thành các giá trị của channel `mouth` |
| Một ánh xạ và làm mượt | Mỗi âm sang một hình dạng, mỗi hình dạng giữ ít nhất hai frame, hình dạng đến sớm một frame, bỏ các hình dạng nhỏ |

Không có thời điểm phoneme, một cái miệng mở trên mỗi từ và đóng giữa các từ là tối đa có thể làm, và trên một close shot nó trông rẻ tiền. Ưu tiên câu chuyện không có thoại, một giọng nói trên một nhân vật không thấy miệng, hoặc lời hát hiển thị thành chữ (`type-and-captions.md`). Một track giọng nói và timing của nó là chủ đề của `references/sound-and-voice.md`.

## 8. Nhân vật 3D

Khi yêu cầu đòi three.js, một look đồ chơi hoặc đất sét, một nhân vật được nhìn từ mọi phía, hoặc một cú quay quanh người hùng.

| Phần | Làm thế nào, trong engine này |
|---|---|
| Vẽ ở đâu | Một scene three.js được render vào một target riêng của shot, `makeRT(W, H, { samples: 4 })`, xóa về alpha 0, rồi composite lên frame với `premult: false` (`engine-architecture.md`, mục 4) |
| Cơ thể | Các phần cứng từ primitive (hình cầu, capsule, hộp bo góc), mỗi phần trong một group `Object3D` có gốc tọa độ là pivot của nó. Các group là các phần của rig; một dáng đặt góc xoay của chúng. Key hoạt động như trong 2D: viết một hàm trộn cho bản ghi dáng của các phần 3D và dùng `poseAt` của `kit-camera.ts` với nó |
| Toon shading | `MeshToonMaterial` với một `gradientMap` ba hoặc bốn bậc: một `DataTexture` nhỏ với `NearestFilter` ở cả hai filter, để các bậc giữ sắc cạnh. Màu trong không gian ánh sáng tuyến tính từ `LIN` của palette |
| Ánh sáng | Một key light, một sky light (hemisphere light) và một rim light (đèn viền) mang hue của nhân vật từ phía sau. Rim là thứ tách một nhân vật tối khỏi một nền tối |
| Đường viền | Hai cách. Cách rẻ vẽ mỗi mesh lần thứ hai bằng mặt sau, đẩy ra theo pháp tuyến, bằng mực phẳng; độ rộng không đều và nó gãy ở các góc nhọn. Cách tốt hơn render pháp tuyến và độ sâu vào một target thứ hai và tìm cạnh trong một pass toàn màn hình: dày ở chỗ độ sâu nhảy vọt (silhouette), mảnh ở chỗ pháp tuyến đổi hướng (nếp gấp). Giữ phép thử độ sâu lỏng và dựa vào pháp tuyến, nếu không các bề mặt nghiêng sẽ đầy sọc mảnh. three.js cũng có sẵn một outline effect kiểu thứ nhất trong các add-on |
| Khuôn mặt | Mắt là hình cầu dẹt hoặc đĩa với con ngươi xoay để nhìn; mí là nửa hình cầu khép lại; miệng vẽ trên một `Layer2D` và dùng làm texture của một mặt phẳng nhỏ trước đầu. Các channel khuôn mặt của mục 2 điều khiển chúng |
| Bóng đổ | Một hình elip mềm trên mặt đất co lại và mờ đi khi nhân vật bay lên. Đó là thứ làm nhân vật đứng vững |
| Đồ chơi và đất sét | Một vật liệu physically based với độ nhám cao và không có kim loại; một ánh sáng ôm nhẹ quanh khối (một fill ấm từ dưới và sau giả ánh sáng xuyên qua đất sét); một bóng tiếp xúc tối mềm ở mọi chỗ hai phần hoặc một phần với mặt đất gặp nhau; một chút nhiễu rất nhỏ trên pháp tuyến cho dấu vân tay. Bo tròn mọi cạnh: không gì làm bằng đất sét lại sắc cạnh |
| Post | Look toon cần ít bloom. Giữ đường viền dưới ngưỡng bloom, nếu không nó sẽ phát sáng |

Skinned mesh, nơi một bề mặt uốn theo xương, khả thi trong three.js, nhưng một model skinned được làm bằng công cụ bên ngoài và đưa vào dưới dạng file. Điều đó nằm ngoài lộ trình chỉ-code và cần asset hoặc sự chấp thuận của chủ sở hữu. Các phần cứng với khớp tròn là look trung thực của lộ trình chỉ-code: một món đồ chơi, một hình nhân bằng đất sét, một con búp bê gỗ.

## 9. Giữ nhân vật nhất quán qua các shot

| Rủi ro | Cách phòng |
|---|---|
| Một builder vẽ lại nhân vật "đẹp hơn một chút" | Cast file là bản vẽ duy nhất. Builder brief nói rõ điều đó |
| Kích thước trôi dạt từ shot này sang shot khác | Cast file liệt kê chiều cao nhân vật ở mỗi cỡ shot. Cột camera của storyboard ghi cỡ shot |
| Màu sắc hoặc độ dày nét thay đổi | Cả hai nằm trong cast file. Một shot nhuộm màu nhân vật vì đổi ánh sáng thì ghi rõ trong storyboard |
| Quay mặt sai hướng sau một cú cắt | Hướng màn hình theo section trong storyboard |
| Chi tiết lúc có lúc không (dấu trên ngực, khăn quàng) | Checklist các dấu hiệu ở đầu cast file, đọc ở mỗi lần review |
| Phong thái thay đổi (nhanh ở shot này, chậm ở shot khác) | Cast file chứa timing riêng của nhân vật: nó di chuyển nhanh thế nào, hold bao lâu |

Khi review, đặt một still của mỗi shot cạnh still hàng dàn nhân vật. Xem chiều cao, dấu hiệu, màu sắc và độ dày nét trước mọi thứ khác.

## 10. Kể chuyện không lời

### Khung truyện theo độ dài

| Độ dài | Khung | Cấu trúc ví dụ |
|---|---|---|
| 15 đến 30 giây | Một gag (mẩu hài), hoặc một điều ước thành sự thật. Dẫn dắt, bẻ lái, phản ứng | Mong muốn trong hai giây đầu; một lần thử; bất ngờ trên drop; một phản ứng được giữ đến hết |
| 45 đến 90 giây | Mong muốn, các lần thử thất bại và tăng dần (ba lần), bước ngoặt, phần thưởng, một button | Mỗi lần thử là một phrase (câu nhạc); bước ngoặt trên drop lớn nhất; button ở bar cuối |
| 2 đến 4 phút | Một vòng cung nhỏ: nhân vật thay đổi ở cuối. Một nhân vật thứ hai hoặc một tuyến phụ, một callback | Các hồi theo các section của bản nhạc: dẫn dắt ở intro, rắc rối qua các verse, điểm thấp nhất ở break, bước ngoặt trên drop cuối, trạng thái bình thường mới ở outro |

Button là một beat nhỏ sau đoạn kết: tiếng vọng của gag, cái nhìn cuối của nhân vật vào camera, thứ đã mất bỗng xuất hiện. Đó là thứ người xem nhớ.

### Làm câu chuyện đọc được mà không cần lời

| Công cụ | Cách dùng |
|---|---|
| Cho thấy mong muốn ngay lập tức | Nhân vật nhìn vào vật đó, rồi với lấy nó. Trong ba giây đầu của một phim ngắn, shot đầu tiên của một phim dài hơn |
| Eyeline (hướng nhìn) và point of view | Một shot nhân vật đang nhìn, rồi một shot thứ họ thấy. Người xem hiểu bằng cách nối hai shot |
| Nhân quả trong một khung hình | Hành động và kết quả của nó trong cùng một shot, hoặc trong hai shot cắt trên hành động |
| Shot phản ứng | Khuôn mặt của nhân vật khác cho người xem biết nên cảm thấy thế nào về điều vừa xảy ra |
| Đồ vật thay lời | Một lá thư, một trái tim, một bức ảnh, một chiếc đồng hồ, một tấm biển trên cửa. Chọn đồ vật mà đời sống của người xem đã quen |
| Pictogram (biểu tượng hình) | Một bong bóng suy nghĩ có hình bên trong, một mũi tên, một icon trên đầu. Dùng tiết kiệm |
| Quy tắc ba lần | Lần đầu thiết lập, lần hai xác nhận, lần ba phá vỡ khuôn mẫu |
| Plant và callback (gieo và gọi lại) | Cho thấy một thứ từ sớm mà không có lý do rõ ràng (một chiếc mũ vỏ bưởi, một ngăn kéo bị kẹt); mang nó trở lại ở bước ngoặt, đã thay đổi. Callback là khoảnh khắc thỏa mãn nhất mà một phim ngắn có thể mang lại |
| Tương phản về tỉ lệ và màu sắc | Cái nhỏ đối với cái lớn, cái được chiếu sáng đối với bóng tối: người xem đọc được quyền lực và sự cô đơn mà không cần một lời |
| Hướng màn hình | Di chuyển sang phải được đọc là tiến lên; sang trái là quay lại hoặc về nhà. Giữ một hành trình đi theo một hướng |

### Âm thanh kể một nửa câu chuyện

Trong một bộ phim không lời, âm thanh mang những gì hình ảnh không thể: điều xảy ra ngoài khung hình, một vật nặng bao nhiêu, nhân vật cảm thấy gì trước khi khuôn mặt thể hiện. Lên kế hoạch theo từng shot trong storyboard, không phải lúc cuối.

| Âm thanh | Kể |
|---|---|
| Một hiệu ứng từ ngoài khung hình | Có gì đó sắp đến: tiếng gõ cửa, tiếng va chạm, một thiên thạch, một tiếng chuông |
| Im lặng trước khi lộ diện | "Nhìn đi." Hơi thở của `transitions.md` trong âm thanh |
| Một motif cho mỗi nhân vật | Đây là ai, kể cả khi không thấy. Nó đổi giọng hoặc nhạc cụ khi nhân vật thay đổi |
| Foley trên mọi tiếp xúc | Trọng lượng: một bước chân, một cú tiếp đất, một cái tát, tiếng giấy |
| Nhạc tắt đi | Điểm thấp nhất. Nhạc trở lại là bước ngoặt |

Trong một bộ phim cắt theo một bản nhạc hoàn chỉnh, nhạc mang cảm xúc còn hình ảnh mang cốt truyện; hiệu ứng vẫn có thể thêm lên trên ở chỗ chủ sở hữu muốn. Âm thanh viết bằng code, hiệu ứng và giọng nói là chủ đề của `references/sound-and-voice.md`.

### Trong storyboard

Trường `see` của mỗi shot ghi beat câu chuyện và cảm xúc, không chỉ hình ảnh: "Chú heo thấy hộp thư trống. Thất vọng: tai cụp xuống, một hold dài." Trường `move` đặt các dáng chính lên beat. Cột `camera` ghi cỡ shot mà diễn xuất cần (mục 5). Một phim kể chuyện được duyệt trên animatic như mọi phim khác, và đáng để đọc to câu chuyện cho chủ sở hữu nghe từng shot trước đó: nếu nó không hoạt động như một danh sách câu văn, nó sẽ không hoạt động như hình ảnh.

## 11. Lỗi cần tìm trong still

Xem các still chụp tại beat của các dáng chính, các cặp still cách nhau một beat cho các cycle, và still hàng dàn nhân vật đặt cạnh mỗi shot. Xem một still thu nhỏ bằng kích thước màn hình điện thoại để kiểm tra khuôn mặt.

| Lỗi | Biểu hiện trong still | Nguyên nhân | Cách sửa |
|---|---|---|---|
| Chân lơ lửng | Một khe hở giữa đế chân và mặt đất, hoặc không có bóng tiếp xúc | Hông được key nhưng chân không được đặt xuống đất | Đặt chân vào chỗ bằng `reach`, hoặc dịch nhân vật bằng `Rig.plant`; vẽ bóng tiếp xúc |
| Chân lún | Một bàn chân dưới đường mặt đất | Như trên | Như trên |
| Chân trượt | Trong hai still cách nhau một beat, bàn chân đang đặt đã di chuyển so với mặt đất | Tốc độ mặt đất và sải chân không khớp | Lấy tốc độ mặt đất từ cycle của cast file |
| Tay chân bị kéo dài | Cẳng tay ở still này dài hơn ở still khác | Bàn tay được dịch bằng `x`, `y` thay vì xoay các xương | Xoay các xương; dùng `reach` cho bàn tay phải với tới một điểm |
| Khớp bị hở | Một khe hở hoặc góc nhọn ở khuỷu tay hoặc đầu gối | Các phần được cắt không có chồng lấn tại pivot | Đầu tròn chồng lên pivot, hoặc vẽ khớp thành một hình tròn |
| Mọi người cùng một khuôn mặt | Hai nhân vật chỉ phân biệt được bằng màu | Dùng chung một bản vẽ khuôn mặt | Mỗi nhân vật có hình mắt, khoảng cách mắt, lông mày và miệng riêng trong cast file |
| Nhân vật thay đổi giữa các shot | Chiều cao, dấu hiệu, độ dày nét hoặc màu sắc khác với hàng dàn | Một builder tự vẽ, hoặc scale tùy ý | Chỉ vẽ từ cast file; kích thước lấy từ bảng của nó |
| Twinning (đối xứng sinh đôi) | Hai tay hoặc hai chân cùng một dáng, phản chiếu | Key được chép từ bên này sang bên kia | Lệch thời gian một bên, hoặc đổi dáng của nó |
| Silhouette không đọc được | Dáng tô đen không nói lên gì | Tay ở trước thân, dáng nhìn thẳng chính diện | Xoay nhân vật ba phần tư; đưa tay ra khỏi đường viền của thân |
| Mắt chết | Nhân vật nhìn vào hư không, hoặc nhìn camera vô cớ | Không có eyeline | Hướng channel `look` vào thứ quan trọng |
| Bị tắt máy | Không phần nào chuyển động giữa hai still của một hold | Không có sự sống idle | Thêm `wander`, hơi thở và nháy mắt dưới hold |
| Popping (giật cục) | Một dáng thay đổi hoàn toàn giữa hai frame | Một key không có `over` ở chỗ không định thế | Cho key một chuyển động, hoặc đặt cú chuyển tức thì vào một cú cắt |
| Mọi thứ cùng lúc | Mọi phần chuyển động trong mọi still | Không có hold, không có hành động dẫn dắt | Mỗi lúc một hành động, hold sau các dáng chính |
| Tiếp đất không trọng lượng | Cơ thể tiếp đất không nén, không bụi, không hạ người | Không có squash khi tiếp xúc, không có anticipation | `squash` khi tiếp đất, hạ hông xuống, bụi từ `effects.md` |
| Không đọc được khuôn mặt | Đầu là một chấm nhỏ trong khung hình dọc | Một beat khuôn mặt được dàn dựng trong wide shot | Một close shot cho beat đó |
| Vượt hướng màn hình | Một nhân vật đứng ở phía bên kia sau một cú cắt | Không có hướng theo section | Ghi phía đứng và hướng quay mặt trong storyboard |
| Miệng mấp máy không có tiếng | Miệng chuyển động mà không nghe thấy gì | Một channel để chạy | Miệng chỉ chuyển động trên âm thanh được nghe thấy |
| Kích thước pixel lẫn lộn (pixel art) | Một số pixel to hơn hoặc mềm hơn các pixel khác | Một phần được vẽ ở độ phân giải đầy đủ, hoặc một sprite bị xoay | Vẽ mọi thứ trên canvas nhỏ của `kit-pixel.ts`; xem `art-styles.md` |

Chủ sở hữu đánh giá diễn xuất trên animatic và trên một section mẫu có nhân vật đã dựng. Một nhân vật chủ sở hữu không thích được sửa trong cast file, một lần, và mọi shot thay đổi theo. Đó là lý do có file này.
