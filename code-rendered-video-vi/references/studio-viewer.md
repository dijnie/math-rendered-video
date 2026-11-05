# Studio viewer

Studio là trang mà owner (chủ phim) dùng để xem phim, từ ngày đầu tiên, khi mọi shot vẫn còn là thẻ storyboard, cho đến ngày phim hoàn thành. File này đặc tả trang đó phải làm gì, starter làm điều đó ra sao, và phim được bàn giao thế nào: dưới dạng chính trang này, được build thành một file HTML duy nhất phát được từ ổ đĩa. Một file video chỉ được làm khi owner yêu cầu.

Nạp file này khi: bạn thiết lập studio cho một bộ phim mới, chuẩn bị một buổi review với owner, bàn giao phim, thay đổi player, thẻ storyboard hay overlay, hoặc owner báo rằng một shot bị trống, bị trễ hay lệch đồng bộ.

## 1. Phạm vi và bản triển khai tham chiếu

Bản triển khai tham chiếu của file này là starter mà skill đi kèm, `assets/starter/`. Một thư mục phim là một bản sao của nó, và mọi đường dẫn trong file này là tương đối theo thư mục đó, thư mục chứa `package.json`. Danh sách shot và lời là `shots.json` và `copy.json` trong thư mục đó. Beat grid (lưới nhịp) và thời điểm các cú cắt là `data/audio.json`. Studio server tự phục vụ các thư mục `audio/` và `data/` (plugin `filmFolders` trong `vite.config.ts`), nên không có link nào phải giữ.

Starter được làm từ app của bộ phim tham chiếu. Khi file này nói "app tham chiếu", ý là app trước đó, thứ mà starter đã thay thế.

Starter dùng hai tên khác với thuật ngữ của skill này.

| Thuật ngữ của skill này | Tên trong starter |
|---|---|
| section (một nhóm shot) | một `group` trong `shots.json`, định kiểu trong `src/film.ts`. Một section có đánh số là một group thuộc kind `section`; các kind còn lại là `title`, `recap` và `end` |
| shot | một mục của danh sách `sections` trong `data/audio.json`, và một mục của `shots` trong `shots.json` |

Mọi thứ trong các section 2 đến 11 và trong section 14 đều có trong code của starter, trừ khi một câu nói khác. Section 12 liệt kê các phần mở rộng, phần lớn chưa được build.

## 2. Studio dùng để làm gì, theo từng giai đoạn

Một tài liệu storyboard cho biết thứ tự các shot và độ dài của chúng tính bằng bar (ô nhịp). Nó không thể hiện được thời gian. Studio phát cùng storyboard đó theo tempo của bản nhạc, nên owner đánh giá phim bằng cách xem nó chứ không phải đọc về nó.

| Giai đoạn | Cái gì được phát | Owner đánh giá được gì | Những gì chờ giai đoạn sau |
|---|---|---|---|
| Animatic | Mọi shot là một thẻ storyboard. Nhạc phát. Các transition (chuyển cảnh) phát giữa các thẻ. Overlay hiển thị bộ đếm và mọi chú thích. | Nhịp cắt: mỗi cú cắt có rơi đúng chỗ bản nhạc đòi hỏi không. Độ dài của từng section và từng shot. Thứ tự các shot. Mỗi chú thích có đọc kịp trong thời gian của nó không. Một cái tên có được lộ ra đúng bar không. Phiên bản nhạc nào phục vụ bộ phim. | Hình ảnh, camera, frame rate. |
| Hỗn hợp | Shot đã build và thẻ trong cùng một lượt phát. Danh sách shot đánh dấu mỗi shot là đã build hay là thẻ và đếm số shot đã build. | Một shot đã build giữa các shot lân cận và dưới các transition của nó. Một shot đã build có giữ được suốt độ dài của nó không. Một plate (tấm nền chữ) chú thích có che thứ gì hình cần không. Frame rate của mỗi shot đã build. | Bộ phim như một khối liền. |
| Phim hoàn chỉnh | Mọi shot đều đã build. Con số ở đầu danh sách cho thấy không còn thẻ nào. | Toàn bộ phim trong một lượt phát. Frame rate ở shot nặng nhất. Hình so với tiếng ở đầu, giữa và cuối. | Không gì cả. Trang này chính là sản phẩm giao. |

Quy tắc cho lead (người dẫn dắt):

- Cho owner xem animatic và chờ owner xác nhận storyboard trước khi bất kỳ builder nào bắt đầu. Duyệt một bảng nội dung không phải là cho phép build.
- Đề nghị owner gọi tên một shot bằng tiêu đề của nó trong danh sách shot, và một khoảnh khắc bằng thời gian, bar và beat trên dòng thông tin. Cả hai đều có thể chuyển thành một capture.
- Đừng mô tả trong tài liệu những gì studio có thể phát. Đưa địa chỉ và nói cần nhìn vào đâu.

## 3. Yêu cầu

Đánh dấu mọi dòng khi bạn thiết lập studio cho một bộ phim mới. Các dòng MUST là cần thiết để owner đánh giá phim. Các dòng SHOULD có thể bỏ qua khi lý do không áp dụng cho bộ phim.

