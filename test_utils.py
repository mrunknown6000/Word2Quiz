import pytest
from utils import *

case1 = {
    0: {'title': 'Câu 1: Châu Á tiếp giáp với những châu lục nào dưới đây ?', 'answer': ' Châu Âu, Châu Phi.',
        'options': [' Châu Phi, Châu Đại Dương.', ' Châu Mĩ, Châu Âu.', ' Châu Âu, Châu Phi.',
                    ' Châu Mĩ, Châu Phi.']},
    1: {'title': 'Câu 2: Châu Á không tiếp giáp với đại dương nào sau đây', 'answer': ' Đại Tây Dương.',
        'options': [' Thái Bình Dương.', ' Ấn Độ Dương.', ' Bắc Băng Dương.', ' Đại Tây Dương.']},
    2: {'title': 'Câu 3: Các núi và sơn nguyên cao của châu Á tập trung chủ yếu ở', 'answer': ' vùng trung tâm.',
        'options': [' vùng trung tâm.', ' vùng phía đông.', ' vùng phía tây.', ' phía bắc.']},
    3: {'title': 'Câu 4: Đặc điểm nào sau đây không phải là đặc điểm vị trí của Châu Á?',
        'answer': ' Đại bộ phận châu lục nằm giữa 2 chí tuyến.',
        'options': [' Là 1 bộ phận của lục địa Á Âu.', ' Đại bộ phận châu lục nằm giữa 2 chí tuyến.',
                    ' Kéo dài từ cực Bắc đến xích đạo.', ' Tiếp giáp 2 châu lục và ba đại dương.']},
    4: {'title': 'Câu 5: Chiều dài từ điểm cực Bắc đến điểm cực Nam châu Á là:', 'answer': ' 8500 km.',
        'options': [' 6500 km.', ' 7500 km.', ' 8500 km.', ' 9500 km.']},
    5: {'title': 'Câu 6: Chiều rộng từ bờ Tây sang bờ Đông nơi lãnh thổ Châu Á rộng nhất là:',
        'answer': ' 9.200 km.', 'options': [' 6.200km.', ' 7.200 km.', ' 8.200 km.', ' 9.200 km.']},
    6: {'title': 'Câu 7: Dãy núi nào sau đây là ranh giới tự nhiên giữa Châu Á và Châu Âu?', 'answer': ' U- ran.',
        'options': [' Himalaya.', ' U- ran.', ' An-tai.', ' Hin - đu - cúc.']},
    7: {'title': 'Câu 8: Đồng bằng Ấn Hằng thuộc khu vực nào sau đây?', 'answer': ' Nam Á.',
        'options': [' Bắc Á.', ' Đông Á.', ' Nam Á.', ' Đông Nam Á.']},
    8: {'title': 'Câu 9: Sơn nguyên nào sau đây thuộc khu vực Bắc Á?', 'answer': ' Trung Xibia.',
        'options': [' Trung Xibia.', ' Đê can.', ' Tây Tạng.', ' Ả rập.']},
    9: {'title': 'Câu 10: Đồng bằng Hoa Trung thuộc khu vực nào sau đây?', 'answer': ' Đông Á.',
        'options': [' Bắc Á.', ' Nam Á.', ' Đông Nam Á.', ' Đông Á.']}}
