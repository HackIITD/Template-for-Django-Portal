var data = {         
 "background_change":function(){
   $("html body").css("background-color","#ffe082");
   $("nav").css("background-color","#f57f17");
 },
 "ListJS":function(){
   var options = {
  valueNames: [ '#', '#' ]
};

var userList = new List('#', options);
 },
  "Basehtmljs":function(){
      $(".Text").typed({
        strings: ["Hello Pokemon Geeks ","Presenting","Pokemon Kingdom" ,"Are you ready ?","So Count","3","2","1","Let's  The Battel  Begin !"],
        typeSpeed: 30, // typing speed
            backDelay: 750,
      });
 

  }
};
$(document).ready(function(){
  data.background_change() ;
  data.Basehtmljs() ;
});