| ID | Mức | Yêu cầu | Lý do | Trong starter |
|---|---|---|---|---|
| S1 | MUST | Hình được hiển thị đúng tỉ lệ khung hình của phim, lấy từ cấu hình dự án duy nhất, và vừa cửa sổ mà không bị cắt hay kéo giãn. Phim dọc và phim ngang dùng cùng một trang. | Owner đánh giá bố cục và cỡ chữ. Một hình bị kéo giãn dẫn đến đánh giá sai. | `src/project-config.ts` (`width`, `height`, và các `formats` khác; `OUTPUT` là định dạng của trang). `src/main.ts` đặt `--out-w`, `--out-h` và `--out-aspect`. `index.html` định kích thước `#c` từ chúng. |
| S2 | MUST | Mọi shot của danh sách shot đều phát, theo thứ tự, cùng nhạc. Một shot chưa có module được phát bằng thẻ storyboard. | Toàn bộ phim có thể phát được từ ngày đầu tiên. | `src/timeline.ts` (`has`, `CARD`). |
| S3 | MUST | Danh sách shot được nhóm theo section. Mỗi dòng hiển thị thời điểm bắt đầu, tiêu đề và shot đã build hay là thẻ. Phần đầu đếm số shot đã build. | Owner gọi tên một shot bằng tiêu đề của nó trong danh sách này. Con số đếm là trạng thái sản xuất. | `src/main.ts` (`setupPlayer`), `index.html` (`#shots`, `#count`). Tiêu đề nhóm lấy từ `groupHeading` trong `src/film.ts`, và tiêu đề phía trên danh sách là `title` từ `src/project-config.ts`. |
| S4 | SHOULD | Dòng của shot đang phát được đánh dấu và cuộn vào tầm nhìn. Tiêu đề của nó đứng cạnh các nút điều khiển. | Owner luôn biết shot nào đang ở trên màn hình. | `src/main.ts` (`tick`), `index.html` (`.shot.on`, `#now`). |
| S5 | MUST | Phát và tạm dừng, bằng nút, bằng phím và bằng một click lên hình. | Đó là việc đầu tiên owner làm. | `src/main.ts` (`setPlaying`, `toggle`). |
| S6 | MUST | Scrub (tua kéo): một thanh trải suốt độ dài phim. Hình đi theo ngay lập tức, kể cả khi đang tạm dừng. | Có thể đến và kiểm tra bất kỳ khoảnh khắc nào. | `index.html` (`#scrub`), `src/main.ts` (`seek`). Bước nhảy là 0,001 giây. Sau một lần seek, thanh scrub trả lại focus (`scrub.onchange`), nên các phím mũi tên vẫn giữ bước nhảy riêng của chúng. |
| S7 | MUST | Điều khiển bằng bàn phím cho phát, seek và nhảy giữa các shot. Bước nhảy một frame là SHOULD. | Nhịp được đánh giá bằng mắt nhìn vào hình, không phải vào con trỏ. | `src/main.ts` (listener `keydown`). Các phím chữ được so sánh không phân biệt hoa thường, nên Caps Lock và Shift không chặn chúng. |
| S8 | MUST | Nhảy tới một shot bằng click lên dòng của nó và bằng phím. | Các buổi review đi theo từng shot. | `src/main.ts` (`r.onclick`, phím `[` và `]`). |
| S9 | SHOULD | Loop một shot. | Một shot được đánh giá bằng cách xem nó nhiều lần cùng nhạc của nó. | `src/main.ts` (phím `l`, `loop`). |
| S10 | SHOULD | Chuyển giữa các nguồn audio dùng chung một timing. Vị trí và trạng thái phát được giữ nguyên. | Các phiên bản nhạc được đánh giá bằng tai, đối chiếu với hình. | `src/project-config.ts` (`studioAudio`), `src/main.ts` (`setMusic`, `hasAudio`). Một file có trong danh sách mà server không có sẽ bị bỏ qua. Sau các file của phim, nút chuyển luôn có `click`, một tiếng click ở mọi beat tạo từ beat grid (`src/click-track.ts`), và `silent`, nên một bộ phim không có nhạc vẫn phát được. |
| S11 | MUST | Một dòng thông tin hiển thị thời gian tính bằng giây, bar, beat trong bar, và số frame mỗi giây khi đang phát hoặc một chữ báo tạm dừng. Nó cũng cho biết khi loop đang bật. | Một nhận xét của owner có thể chuyển thành capture của đúng khoảnh khắc đó. Frame rate trên trang là phép đo duy nhất về việc phát trên máy của owner. | `src/main.ts` (`info.textContent`). Bar được đếm từ không, beat từ một đến bốn. Frame rate được lấy trung bình trên nửa giây. |
| S12 | MUST | Khi player đang tạm dừng và không có gì thay đổi, trang không vẽ gì. | Owner để trang mở trong khi làm việc. Một trang tạm dừng mà vẫn vẽ lại sẽ làm nặng máy mà không ra hình mới nào. | `src/main.ts` (`drawn`, và phép thử `playing \|\| t !== drawn`). |
| S13 | MUST | Một scene module vừa lưu thay thế scene đang chạy mà không reload trang. Player giữ vị trí và tiếp tục phát. | Builder lưu file trong khi owner đang xem. Reload trang đưa player về lại từ đầu. | `vite.config.ts` (`sceneHotSwap`), `src/main.ts` (listener `scene-module-updated`), `src/engine/engine.ts` (`reload`). |
| S14 | MUST | Một scene nạp thất bại được báo trên trang, kèm id của shot và stack. | Lỗi được hiển thị ở nơi owner và lead nhìn vào. | `src/engine/engine.ts` (`loadEntry`, `errors`), `index.html` (`#errs`). |
| S15 | MUST | Một scene bị lỗi không làm dừng phim. Shot của nó hiển thị một frame đỏ sẫm và mọi shot khác vẫn phát. | Một shot hỏng không được che mất phần còn lại của phim. | `src/engine/engine.ts` (`drawEntry`). |
| S16 | MUST | Lỗi từ trình duyệt của owner đến được log của development server. | Lead không thấy được màn hình của owner, và trình duyệt capture có thể không lỗi ở chỗ trình duyệt của owner lỗi. | `console.error` trong `src/engine/engine.ts`, được chuyển tiếp tới terminal của studio vì `vite.config.ts` đặt `server.forwardConsole: true`. App tham chiếu để trống tuỳ chọn này; starter đáp ứng dòng này bất kể ai khởi động server (section 10). |
| S17 | MUST | Studio chạy trên một port cố định và từ chối khởi động khi port đó đã bị chiếm. | Địa chỉ không bao giờ thay đổi. Một port bị chiếm làm lộ ra một server bị bỏ quên đang chạy, thay vì thêm một server thứ hai. | `package.json`, script `studio` (`vite`). `vite.config.ts` đặt `server.port` bằng `studioPort` từ `src/project-config.ts` (5180 trong starter) và `strictPort: true`. |
| S18 | MUST | Trang owner xem và trang mà công cụ capture điều khiển là cùng một app. | Khi đó một capture cho thấy đúng những gì studio hiển thị ở thời điểm đó. | `src/main.ts` (`setupExport`, `setupPlayer`), được chọn bằng tham số URL `export`. |
| S19 | SHOULD | Trang mang một marker để công cụ có thể phân biệt app này với bất kỳ thứ gì khác trả lời trên một port. | Công cụ capture không được gắn vào trang của một dự án khác. | Plugin `pageIdentity` trong `vite.config.ts` thêm `<meta name="render-app">` với giá trị của `appMarker()` (`src/project-config.ts`), vốn mang tên bộ phim. `scripts/render.ts` (`reachable`) chỉ chấp nhận một trang khi giá trị đó là của bộ phim này. App tham chiếu chỉ kiểm tra rằng có một marker. |
| S20 | SHOULD | Studio phát các bản sao nén của audio, với cùng timing như file master. | Trang nạp nhanh, và một beat grid phục vụ mọi bản sao. | `src/project-config.ts` (`audioFile`, `studioAudio`). |
| S21 | SHOULD | Các nhãn của trang dùng ngôn ngữ của owner, và trang liệt kê các phím của nó. | Owner tự dùng trang một mình. | `index.html` (`#keys`) và các nhãn nút trong `src/main.ts`. Nhãn của starter bằng tiếng Anh; hãy dịch chúng khi owner đọc ngôn ngữ khác. |
| S22 | SHOULD | Một bộ phim làm ở nhiều định dạng có thể xem ở từng định dạng trên cùng trang, và dòng thông tin nêu tên định dạng đang hiển thị. | Owner duyệt từng định dạng bằng cách xem nó, không phải đọc về nó. | `src/main.ts` (`nextFormat`, nút `#format`, phím `f`), tham số trang `format`. Trang được nạp lại ở định dạng tiếp theo tại cùng thời điểm, vì mọi target lấy kích thước của nó lúc nạp. Nút bị ẩn khi phim chỉ có một định dạng. |
| S23 | SHOULD | Trang công bố `window.seek(t)`, hàm vẽ frame tại song time (thời gian bài nhạc) `t` và resolve khi mọi hình của frame đó đã nạp xong. | Nhiều prompt yêu cầu một hàm như vậy theo tên, và khi đó một người hay một công cụ bên ngoài studio có thể hiển thị bất kỳ khoảnh khắc nào. | `src/main.ts`. Trong studio nó cũng tạm dừng player tại `t`. `window.duration` là độ dài của phim. |

