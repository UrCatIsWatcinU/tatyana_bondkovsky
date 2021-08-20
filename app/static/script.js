function isIOS() {
    return [
      'iPad Simulator',
      'iPhone Simulator',
      'iPod Simulator',
      'iPad',
      'iPhone',
      'iPod'
    ].includes(navigator.platform)
    // iPad on iOS 13 detection
    || (navigator.userAgent.includes("Mac") && "ontouchend" in document)
}

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

function showShad(elem, right = 0){
    if(typeof(elem) == 'string') elem = document.querySelector(elem);
    const scroll =  elem.getBoundingClientRect().top + pageYOffset - document.documentElement.clientHeight / 2;
    if(right === 0){
        if (pageYOffset > scroll && pageYOffset < scroll + elem.offsetHeight){
            elem.style.transform = 'translate(-3px, -3px)';
            elem.style.boxShadow = '4px 4px 10px rgba(42, 42, 42, 0.2)';         
        }else{
            elem.style.transform = 'none';
            elem.style.boxShadow = 'none';         
        };
    }else{
        if (pageYOffset > scroll && pageYOffset < scroll + elem.offsetHeight){
            elem.style.transform = 'translate(3px, -3px)';
            elem.style.boxShadow = '-4px 4px 10px rgba(42, 42, 42, 0.2)';         
        }else{
            elem.style.transform = 'none';
            elem.style.boxShadow = 'none';         
        };
    };           
};

window.addEventListener('scroll', function() {
    let menu = document.querySelector('.menu-cont');
    let header = document.querySelector('.header-cont');

    if(pageYOffset > 130){
        menu.style.cssText =('animation: fixed 1s cubic-bezier(1,.01,.16,.89); position: fixed; z-index: 3; opacity: 0.9; top: 0px;');
        header.style.cssText =('margin-bottom:50px');
    }
    else{
        menu.style.cssText =('position:static;');
        header.style.cssText =('margin-bottom:0px');
    };
    
    
    showShad('.advantages-cont_1')
    showShad('.advantages-cont_2', 1)
    showShad('.advantages-cont_3')
    if(window.matchMedia('(min-width: 1160px)').matches){
        
        if (document.getElementById('how').getBoundingClientRect().top < 300){
            document.querySelector('.how-cont__content').classList.add('how-cont_line')       
        };
        if(document.getElementById('how').getBoundingClientRect().top > 700){
            document.querySelector('.how-cont__content').classList.remove('how-cont_line')
        };   
    };  
});


window.onload = () => {
    document.querySelectorAll('.menu-cont__point').forEach(link => {
        link.addEventListener('click', evt => {
            evt.preventDefault();
            
            const block = document.querySelector(`#${link.getAttribute('href').split('#')[1]}`);
            if(!block) return;
            
            const rect = block.getBoundingClientRect();
            
            const neededY = rect.top + document.documentElement.scrollTop - document.querySelector('.menu-cont').offsetHeight - 10;
            
            if(isIOS()){
                document.documentElement.style.scrollBehavior = 'auto';

                let startY = document.documentElement.scrollTop;
                const SPEED = .04;
                const oneStepY = (neededY - startY) * SPEED;
                console.log(neededY); 
                
                let previousY = document.documentElement.scrollTop;
                
                const changeScrollY = () => {
                    if(
                        Math.round(document.documentElement.scrollTop) != Math.round(previousY) ||    
                        (neededY > startY && neededY - document.documentElement.scrollTop <= 0) ||
                        (neededY < startY && neededY - document.documentElement.scrollTop >= 0)
                    ) return;
                    
                    document.documentElement.scrollTop += oneStepY;
                    previousY = document.documentElement.scrollTop;
                    
                    requestAnimationFrame(changeScrollY);
                }
                requestAnimationFrame(changeScrollY);
            }else{
                window.location.hash = block.id;
                document.documentElement.scrollTop = neededY;
            }
        }, { passive: false })
    
    })
}