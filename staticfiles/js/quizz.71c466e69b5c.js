var skip = document.getElementById('skip');
var score = document.getElementById('score');
var totalScore = document.getElementById('totalScore');
var countdown = document.getElementById('countdown');
var count = 0;
var scoreCount = 0;
var duration = 0;
var qSet= document.querySelectorAll('.quizz_set');
var qAns= document.querySelectorAll('.quizz_set .quizz_ans input');

skip.addEventListener('click',function(){
    step();
    duration =15;
})

qAns.forEach(function(qAnsSingle){
    qAnsSingle.addEventListener('click',function(){
        setTimeout(function(){
            step();
            duration = 15;
        },500)

    var valido = this.getAttribute("valid");
    if(valido == "valid"){
        scoreCount += 20;
        score.innerHTML = scoreCount;
        totalScore.innerHTML = scoreCount;
    }else{
        scoreCount -= 20;
        score.innerHTML = scoreCount;
        totalScore.innerHTML = scoreCount;
    }
    })
});

function step(){
    count+=1;
    for(var i=0;i<qSet.length;i++){
        qSet[i].className='quizz_set';
    }
    qSet[count].className = 'quizz_set active';
    if(count == 5){
        skip.style.display = 'none';
        clearInterval(durationTime);
        countdown.innerHTML = 0;
    }
}

var durationTime = setInterval(function(){
    if(duration == 15){
        duration = 0;
    }
    duration +=1;
    countdown.innerHTML=duration;
    if(countdown.innerHTML == "15"){
        step();
    }
},1000);