### Hot swap hoạt động thế nào

1. Plugin `scene-hot-swap` trong `vite.config.ts` chỉ chạy trong development server. Nó xem xét mọi file nằm trực tiếp trong `src/scenes/` có chứa `export default class`, và nối thêm một khối chấp nhận các cập nhật của chính module đó.
2. Khi một file như thế được lưu, khối đó gửi window event `scene-module-updated` kèm tên file và module mới.
3. `src/main.ts` gọi `engine.reload(id, module)` cho mọi mục timeline phát file đó. Engine huỷ scene cũ, xoá các lỗi cũ của nó và tạo scene mới.
4. Player đặt `drawn` thành `-1`, để một trang đang tạm dừng vẽ scene mới một lần, và làm mới bảng lỗi.

Các file mà nhiều scene dùng chung nằm trong `src/scenes/parts/`. Chúng không có khối như vậy, nên một thay đổi trong một file đó sẽ lan tới các scene import nó, và từng scene đó được swap. Một thay đổi trong file mà player, timeline hay engine cũng import sẽ reload toàn bộ trang. Sau một lần reload, player bắt đầu ở không, hoặc ở thời điểm cho bởi tham số URL `t`.

Một shot là đã build hay là thẻ được quyết định khi timeline được tạo, lúc nạp trang (`has` trong `src/timeline.ts`). Một shot vừa được viết module lần đầu sẽ hiện là đã build sau khi trang được nạp lại.

## 4. Điều khiển

| Phím hoặc click | Hành động |
|---|---|
| Space | Phát hoặc tạm dừng. |
| Click lên hình | Phát hoặc tạm dừng. |
| Nút Play | Phát hoặc tạm dừng. Nhãn nêu tên hành động đang khả dụng. |
| Nút Music, hoặc `m` | Nguồn audio tiếp theo. Nhãn nêu tên nguồn đang phát. |
| Thanh scrub | Seek tới bất kỳ thời điểm nào. |
| Mũi tên phải, mũi tên trái | Tiến một giây, lùi một giây. |
| Shift kèm một mũi tên | Tiến hoặc lùi năm giây. |
| `.` và `,` | Tiến một frame, lùi một frame. Một frame bằng một chia cho frame rate đã cấu hình. |
| `]` | Điểm bắt đầu của shot tiếp theo. |
| `[` | Điểm bắt đầu của shot đang phát. Nếu nhấn trong vòng 0,3 giây kể từ điểm bắt đầu đó, thì là điểm bắt đầu của shot trước. |
| `l` | Loop shot dưới playhead (đầu phát), hoặc tắt loop. |
| Nút Format, hoặc `f` | Nạp lại trang ở định dạng tiếp theo của phim, tại cùng thời điểm. |
| Click lên một dòng của danh sách shot | Điểm bắt đầu của shot đó. |

Một lần nhảy rơi vào một mili giây sau điểm bắt đầu của shot, để thời điểm nằm bên trong shot chứ không nằm đúng trên cú cắt. Loop ở lại trên shot mà nó được đặt: khi loop đang bật và phim đang phát, một lần seek vượt quá cuối shot đó sẽ bị đưa trở về điểm đầu của nó. Dòng phím in trên trang liệt kê mọi phím trong bảng này. Các phím chữ hoạt động khi bật Caps Lock, và sau một click lên thanh scrub, các phím mũi tên vẫn di chuyển một giây, vì thanh trả lại focus sau lần seek.

## 5. Tham số URL

| Tham số | Có tác dụng ở | Hiệu ứng |
|---|---|---|
| `export` (giá trị bất kỳ, viết `export=1`) | Chọn chế độ | Chế độ export. Không tạo player và không tạo phần tử audio. Các nút điều khiển, danh sách shot và bảng lỗi bị ẩn. Canvas đứng ở góc trên bên trái với đúng kích thước output. Trang công bố `window.__render` (section 9). |
| `only=id1,id2` | Studio và export | Chỉ các shot được nêu tên mới được nạp, giúp trang nạp nhanh hơn. Overlay luôn được nạp. Một shot không được nạp hiển thị một frame đỏ sẫm. Một transition chỉ phát khi các shot ở cả hai bên cú cắt đều được nạp. |
| `t=53.5` | Studio | Thời điểm tính bằng giây mà player đứng khi trang đã nạp xong. Player ở trạng thái tạm dừng. |
| `scale=2` | Studio và export | Một số nguyên từ 1 đến 4. Hình được vẽ ở kích thước gấp chừng ấy lần kích thước đã cấu hình. Các scene vẫn bố cục theo kích thước đã cấu hình. Nó tồn tại cho các capture ở độ phân giải cao hơn. |
| `format=16:9` | Studio và export | Một trong các định dạng của `src/project-config.ts`. Trang được vẽ ở kích thước của định dạng đó, với các vùng của định dạng đó. Không có nó thì là định dạng master. Một tên không xác định được báo trong console và định dạng master được hiển thị. |

Không có tham số nào nêu tên một shot, và trang không ghi vị trí của nó vào địa chỉ.

## 6. Thẻ storyboard

Một module, `src/scenes/storyboard-card.ts`, phát mọi shot chưa có module riêng. Nó tìm shot của mình từ id của mục timeline (`shotOf` trong `src/film.ts`), nên toàn bộ chữ của nó đến từ `shots.json`. Không có gì về một shot được viết cứng trong app.

| Trên thẻ | Trường trong `shots.json` |
|---|---|
| Một viền nét đứt và không có hình. Thẻ nói rằng nó là một thẻ giữ chỗ. | |
| Id của shot và các bar mà nó chiếm | `id`, `bar`, `bars` |
| Tiêu đề, cỡ lớn | `title` |
| Những gì có trên màn hình | `see` |
| Điều gì xảy ra với nhạc | `move` |
| Camera làm gì | `camera` |
| Transition dẫn vào shot, theo nhãn của nó | `in.kind`, tra trong `transitions` |
| Loại hình ảnh | `look` |
| Nền sáng hay tối | `tone` |

