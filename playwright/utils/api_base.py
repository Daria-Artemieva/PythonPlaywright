from playwright.sync_api import Playwright
order_payload = {"orders": [{"country": "Ukraine", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}



class APIUtils:

    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",
                                 data={"userEmail": "123bug456report@gmail.com", "userPassword": "Coco2004!"})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]


    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = order_payload,
                                 headers={"Authorization": token,
                                     "Content-Type": "application/json"})
        print(response.json())
        response_body = response.json()
        order_id =  response_body["orders"][0]
        return order_id