-- 코드를 입력하세요
SELECT b.title, b.board_id, p.reply_id, p.writer_id, p.contents, p.created_date
from used_goods_board b,used_goods_reply p
where (b.board_id = p.board_id) and b.created_date like "2022-10%"
order by p.created_date, b.title;