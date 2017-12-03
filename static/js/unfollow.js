function unfollow(username){
    var req = new XMLHttpRequest();
    req.open("POST", "unf", true);
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    req.send("unfollow=" + username);
    console.log(req.responseText);
    unfbtn = document.getElementById("butten-unf-" + username);
    unfbtn.innerHTML = "Unfollowed";
    unfbtn.setAttribute("disabled", "true");
}
