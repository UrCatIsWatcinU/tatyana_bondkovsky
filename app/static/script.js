const TRANSITION_DURATION = 1200;

//drop menu in menu block
let dropMenuState = 0;

function showDropMenu() {
    let menuPoints = document.querySelector(".menu-cont__points"); 

    if(!dropMenuState){
        dropMenuState = 1
        menuPoints.style.display = 'flex';
        setTimeout(() => {menuPoints.style.opacity = '0.97';}, 1)
        return;
    } else{
        dropMenuState = 0
        menuPoints.style.opacity = '0';
        setTimeout(() => {menuPoints.style.display = 'none'}, TRANSITION_DURATION);
        return;
    }
};

function hideDropMenu(){
    if(window.matchMedia('(max-width: 450px)').matches){
        let menuPoints = document.querySelector(".menu-cont__points");
        menuPoints.style.opacity = '0';
        setTimeout(function(){menuPoints.style.display = 'none'}, TRANSITION_DURATION);
    };    
};


//more text in about block
let state_moreTxt = 0;

function showMoreTxt(){
    let moreTxt = document.querySelector('.about-cont__moretxt');
    let txt = document.querySelector('.about-cont__txt');

    if (!state_moreTxt) {
        state_moreTxt = 1;
        txt.style.maxHeight = '850px';
        txt.style.paddingBottom = '47px';
        setTimeout(() => {
            moreTxt.classList.add('about-cont_lesstxt');
            moreTxt.innerHTML = 'Свернуть';            
        }, TRANSITION_DURATION);     
        return;
    } else {
        state_moreTxt = 0;
        txt.style.maxHeight = '350px';
        moreTxt.style.cssText = '';
        setTimeout(() => {
            moreTxt.classList.remove('about-cont_lesstxt'); 
            moreTxt.innerHTML = 'Подробнее'
        }, TRANSITION_DURATION);
        return;
    };
};


function scroll(cls) {
    jQuery(document).ready(function () {
        jQuery(cls).click(function () {
            elementClick = jQuery(this).attr("href");
            destination = jQuery(elementClick).offset().top - 150;
            jQuery("html:not(:animated),body:not(:animated)").animate({ scrollTop: destination }, 900);
            return false;
        });
    });
};

scroll('a.menu-cont__point')
scroll('a.contacts-cont__txt')
scroll('.course-card__price')


window.addEventListener('scroll', function() {
    let menu = document.querySelector('.menu-cont');
    let header = document.querySelector('.header-cont');

    if(pageYOffset > 130){
        menu.style.cssText =('animation: fixed 1s cubic-bezier(1,.01,.16,.89);position: fixed;z-index: 3;opacity: 0.9;top: 0px;');
        header.style.cssText =('margin-bottom:50px');
    }
    else{
        menu.style.cssText =('position:static;');
        header.style.cssText =('margin-bottom:0px');
    };
    
    function showShad(elem, scroll, right = 0){
        if(right === 0){
            if (pageYOffset > scroll && pageYOffset < scroll + 500){
                document.querySelector(elem).style.transform = 'translate(-3px, -3px)';
                document.querySelector(elem).style.boxShadow = '4px 4px 10px rgba(42, 42, 42, 0.4)';         
            }else{
                document.querySelector(elem).style.transform = 'none';
                document.querySelector(elem).style.boxShadow = 'none';         
            };
        }else{
            if (pageYOffset > scroll && pageYOffset < scroll + 500){
                document.querySelector(elem).style.transform = 'translate(3px, -3px)';
                document.querySelector(elem).style.boxShadow = '-4px 4px 10px rgba(42, 42, 42, 0.4)';         
            }else{
                document.querySelector(elem).style.transform = 'none';
                document.querySelector(elem).style.boxShadow = 'none';         
            };
        };           
    };
    
    if(window.matchMedia('(min-width: 1160px)').matches){
        showShad('.advantages-cont_1', 2200)
        showShad('.advantages-cont_2', 2600, 1)
        showShad('.advantages-cont_3', 3000)
        
        if (document.getElementById('how').getBoundingClientRect().top < 300){
            document.querySelector('.how-cont__content').classList.add('how-cont_line')       
        };
        if(document.getElementById('how').getBoundingClientRect().top > 700){
            document.querySelector('.how-cont__content').classList.remove('how-cont_line')
        };   
    };  
});


// window.addEventListener('scroll', function() {
//     document.getElementById('scroll').innerHTML = document.getElementById('scroll').getBoundingClientRect().top + 'px';    
// });