Các khối mô tả được bố cục một lần, khi thẻ được tạo: thành một cột trong khung cao, thành hai cột khi khung rộng hoặc một cột không vừa, ở cỡ lớn nhất vừa giữa tiêu đề và các ô beat, đo ở đúng kích thước được vẽ. Thẻ cho phép đi xuống dưới cỡ chữ nhỏ nhất của kit, tới 22 đơn vị, trước khi cắt ngắn một khối bằng dấu ba chấm; nó là một thẻ làm việc đọc trong studio, không phải một hình của bộ phim.

Thẻ đánh dấu beat theo hai cách. Tiêu đề phóng to vài phần trăm ở mỗi beat rồi thu lại. Ở chân thẻ có một ô vuông cho mỗi beat của shot, mười sáu ô một hàng và xếp thành nhóm bốn, để một nhóm là một bar. Các beat đã qua thì sáng, beat đang phát có màu tín hiệu, và các beat sắp tới thì mờ. Số ô vuông cho thấy độ dài của shot chỉ trong một cái liếc.

Các transition phát giữa các thẻ y như chúng sẽ phát giữa các shot đã build, vì engine làm việc trên hình hoàn chỉnh của mỗi bên. Một transition mà một shot cần tham gia sẽ có một phương án thay thế (stand-in) khi một trong hai bên vẫn còn là thẻ (`standIn` trong `src/timeline.ts`, `played` trong `src/engine/transition.ts`).

| Loại transition | Cả hai shot đã build | Một trong hai shot vẫn là thẻ |
|---|---|---|
| `travel` | Engine không làm gì ở cú cắt. Hai shot tự mang camera. | Một whip (lia nhanh) thay thế. |
| `match` | Một cú cắt trơn mà các shot đã canh khớp. | Một cú cắt kèm một cú punch (nhấn) nhỏ, để cảm nhận được cú cắt. |
| `zoom-in`, `pull-out` | Shot tự phát phần của mình khi scene của nó đặt `handlesPortal`. | Engine phát một cú zoom trơn giữa hai hình. |
| Mọi loại khác | Do engine phát. | Do engine phát theo cùng cách. |

## 7. Overlay

`src/scenes/overlay.ts` vẽ bộ đếm và các chú thích. Nó là một mục timeline chạy suốt độ dài của phim và được đánh dấu `overlay`. Engine vẽ nó sau shot, trên hình đã hoàn chỉnh, và nó không tham gia vào các transition. Cái gì hiển thị lúc nào là dữ liệu: timing và vị trí lấy từ `shots.json`, lời lấy từ `copy.json`.

| Phần | Hiển thị gì | Nguồn |
|---|---|---|
| Bộ đếm | Số thứ tự của section trên tổng số, ở góc trên bên trái trên plate tối riêng của nó. Một dấu caret bên cạnh sáng lên trong nửa đầu của mỗi beat. | `n` của group của section. Tổng số là số group thuộc kind `section` (`SECTION_COUNT` trong `src/film.ts`) |
| Lộ tên | Trước bar `reveal`, bộ đếm hiển thị `???` thay cho tên. Từ bar đó trở đi nó hiển thị tên, và plate hơi nảy nhẹ khi tên xuất hiện. | `reveal` và `name` của group của section. Không có `reveal` thì tên hiển thị từ bar đầu tiên của section |
| Chú thích | Một câu, từng dòng một: dòng đầu cùng với plate, sau đó mỗi nửa beat thêm một dòng. Chữ được đặt nhỏ hơn khi một dòng không vừa. | `captions` trong `shots.json` (`group`, `kind`, `bar`, `bars`, `how`, `place`). Các dòng là `lines[kind]` của mục của section trong `copy.json`, nối theo `group`. Nhãn nhỏ trên plate và màu của thanh của nó là `labels[kind]` và `accents[kind]` của `copy.json` |

Mỗi chú thích có một chế độ, trường `how`.

| `how` | Trên một shot đã build | Trên một thẻ |
|---|---|---|
| `plate` | Overlay đặt câu trên một plate tối tại `place`. | Như vậy. |
| `shot` | Overlay không vẽ gì. Shot tự đặt chữ như một phần của hình của nó. | Một plate vẽ mờ có viền nét đứt, gắn nhãn là chữ mà shot sẽ tự đặt. |
| `none` | Không có gì. Hình tự nói mà không cần chữ. | Một plate vẽ mờ có viền nét đứt, gắn nhãn là một khoảnh khắc không có chữ. |

| `place` | Plate đứng ở đâu |
|---|---|
| `top` | Dưới bộ đếm. Nó lớn dần xuống dưới. |
| `middle` | Căn giữa khung hình. |
| `bottom` | Trên cạnh dưới của vùng chú thích. Nó lớn dần lên trên. Đây là mặc định. |

Quy tắc đằng sau bảng thứ hai: khi một shot vẫn còn là thẻ, mọi chú thích được hiển thị dưới dạng plate, để owner có thể đọc toàn bộ lời của phim trong animatic và đánh giá xem mỗi câu có đọc kịp trong thời gian của nó không. `src/timeline.ts` đưa cho overlay danh sách các shot là thẻ (`params.cards`).

Chỉ các section có đánh số, các group thuộc kind `section`, mới mang bộ đếm và chú thích. Tiêu đề, recap và thẻ kết tự đặt lời của chúng.

Từ thực tế: trong app tham chiếu, tổng số của bộ đếm và tiêu đề của danh sách shot được viết tay trong code, và cả hai phải thay đổi cho mỗi bộ phim mới. Trong starter cả hai đều theo dữ liệu: tổng số là `SECTION_COUNT`, và tiêu đề là `title` trong `src/project-config.ts`.

## 8. Đồng hồ

Player giữ một con số, song time `t` tính bằng giây. Hình, thanh scrub, dòng được đánh dấu, bar và beat đều được suy ra từ nó. Khi phim đang phát, `t` đi theo phần tử audio:

```ts
const nowT = performance.now();
if (audio.currentTime !== lastAudioT) { lastAudioT = audio.currentTime; lastPerf = nowT; }
t = lastAudioT + (audio.paused ? 0 : (nowT - lastPerf) / 1000);
```

Trình duyệt báo `audio.currentTime` theo những bước dài hơn một frame. Nếu chỉ vẽ từ giá trị đó, hình sẽ đứng rồi nhảy. Vì vậy player nhớ giá trị được báo gần nhất và thời điểm nó thay đổi, rồi cộng thêm khoảng thời gian đã trôi qua kể từ đó. Wall time (thời gian thực của đồng hồ hệ thống) chỉ lấp khoảng trống giữa hai lần báo. Nó không bao giờ được cộng dồn suốt lượt phát.

Một lần seek giới hạn thời gian trong độ dài của phim, rồi đặt cả `t` lẫn `audio.currentTime`. Khi loop đang bật và `t` vượt qua điểm cuối của nó, player seek về điểm đầu. Khi audio đã kết thúc, player tạm dừng. Engine coi một thời điểm đi lùi, hoặc đi tới quá một phần tư giây (hoặc bốn frame, nếu khoảng đó dài hơn), là một lần seek, và đưa các scene có giữ trạng thái tới thời điểm mới trước khi vẽ.

