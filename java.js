$(document).ready(function(){
   $("#btn").click(function(){
      $('html, body').animate({
        scrollTop: $("#report").offset().top
      }, 1000);
   });
});

$(document).ready(function(){
   $("#btn1").click(function(){
      $('html, body').animate({
        scrollTop: $("#fore_title").offset().top
      }, 1000);
   });
});

function show() {
   document.getElementById('charts').style.display = "block";
}

function showx() {
   document.getElementById('xporeport').style.display = "block";
   document.getElementById('maerskreport').style.display = "none";
   document.getElementById('knreport').style.display = "none";
   
}

function showm(){
   document.getElementById('maerskreport').style.display = "block";
   document.getElementById('knreport').style.display = "none";
   document.getElementById('xporeport').style.display = "none";
}

function showk(){
   document.getElementById('knreport').style.display = "block";
   document.getElementById('xporeport').style.display = "none";
   document.getElementById('maerskreport').style.display = "none";
}

const uploadInput = document.getElementById("csv-upload");
const customTxt = document.getElementById("file-name");
const customBtn = document.getElementById("bt");

customBtn.addEventListener("click", function(){
   uploadInput.click()
});

// uploadInput.addEventListener("change", function(){
//    if(uploadInput.value){
//       customTxt.innerHTML = uploadInput.value.match( /[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
//    } else{
//       customTxt.innerHTML = "No file chosen";
//    }
// });
