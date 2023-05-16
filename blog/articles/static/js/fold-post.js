var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++)
{
    foldBtns[i].addEventListener("click", function(e) { 
        if (e.target.parentElement.parentElement.className == "one-post folded"){
        e.target.parentElement.parentElement.className = "one-post";
        e.target.className == "fold-button"; 
        }
        else{
        e.target.innerHTML = "развернуть"; 
        e.target.parentElement.parentElement.className = "one-post folded";
        }
        });
}