Bar và beat lấy từ beat grid đã đo (`barAt` và `beatAt` trong `src/engine/audio.ts`), vốn chứa thời điểm của mọi beat. Chúng vẫn đúng khi tempo của bản nhạc bị trôi.

Hình phải được suy ra từ thời gian audio chứ không phải từ wall time đã trôi qua, vì bốn lý do.

| Lý do | Điều gì sai khi dùng wall time |
|---|---|
| Owner nghe audio. | Đồng hồ của thiết bị audio và đồng hồ hệ thống không chạy cùng tốc độ, và audio có thể khựng lại khi đang nạp. Hình trôi lệch khỏi tiếng. |
| Seek, loop và việc đổi nguồn audio đều dịch chuyển vị trí audio. | Mỗi thứ sẽ cần một lần hiệu chỉnh riêng cho đồng hồ của hình. |
| Một frame là một hàm của song time. | Scrub, bước nhảy frame, một capture tại thời điểm owner nêu và studio sẽ không hiển thị cùng một hình cho cùng một thời điểm. |
| Trình duyệt ngừng vẽ một trang ở chế độ nền. | Khi quay lại, hình sẽ chậm hơn tiếng. |

## 9. Export hook

Với tham số URL `export`, trang công bố `window.__render`. Công cụ capture `scripts/render.ts` là người dùng duy nhất của nó.

| Thành viên | Trả về gì |
|---|---|
| `ready` | `true` khi mọi thành viên khác đã sẵn sàng. |
| `error` | Stack dưới dạng text. Nó chỉ có mặt khi trang khởi động thất bại, và khi đó hook không có thành viên nào khác. |
| `errors` | Một danh sách text, mỗi text cho một scene nạp thất bại, mỗi text bắt đầu bằng id của shot trong ngoặc vuông. |
| `duration` | Độ dài của phim tính bằng giây. |
| `fps` | Frame rate đã cấu hình. |
| `logicalWidth`, `logicalHeight` | Kích thước của định dạng đang hiển thị, tính bằng pixel. |
| `format` | Tên của định dạng đó. |
| `scale` | Giá trị của tham số URL `scale`. |
| `width`, `height` | Kích thước output tính bằng pixel: kích thước đã cấu hình nhân với `scale`. |
| `timeline` | Một danh sách gồm `id`, `start` và `end` của mọi shot. Overlay bị loại ra. |
| `timeOfBeat(i)` | Song time tính bằng giây của beat `i` trong beat grid. Cho phép phân số. |
| `still(t, samples, shutter)` | Vẽ frame tại song time `t` lên canvas, chờ mọi ảnh hay frame clip của nó còn đang nạp và vẽ lại (`renderSettled` trong `src/engine/engine.ts`). Resolve thành số sub-frame đã dùng, là 1 trừ khi `samples` yêu cầu nhiều hơn. |
| `png()` | Một promise trả về frame vẽ gần nhất dưới dạng PNG ở kích thước output đầy đủ, mã hoá base64. |
| `engine` | Chính engine. Chế độ `perf` của công cụ capture dùng nó để đo thời gian frame. |
| `stream(options)` | Vẽ một dải frame và gửi chúng qua WebSocket tới một encoder. Nó chỉ phục vụ việc export video. |

Bên cạnh `window.__render`, mọi trang đều công bố `window.seek(t)` và `window.duration` (S23). Trên trang export, `window.seek(t)` là `still(t)` không có giá trị trả về. Một prompt yêu cầu "một `seek(t)` tất định" được đáp ứng bởi hợp đồng của engine (`engine-architecture.md`, section 1) và bởi hàm này; công cụ capture vẫn tiếp tục dùng `window.__render`, vốn còn báo lỗi, kích thước và timeline.

Công cụ capture dùng trang như thế nào:

1. Nó lấy thư mục khoá `.render.lock`, để mỗi lúc chỉ chạy một capture. Lượt chạy thứ hai sẽ chờ. Thư mục chứa khoá được tìm bởi `lockHome` trong `scripts/render.ts`: thư mục do biến môi trường `RENDER_LOCK_DIR` chỉ định, nếu không thì thư mục gần nhất phía trên thư mục phim có chứa `.git`, nếu không thì thư mục gần nhất có chứa `CLAUDE.md` hoặc `AGENTS.md`, nếu không nữa thì thư mục tạm của hệ thống. Vì vậy mọi bộ phim trong cùng một repository dùng chung một khoá.
2. Nó khởi động một development server riêng trên một port trong khoảng 5300 đến 5799 với live reload bị tắt (`RENDER_NO_HMR=1`), và dừng server đó khi đã xong. Với `--url`, ví dụ `http://localhost:<studioPort>` (port của `src/project-config.ts`), nó dùng server ở địa chỉ đó thay thế và chỉ chấp nhận trang nếu marker của nó (S19) mang tên bộ phim này. Khi bộ phim này không trả lời ở đó, nó dừng với một lỗi nêu tên bộ phim đang trả lời.
3. Nó mở Chrome không cửa sổ, ở kích thước của định dạng được yêu cầu (`--format`, mặc định là master), với graphics backend của hệ thống hoặc backend do `--angle` chỉ định, nạp trang với `export=1` và với `only`, `scale` và `format` theo yêu cầu, rồi chờ `ready` hoặc `error`. Với `--page` nó mở một bản build single-file từ ổ đĩa thay thế, và không khởi động server nào.
4. Nó kiểm tra kích thước, in ra `errors`, và gọi `still` cho mỗi thời điểm được yêu cầu. Ở scale 1 nó lưu một screenshot của trang. Ở scale cao hơn nó lưu những gì `png()` trả về.
5. Nó in log của trình duyệt: các lỗi và cảnh báo console, lỗi trang, và mọi response có status từ 400 trở lên.

Công cụ capture từ chối chế độ `video` của nó trừ khi biến môi trường `OWNER_ASKED_FOR_VIDEO` có giá trị `yes`.

## 10. Hỗ trợ trình duyệt

Trình duyệt của owner có thể khác trình duyệt capture. Công cụ capture điều khiển Chrome (`channel: 'chrome'` trong `scripts/render.ts`). Một shot có thể đúng trong mọi capture mà vẫn hỏng trên màn hình của owner.

| Loại lỗi | Hiển thị ở đâu |
|---|---|
| Trang khởi động thất bại | Stack màu đỏ ở góc trên bên trái trang. |
| Một scene nạp hoặc tự thiết lập thất bại | Bảng lỗi của trang, console, và một frame đỏ sẫm cho shot đó. |
| Một scene ném lỗi khi đang vẽ | Một frame đỏ sẫm cho shot đó và dòng console `scene <id> render error`. Bảng lỗi không hiển thị nó. |
| Overlay ném lỗi khi đang vẽ | Dòng console `overlay <id> render error`. Shot phát mà không có bộ đếm và chú thích. |

Quy tắc cho lead:

