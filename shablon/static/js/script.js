document.addEventListener('DOMContentLoaded', function(){

    document.getElementById('logIn_link').addEventListener('click', function (e) {
        e.preventDefault();
        e = e.target;

        var hideBlock = document.getElementById('logIn_hideBlock');

        // console.log(x);
        if( hideBlock.clientHeight === 0){
            hideBlock.style.visibility = 'visible';
            hideBlock.style.height = '300px';
        }else{
            hideBlock.style.visibility = 'hidden';
            hideBlock.style.height = '0px';
        }
    })


});
