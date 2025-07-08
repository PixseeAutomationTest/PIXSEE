eamil="com.compal.bioslab.pixsee.pixm01:id/signInEmailField"
email_address="amypixsee02@gmail.com"
password="com.compal.bioslab.pixsee.pixm01:id/signInPasswordField"
password_address="@Aa12345"
signid="com.compal.bioslab.pixsee.pixm01:id/btSignIn"
app="com.compal.bioslab.pixsee.pixm01"
driver= ""

class Count:
    def __init__(self):
       pass
    def sum(self,a,b):
        ans=a+b
        print(ans)
    def subtract(self,a,b):
        ans=a-b
        print(ans)
    def multiply(self,a,b):
        ans=a*b
        print(ans)
    def divide(self,a,b):
        ans = a / b
        print(ans)
a=int(input("num1:"))
b=int(input("num2:"))
count=Count()
count.divide(a,b)