- Khi owner báo một shot bị trống hoặc hỏng mà các capture vẫn ổn, hãy đọc log của development server trước. Đừng trả lời bằng phỏng đoán.
- Trong một stack, các dòng có dạng `name@http://...` và `@[native code]` đến từ WebKit, engine của Safari.
- Các scene không được dùng `filter` của context 2D của canvas, thứ mà Safari không có. `letterSpacing` của canvas cũng có thể bị thiếu. Nó thất bại mà không báo lỗi và đặt chữ sít hơn, nên không bố cục nào được phụ thuộc vào nó.
- Để capture trên một browser engine khác, engine đó phải được cài cho công cụ capture. Hỏi owner trước khi cài.

Luồng chuyển tới log của server là tuỳ chọn `server.forwardConsole` của development server. Theo tài liệu của Vite (đọc ngày 2026-09-28), mặc định nó chỉ bật khi server phát hiện ra rằng một AI coding agent đã khởi động nó, nên một server mà owner tự khởi động bằng tay đã không ghi log gì từ trình duyệt trong app tham chiếu. Starter đặt tuỳ chọn này thành `true` trong `vite.config.ts`, nên lỗi của owner đến được terminal của studio bất kể ai khởi động nó. Giữ dòng đó khi bạn thay đổi cấu hình.

Những gì chỉ owner mới test được:

| Test | Cách làm |
|---|---|
| Mọi shot đều hiển thị hình trên trình duyệt của owner | Phát phim một lần từ đầu đến cuối và tìm các frame đỏ sẫm. |
| Frame rate khi phát | Đọc dòng thông tin ở shot nặng nhất. |
| Hình so với tiếng | Xem một sự kiện rơi đúng một tiếng trống ở đầu, giữa và cuối phim. |
| Bản thân bản nhạc | Bằng tai, với nút chuyển giữa các nguồn audio. |

Từ thực tế: owner xem trên Safari và hai lần báo một shot bị trống, trong khi mọi capture của nó đều ổn. Câu trả lời đầu tiên, rằng trang đã được xem giữa lúc đang build, là phỏng đoán và nó sai. Engine đã vá thuộc tính `filter` của context 2D của canvas mà không kiểm tra xem nó có tồn tại không, nên shot ném lỗi ở mọi frame trên Safari. Log của server cho thấy lỗi ngay lập tức, kèm id của shot và một stack WebKit.

## 11. Giao phim

Phim được bàn giao dưới dạng một trang phát trong trình duyệt. Nó có hai dạng, cùng một code:

| Dạng | Nó là gì | Dùng cho |
|---|---|---|
| Studio | Development server và trang mà nó phục vụ (`bun run studio`) | Mọi buổi review trong khi làm phim: hot swap, log server của trình duyệt owner, nút chuyển nhạc |
| Single file | Một file HTML với script (three.js và mọi scene bên trong), font, dữ liệu, hình ảnh và nhạc được đóng gói sẵn (`bun run single`) | Bàn giao: mở bằng double click, không cần server, không cần mạng và không cần cài đặt |

### Single file

```sh
bun run single                               # out/single/<title>.html, with the first music file of studioAudio that exists
bun run single -- --audio all                # every music file of studioAudio that exists; the music switch keeps them
bun run single -- --audio none               # no music file: the click track and silence
bun run single -- --audio audio/track.m4a    # this file only
bun run single -- --format 1:1               # opens in that format; the Format button still switches
bun scripts/render.ts stills --page out/single/<title>.html --t 5   # a still taken from the file itself
```

Cách nó được làm: `scripts/build-single.ts` chạy bản build của Vite với biến môi trường `SINGLE_FILE` được đặt, thứ mà `vite.config.ts` biến thành một script duy nhất không có chunk và dùng đường dẫn tương đối. Sau đó script đóng gói, dưới dạng base64, mọi file của `public/` (các font và giấy phép của chúng), các file JSON của `data/`, mọi file của `media/`, và nhạc được yêu cầu, rồi ghi trang với hai inline script: một script nhỏ trả lời `fetch()` cho các file đã đóng gói và tạo một blob URL cho nhạc (`window.__filmFileUrl`), rồi tới app. Một đường dẫn dưới thư mục của trang mà không được đóng gói sẽ trả về 404, nên trang không bao giờ đọc ổ đĩa và phát giống nhau ở bất cứ đâu nó được mở. Một comment ở đầu file liệt kê những gì đã được đóng gói và giấy phép của engine, của các thư viện trong script và của các font. Không có package nào được thêm vào cho việc này.

Khác gì so với studio: không có hot swap và không có log server; mọi thứ khác vẫn là cùng một trang, với cùng các phím, danh sách shot, nút chuyển nhạc, nút chuyển định dạng, `window.seek` và `?export=1`. Một still lấy từ file với `--page` là cùng một hình với still lấy từ studio.

Kích thước, đo trên bộ phim ví dụ của starter: script là 0,87 MB và font là 0,98 MB, và trang là 2,2 MB khi không có nhạc. Các file đóng gói lớn thêm một phần ba. Với file WAV 50 giây mà `bun run score` tạo ra (9,5 MB), trang là 15 MB. Một WAV master dài ba phút (khoảng 30 MB) sẽ tạo ra một trang khoảng 42 MB, mở chậm và khó gửi; một bản sao nén có cùng timing (một file m4a hoặc mp3 từ 4 đến 6 MB cho ba phút) giữ trang dưới 10 MB. Bản build sẽ báo điều này khi nó đóng gói một WAV, và cảnh báo khi vượt 50 MB. Clip dưới dạng chuỗi ảnh là thứ lớn còn lại (`engine-architecture.md`, section 4).

Khi một prompt yêu cầu "một file HTML, không thư viện, vanilla WebGL": single file là một file HTML không cần gì khác, nhưng three.js và opentype.js nằm bên trong script của nó, và trang được build bằng công cụ, không phải viết tay. Hãy nói rõ điều đó với owner. Phương pháp này có phù hợp với yêu cầu như vậy hay không thì được quyết định trong chương route.

Những gì đã được thử: bản build, các still lấy từ file qua công cụ capture (giống từng byte với still của studio), và trang mở từ ổ đĩa trong headless Chrome trên Windows, phát nhạc đã đóng gói và trả lời `window.seek`. Chưa thử: mở nó trên Safari hay Firefox, trên điện thoại, và một trang lớn hơn 15 MB.

### Bàn giao

| Bước | Làm gì |
|---|---|
| Build | `bun run single`, với nhạc mà owner cần nghe. Lấy một still từ file với `--page` và so sánh với still của studio ở cùng khoảnh khắc |
| Bàn giao | Đường dẫn của file, các nút điều khiển ở section 4, các định dạng nó có thể hiển thị, và những gì nó không chứa (một file video) |
| Studio, khi owner review | Kiểm tra port (`studioPort` trong `src/project-config.ts`, 5180 trong starter). Nếu đã có một server trả lời ở đó và đó là studio này, hãy dùng nó. Nếu đó là một server bạn đã khởi động trước đó, hãy dừng nó. Đừng chuyển sang port khác. Hai bộ phim trên cùng một máy cần hai port. Chạy script `studio` từ thư mục phim, đưa địa chỉ `http://localhost:<studioPort>`, và dừng server bằng Ctrl+C khi owner đã xong |
| Studio cần gì | bun, Node.js 20 trở lên, và các package (`bun install`). Một tiến trình, development server, biên dịch các module khi trang yêu cầu và tự phục vụ `audio/`, `data/` và `media/`, với byte range để audio có thể seek. Một file bị thiếu trả về 404 |

