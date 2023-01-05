-- UPDATE user SET password = password('myPa$$word') WHERE user = 'root';
-- set password for 'root'@'localhost' = password('mypassword');

-- select count(*) from daily_price;
-- CREATE VIEW pricecount AS SELECT code, count(*) as cnt from daily_price group by code;




--  not in (select code from daily_price);


select A.code from company_info A left OUTER JOIN pricecount B on A.code = B.code where B.code is NULL;