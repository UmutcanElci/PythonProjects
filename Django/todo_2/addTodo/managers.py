from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username,email,password):
        if not username:
            raise ValueError("Kullanıcı adı gereklidir.")
        if not email:
            raise ValueError("Email gereklidir.")
        if not password:
            raise ValueError("Şifre gereklidir")
        
        email = self.normalize_email(email)
        user = self.model(username=username,email=email , password= password)
        user.set_password(password)
        user.save()
        return user