```sh
lsof -i :5180                    # on Windows: netstat -ano | findstr :5180
bun run studio
```

Quy tắc:

- Một studio phục vụ toàn bộ dự án. Các builder không tự khởi động server hay trình duyệt riêng.
- Ai khởi động server thì người đó dừng nó. Không để server, trình duyệt hay watcher nào còn chạy sau khi công việc cần nó đã xong.
- Một capture không cần studio. Công cụ capture tự khởi động và dừng server riêng của nó, không có live reload, kể cả khi studio đang chạy. Nó chỉ dùng studio khi `--url` chỉ định studio, và khi đó chạy với live reload bật (section 14).

Kiểm tra trước khi bàn giao phim hoàn chỉnh:

| Mục | Cách kiểm tra |
|---|---|
| Không còn thẻ nào | Con số ở đầu danh sách shot. |
| Không scene nào nạp thất bại | Bảng lỗi trống, và công cụ capture không in ra lỗi scene nào, kể cả với `--page` trên single file. |
| Frame rate | Owner đọc dòng thông tin ở shot nặng nhất. |
| Hình so với tiếng | Bài test của owner ở section 10. |
| Mọi định dạng đã hứa | Một still của mỗi khoảnh khắc chính ở mỗi định dạng (`--format`). |
| Tiến trình | Không còn thứ gì do lead hay builder khởi động đang chạy. |

## 12. Các phần mở rộng tuỳ chọn

Không có phần nào trong số này nằm trong starter. Chỉ đặc tả một phần khi bộ phim cần đến nó. Mọi đường dẫn hướng hay dấu đánh của studio phải nằm ngoài hình trong chế độ export.

| Phần mở rộng | Mức | Trạng thái | Nó sẽ làm gì |
|---|---|---|---|
| Đường dẫn hướng vùng an toàn cho nền tảng đích | OPTIONAL | chưa build | Một đường viền phủ lên hình, bật tắt bằng một phím, cho thấy giao diện của nền tảng che khung hình ở đâu. Kit có một vùng `SAFE` trong `src/scenes/parts/kit-frame.ts` mà các scene bố cục bên trong. Studio không vẽ nó. |
| Bật tắt lớp chú thích | OPTIONAL | chưa build | Một phím ẩn overlay, để owner có thể kiểm tra hình có tự truyền đạt được ý mà không cần chữ không. |
| Chớp theo beat | OPTIONAL | chưa build | Một dấu bên ngoài hình chớp ở mọi beat, mạnh hơn ở beat đầu tiên của một bar, để đánh giá đồng bộ trên các shot đã build. Hiện tại chỉ các ô vuông của thẻ và dấu caret của bộ đếm đánh dấu beat. |
| Ghi chú theo từng shot lưu vào file | OPTIONAL | chưa build | Owner viết một nhận xét về shot đang phát. Nó được lưu kèm id của shot, thời gian, bar và beat vào một file mà lead đọc. Nó cần một phần trên server để ghi file. |
| Contact sheet của toàn bộ phim | OPTIONAL | chưa build | Một trang với một still của mọi shot. Công cụ capture có thể ghi một contact sheet thành file ảnh (chế độ `sheet`). Chưa có sheet bên trong studio. |
| Dấu cho các shot đã thay đổi kể từ lần review trước | OPTIONAL | chưa build | Một dấu trong danh sách shot trên mọi shot có module thay đổi sau thời điểm của lần review trước. |
| Loop toàn bộ phim | OPTIONAL | chưa build | Một phím loop từ cuối về 0, cho một loop liền mạch gồm nhiều shot. Hiện tại `l` loop shot dưới playhead, áp dụng cho một đoạn trong một shot. Mối nối của âm thanh khi phần tử audio seek lùi chưa được kiểm tra |
| Một nút chuyển định dạng | OPTIONAL | đã build | Các định dạng có tên trong `src/project-config.ts`, được chọn bằng `?format=`, nút Format, `--format` của công cụ capture và của bản build single-file (S22; `engine-architecture.md`, section 4, "Formats") |
| Một single file mở bằng double click | OPTIONAL | đã build | `bun run single` (section 11) |
| Một trang live cho tác phẩm phát khi click | OPTIONAL | chưa build | Một trang nhỏ riêng ghi lại các click của người xem và gọi cùng hàm vẽ với thời gian và danh sách các click. Studio phát lần chạy theo kịch bản của một tác phẩm như vậy (`short-pieces.md`, section 11) |

## 13. So sánh với HyperFrames Studio

Cột bên phải được lấy từ `hyperframes-facts.md`, section 8, vốn đã đọc các file skill của HyperFrames. Không có gì trong cột đó được chạy thử cho file này.

| Câu hỏi | Studio của skill này | HyperFrames Studio |
|---|---|---|
| Nó là gì | Một viewer: nó phát các shot theo thứ tự cùng nhạc và hiển thị một thẻ cho mọi shot chưa được build. | Một trình chỉnh sửa timeline trong trình duyệt, được các file của nó mô tả là một bề mặt review nơi người dùng phát video và chỉnh sửa bằng tay trước khi render. |
| Đơn vị của timeline | Shot, nhóm theo section, đặt trên một beat grid đã đo. | Một hàng cho mỗi phần tử cấp cao nhất. Các loại track là video, graphics, captions và audio. |
| Nó chỉnh sửa gì | Không gì cả. Thay đổi được thực hiện trong danh sách shot, file lời và các scene module, và trang tự nhận chúng. | HTML của composition. Một biểu tượng con mắt ghi `data-hidden`, một fader ghi `data-volume`. Có một effect rack và các automation lane. |
| Nó cần gì để chạy | Development server, khởi động từ thư mục phim, trên port cố định đặt trong `src/project-config.ts` (5180 trong starter). | `npx hyperframes preview`, một server local mặc định trên port 3002. Địa chỉ phải mang `#project/<project-name>`, nếu không sẽ không có project nào được nạp. |
| Thay đổi khi đang mở | Một scene module được swap và player giữ vị trí. | Nó hot-reload khi file thay đổi. Các file đã đọc không nói vị trí có được giữ hay không. |
| Nó dừng thế nào | Ctrl+C. Không còn gì sót lại. | Với `preview --background` nó tiếp tục chạy theo thiết kế. Nó được dừng bằng `npx hyperframes preview --stop`. |
| Vùng an toàn | Không vẽ (section 12). | Một nút bật tắt lề an toàn: action-safe ở 90 phần trăm, title-safe ở 80 phần trăm. Không cái nào là vùng giao diện của một nền tảng. |
| Agent đọc gì từ nó | Export hook, cho các capture. | Phần tử mà người dùng đã chọn, qua `preview --context --json`. |
| Bề mặt tốt hơn khi | Hình là một canvas do chính engine của phim vẽ. Cú cắt bám theo một beat grid đã đo, kể cả trên bản nhạc có tempo bị trôi. Phim phải phát được dưới dạng thẻ từ ngày đầu tiên. | Composition được làm từ các phần tử trang. Owner muốn thay đổi timing, khả năng hiển thị hay âm lượng bằng tay. Phim là một tác phẩm có thuyết minh với một track chú thích. |

