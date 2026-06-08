-- 1. En cok siparis veren kullanici
SELECT u.name, COUNT(*) AS siparis_sayisi
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
ORDER BY siparis_sayisi DESC
LIMIT 1;