case2 = {
    0: {'title': 'Câu 25: Quốc gia xuất khẩu gạo lớn nhất thế giới hiện nay là', 'answer': ' Ấn Độ.',
             'options': [' Thái Lan.', ' Việt Nam.', ' Trung Quốc.', ' Ấn Độ.']},
         1: {'title': 'Câu 26: Vật nuôi chủ yếu ở các vùng khí hậu khô hạn của châu Á là', 'answer': ' dê, cừu.',
             'options': [' dê, cừu.', ' trâu, bò.', ' lợn, gà.', ' lợn, vịt.']},
         2: {'title': 'Câu 27: Vật nuôi chủ yếu ở các vùng khí hậu ẩm ướt của châu Á là', 'answer': ' trâu, gà.',
             'options': [' dê, cừu.', ' trâu, gà.', ' tuần lộc', ' ngựa, bò.']}, 3: {
        'title': 'Câu 28: Công nghiệp luyện kim, cơ khí chế tạo và điện tử…phát triển mạnh ở các quốc gia nào sau đây?',
        'answer': ' Nhật Bản, Trung Quốc, Ấn Độ.',
        'options': [' Nhật Bản, Trung Quốc, Ấn Độ.', ' Trung Quốc, Việt Nam, Mi-an-ma.', ' Ấn Độ, Lào, Cam-pu-chia.',
                    ' Ả- rập Xê-út, Nê-pan, Cam-pu-chia.']},
         4: {'title': 'Câu 29: Ngành công nghiệp nào sau đây phát triển mạnh ở Nhật Bản, Trung Quốc, Ấn Độ, Đài Loan?',
             'answer': ' Điện tử - tin học.',
             'options': [' Sản xuất hàng tiêu dùng.', ' Điện tử - tin học.', ' Chế biến lương thực, thực phẩm.',
                         ' Khai thác và chế biến khoáng sản.']}, 5: {
        'title': 'Câu 30: Công nghiệp sản xuất xuất hàng tiêu dùng phát triển ở các quốc gia, khu vực nào sau đây?',
        'answer': ' Hầu hết các quốc gia.',
        'options': [' Trung Quốc, Nhật Bản, Hàn Quốc.', ' Khu vực Tây Nam Á.', ' Hầu hết các quốc gia.',
                    ' Khu vực Đông Nam Á.']},
         6: {'title': 'Câu 31: Các quốc gia có ngành dịch vụ phát triển mạnh nhất là',
             'answer': ' Nhật Bản, Xin-ga-po, Hàn Quốc.',
             'options': [' Nhật Bản, Xin-ga-po, Hàn Quốc.', ' Trung Quốc, Hàn Quốc, Ấn Độ.',
                         ' Trung Quốc, Ấn Độ, Nhật Bản.', ' Nhật Bản, Hàn Quốc, Đài Loan.']},
         7: {'title': 'Câu 32: Loại khoáng sản xuất khẩu quan trọng nhất của các nước Tây Nam Á và Trung Á là',
             'answer': ' Dầu mỏ.', 'options': [' Than đá.', ' Dầu mỏ.', ' Sắt.', ' Crôm.']}, 8: {
        'title': 'Câu 33: Trung Quốc là nước sản xuất nhiều lúa gạo nhưng sản lượng lương thực xuất khẩu còn thấp chủ yếu do',
        'answer': ' đây là nước đông dân nhất thế giới.',
        'options': [' chất lượng nông sản còn thấp.', ' chủ yếu phục vụ cho chăn nuôi trong nước.',
                    ' đây là nước đông dân nhất thế giới.', ' nhu cầu tiêu thụ gạo trên thế giới ít.']},
         9: {'title': 'Câu 34: Nguyên nhân làm cho vùng khí hậu khô hạn phát triển chăn nuôi dê, cừu, ngựa là',
             'answer': ' đặc điểm sinh thái của vật nuôi.',
             'options': [' thị trường tiêu thụ rộng lớn.', ' đặc điểm sinh thái của vật nuôi.', ' tập quán sản xuất.',
                         ' chính sách phát triển chăn nuôi.']}}