## 14. Cạm bẫy

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Owner thấy một shot trống hoặc đỏ sẫm, và các capture vẫn ổn. | Trình duyệt của owner thiếu thứ gì đó mà scene hay engine dùng, và scene ném lỗi ở mọi frame. | Đọc log của server tìm `scene <id> render error`. Sửa nguyên nhân trong scene hoặc engine. |
| Một shot bị đỏ sẫm và bảng lỗi trống. | Lỗi ném ra khi đang vẽ chỉ đi vào console. Bảng chỉ liệt kê lỗi khi nạp. | Đọc log của server hoặc console của trình duyệt. |
| Log của server không cho thấy gì từ trình duyệt. | `server.forwardConsole` bị thiếu trong `vite.config.ts`. Starter có đặt nó; một cấu hình đã bị thay đổi có thể đã làm mất nó. | Đặt lại tuỳ chọn thành `true`, hoặc đề nghị owner mở console của trình duyệt. |
| Mọi shot trừ một shot đều đỏ sẫm. | Địa chỉ mang `only`. | Bỏ tham số đó. |
| Server không khởi động và báo port đang được dùng. | Một studio từ phiên trước vẫn đang chạy, hoặc một bộ phim khác trên máy dùng cùng `studioPort`. Server nghiêm ngặt về port. | Tìm tiến trình đang giữ port. Dùng nó, hoặc dừng nó nếu bạn đã khởi động nó. Cho mỗi bộ phim một port riêng trong `src/project-config.ts`. |
| Công cụ capture dừng và nói rằng bộ phim này không trả lời ở địa chỉ đó. | `--url` chỉ tới server của một bộ phim khác, hoặc không có server nào. Công cụ chỉ chấp nhận trang có marker mang tên bộ phim này. | Bỏ `--url` đi, để công cụ tự khởi động server riêng, hoặc đưa địa chỉ studio của bộ phim này. |
| Một capture thất bại giữa chừng, hoặc các still của nó trộn lẫn hình cũ và hình mới của một shot. | Capture được đưa `--url` và chạy trên studio, và một file đã được lưu trong lúc chạy. Studio bật live reload; chỉ server riêng của công cụ là tắt. | Bỏ `--url` đi, hoặc đừng lưu file khi một capture đang chạy trên studio. |
| Một scene vừa lưu làm reload toàn bộ trang. | File không có `export default class`, hoặc nó nằm ngoài `src/scenes/`, hoặc timeline hay player import nó. | Giữ các scene module nằm trực tiếp trong `src/scenes/` và các file dùng chung trong `src/scenes/parts/`. |
| Sau một lần reload player quay về từ đầu. | Vị trí không được giữ qua một lần reload trang. | Mở trang với tham số `t`. |
| Một shot vừa build vẫn phát dưới dạng thẻ. | Đã build hay là thẻ được quyết định lúc nạp trang. | Nạp lại trang. |
| Player tự nhảy lùi. | Một loop vẫn đang bật. Dòng thông tin cho thấy điều đó. | Nhấn `l`. |
| Frame rate thấp, và thu nhỏ cửa sổ không giúp gì. | Canvas luôn được vẽ ở kích thước output. Cửa sổ chỉ scale nó. | Làm shot nhẹ hơn. Đừng truyền `scale` trong studio. |
| Các thẻ hiển thị text mới, mà các cú cắt vẫn ở thời điểm cũ. | Các thẻ đọc danh sách shot. Timeline đọc thời điểm cắt từ `data/audio.json`, file mà `scripts/build-shot-files.py` ghi từ danh sách shot. | Chạy script đó (`bun run shots`) sau mỗi lần thay đổi danh sách shot, và chạy lại sau mỗi lần phân tích nhạc mới, vì việc đó ghi đè file. |
| Trang dừng với `data/audio.json has no sections`. | Beat grid được tạo hoặc đo lại, và thời điểm các shot chưa được ghi vào nó. | Chạy `bun run shots`. |
| Trang dừng với `no audio analysis data found`. | `data/audio.json` chưa tồn tại. | Tạo một grid (`bun run make-grid -- --bpm 120 --bars 24`) hoặc đo một grid từ nhạc, rồi chạy build script. |
| Nút chuyển nhạc chỉ có `click` và `silent`. | Không có file nào được liệt kê trong `studioAudio` nằm trong `audio/`. | Đặt các bản sao nén vào `audio/` với đúng tên mà cấu hình đưa ra. |
| Owner tưởng các plate mờ là chú thích cuối cùng. | Trên một thẻ, mọi chú thích được hiển thị dưới dạng plate. | Nói rõ trong bàn giao rằng một plate có viền nét đứt sẽ biến mất khi shot của nó được build. |
| Hình trôi lệch khỏi tiếng trong một player mới. | Hình được điều khiển bằng wall time đã trôi qua. | Suy ra song time từ phần tử audio (section 8). |
| Single file hiển thị phim cũ. | Nó được build trước lần thay đổi gần nhất; nó là một bản sao, không phải một khung nhìn vào thư mục. | Build lại nó sau mọi thay đổi mà owner cần thấy trong đó. |
| Single file không phát nhạc. | Không có file nào của `studioAudio` tồn tại khi nó được build, hoặc đã truyền `--audio none`. Khi đó nút chuyển nhạc chỉ có `click` và `silent`. | Đặt bản sao nén vào `audio/` và build lại. |
| Single file nặng hàng chục megabyte. | Một WAV đã bị đóng gói, hoặc các clip dài. | Đóng gói một bản sao nén của nhạc (`--audio audio/track.m4a`); giữ các clip ngắn và nhỏ. |
| Nút Format bị thiếu. | Phim chỉ có một định dạng. | Thêm định dạng vào `formats` trong `src/project-config.ts`. |

Từ thực tế: dự án tham chiếu chứa hai app mang cùng một giá trị marker, và app cũ hơn phục vụ trên port mà công cụ capture của app mới hơn tìm đến đầu tiên, nên các capture của bộ phim mới hơn bị lấy từ nhầm app. Starter tránh được điều này: marker của nó mang tên bộ phim, công cụ capture chỉ chấp nhận giá trị đó, và địa chỉ mặc định của nó là port studio của chính bộ phim.
