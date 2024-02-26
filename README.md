
#  metric_shopee_crawler_demo

  

 - **Cài đặt venv**

	    python3 -m venv .

 - **Activate venv**

	- **Linux/MacOS**

			source bin/activate

	- **Windows**

		    Scripts/activate

 - **Cài đặt requirements**
		
		pip install -r requirements.txt

 - **Chạy chương trình**
 
		python crawler.py
	
	Ghi chú trong file crawler.py

 - **Kết luận**
 Do các hạn chế của Shopee đặt ra nhằm ngăn chặn crawler lấy dữ liệu từ website của họ trong những tuần qua. Crawler áp dụng các cách thức phổ thông hoạt động không thành công như kỳ vọng. Cần dành nhiều thời gian hơn để tìm giải pháp mới.
	- Tham khảo:
	 [https://stackoverflow.com/questions/76936341/shopee-api-to-get-products-data-doesnt-seem-to-work-anymore-it-worked-before/78059531#78059531](https://stackoverflow.com/questions/76936341/shopee-api-to-get-products-data-doesnt-seem-to-work-anymore-it-worked-before/78059531#78059531)
		[https://stackoverflow.com/questions/78054805/scraping-products-from-shopee-using-python-requests-returns-90309999/78054996#78054996](https://stackoverflow.com/questions/78054805/scraping-products-from-shopee-using-python-requests-returns-90309999/78054996#78054996)
		
	- Những hạn chế khác có thể xảy ra làm chương trình không hoạt động như kỳ vọng:
		- Hạn chế về phần cứng
		- Hạn chế của script do được phát triển vội vàng 
		- Hiểu biết về website của người phát triển chưa được rõ ràng