case3 = {
    0: {'title': 'Câu 51: Đồng bằng Ấn – Hằng nằm ở vị trí nào trong khu vực Nam Á?',
        'answer': ' Nằm giữa dãy Hi – ma – lay – a và sơn nguyên Đê – can.',
        'options': [' Nằm giữa dãy Hi – ma – lay – a và sơn nguyên Đê – can.', ' Nằm ở phía bắc.',
                    ' Nằm giữa dãy Gát – tây và dãy Gát – đông.', ' Nằm ở biển A – rap.']},
    1: {'title': 'Câu 52: Ranh giới khí hậu quan trọng giữa hai khu vực Trung Á và Nam Á là',
        'answer': ' dãy Hi-ma-lay-a.',
        'options': [' sông Ấn – Hằng.', ' dãy Hi-ma-lay-a.', ' biển A-rap.', ' dãy Bu-tan.']},
    2: {'title': 'Câu 53: Đại bộ phận Nam Á thuộc kiểu khí hậu nào?', 'answer': ' nhiệt đới gió mùa.',
        'options': [' nhiệt đới gió mùa.', ' cận nhiệt đới gió mùa.', ' ôn đới lục địa.', ' ôn đới hải dương.']},
    3: {'title': 'Câu 54: Dạng địa hình nào sau đây không phổ biến ở Nam Á?', 'answer': ' Đầm lầy.',
        'options': [' Sơn nguyên.', ' Đồng bằng.', ' Núi cao.', ' Đầm lầy.']},
    4: {'title': 'Câu 55: Vai trò của dãy Hi-ma-lay-a trong việc điều tiết khí hậu của khu vực Nam Á là',
        'answer': ' đem lại một mùa đông bớt lạnh hơn và mùa hạ có mưa nhiều ở sườn phía nam.',
        'options': [' đem lại một mùa đông bớt lạnh hơn và mùa hạ có mưa nhiều ở sườn phía nam.',
                    ' đem lại một mùa đông lạnh giá và mùa hạ có gió phơn khô nóng ở sườn phía nam.',
                    ' đem lại một mùa đông lạnh, ẩm, mưa nhiều và mùa hạ ít mưa ở sườn phía bắc.',
                    ' đem lại một mùa đông lạnh, khô và mùa hạ mưa nhiều ở sườn phía nam.']}, 5: {
        'title': 'Câu 56: Nguyên nhân chủ yếu nào làm cho sơn nguyên Đê – can mặc dù nằm gần biển nhưng lại khô hạn, ít mưa?',
        'answer': ' Do bị khuất gió vì kẹp giữa hai dãy núi cao là dãy Gát – tây và dãy Gát – đông.',
        'options': [' Do bị khuất gió vì kẹp giữa hai dãy núi cao là dãy Gát – tây và dãy Gát – đông.',
                    ' Do thuộc kiểu khí hậu nhiệt đới gió mùa ẩm.', ' Do có địa hình tương đối thấp và bằng phẳng.',
                    ' Do có dòng biển lạnh chạy ven bờ.']},
    6: {'title': 'Câu 57: Dân cư Nam Á phân bố nhiều nhất ở khu vực nào sau đây?', 'answer': ' Đồng bằng Ấn – Hằng.',
        'options': [' Sơn nguyên Đê – can.', ' Tây bắc Ấn Độ.', ' Đồng bằng Ấn – Hằng.', ' Ven Ấn Độ Dương.']},
    7: {'title': 'Câu 58: Nam Á có các kiểu cảnh quan nào?',
        'answer': ' Rừng nhiệt đới ẩm, xavan, hoang mạc và cảnh quan núi cao.',
        'options': [' Rừng nhiệt đới ẩm, xavan, hoang mạc và cảnh quan núi cao.',
                    ' Rừng lá kim, xavan, hoang mạc và cảnh quan núi cao.',
                    ' Rừng cận nhiệt đới ẩm, xavan và hoang mạc.', ' Xavan, hoang mạc và cảnh quan núi cao.']},
    8: {'title': 'Câu 59: Quốc gia có nền kinh tế phát triển nhất Nam Á là', 'answer': ' Ấn Độ.',
        'options': [' Pa-ki-xtan.', ' Ấn Độ.', ' Nê-pan.', ' Bu-tan.']},
    9: {'title': 'Câu 60: Hai trung tâm công nghiệp lớn nhất của Ấn Độ là', 'answer': ' Côn-ca-ta và Mum-bai.',
        'options': [' Côn-ca-ta và Mum-bai.', ' Niu Đê-li và Mum-bai.', ' Ma-đrát và Côn –ca-ta.',
                    ' Côn-ca-ta và Niu Đê-li.']},
    10: {'title': 'Câu 61: “Cách mạng trắng” và “Cách mạng xanh” là những cuộc cách mạng về lĩnh vực',
         'answer': ' nông nghiệp.', 'options': [' nông nghiệp.', ' công nghiệp.', ' dịch vụ.', ' du lịch.']},
    11: {'title': 'Câu 62: Quốc gia nào không thuộc Tây Nam Á', 'answer': ' Ấn Độ.',
         'options': [' Cô-oét.', ' Ả rập xê út', ' Ấn Độ.', ' I ran']},
    12: {'title': 'Câu 63: Đặc điểm dân cư – xã hội nào sau đây không đúng với Nam Á?',
         'answer': ' Có lịch sử khai thác lãnh thổ muộn.',
         'options': [' Dân cư tập trung đông nhất châu Á.', ' Có lịch sử khai thác lãnh thổ muộn.',
                     ' Dân cư chủ yếu theo Ấn Độ giáo và Hồi giáo.', ' Tình hình chính trị - xã hội thiếu ổn định.']}}


@pytest.mark.parametrize("test_input, expectation", [
    (r'.\testcases\case1.docx', case1),
    (r'.\testcases\case2.docx', case2),
    (r'.\testcases\case3.docx', case3)
])
def test_converter(test_input, expectation):
    assert questionIdentification(filterer(convertDoc2Txt(test_input))) == expectation
