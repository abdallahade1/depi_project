INSERT INTO Feedback_Aggregated  
    (Book_id, Total_Reviews, Average_Score, Positive_Reviews, Negative_Reviews, Review_id, Review_text, Review_summary, Review_time, User_id, Title, Price)
--SELECT 
--    b.Book_id,
--    COUNT(r.review_id) AS Total_Reviews,
--    AVG(r.review_score) AS Average_Score,
--    SUM(CASE WHEN r.review_score >= 4 THEN 1 ELSE 0 END) AS Positive_Reviews,
--    SUM(CASE WHEN r.review_score <= 2 THEN 1 ELSE 0 END) AS Negative_Reviews,
--    STRING_AGG(r.review_id, ', ') AS Review_id,
--    STRING_AGG(r.review_text, '; ') AS Review_text,
--    STRING_AGG(r.review_summary, '; ') AS Review_summary,
--    MAX(r.review_time) AS Review_time,
--    STRING_AGG(r.user_id, ', ') AS User_id,
--    b.Title,
--    b.Price
--FROM 
--    Customerfeedback.dbo.reviews r
--JOIN 
--    Customerfeedback.dbo.books b ON CAST(r.book_id AS INT) = b.Book_id
--GROUP BY 
--    b.Book_id, b.Title, b.Price
--HAVING 
--    COUNT(r.review_id) > 0;

--SELECT DISTINCT r.book_id
--FROM Customerfeedback.dbo.reviews r
--WHERE TRY_CAST(r.book_id AS INT) IS NULL
--AND r.book_id IS NOT NULL;

--DELETE FROM Customerfeedback.dbo.reviews
--WHERE TRY_CAST(book_id AS INT) IS NULL;

select * from Feedback_Aggregated
