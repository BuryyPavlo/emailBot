To allow authentication you first need to register your application at Azure App Registrations.
1 Login at Azure Portal (App Registrations)
2 Create an app. Set a name.
3 In Supported account types choose "Accounts in any organizational directory and personal Microsoft accounts (e.g. Skype, Xbox, Outlook.com)",
  if you are using a personal account.
4 Set the redirect uri (Web) to: https://login.microsoftonline.com/common/oauth2/nativeclient and click register.
  This needs to be inserted into the "Redirect URI" text box as simply checking the check box next to this link seems to be insufficent.
  This is the default redirect uri used by this library, but you can use any other if you want.
5  Write down the Application (client) ID. You will need this value.
6 Under "Certificates & secrets", generate a new client secret. Set the expiration preferably to never.
  Write down the value of the client secret created now. It will be hidden later on.
7 Under Api Permissions:
    When authenticating "on behalf of a user":
      add the delegated permissions for Microsoft Graph you want (see scopes)
      it is highly recommended to add "offline_access" permission. If not the user you will have to re-authenticate every hour.
    When authenticating "with your own identity":
      add the application permissions for Microsoft Graph you want
      click on the Grant Admin Consent button (if you have admin permissions) or wait until the admin has given consent to your application
As an example, to read and send emails use:
  Mail.ReadWrite
  Mail.Send
  User.Read
