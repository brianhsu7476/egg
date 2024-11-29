var a=document.querySelector('#arctan'), cnt=0;
var b=document.querySelector('#talk');
var c=document.querySelector('#title');
function init(){
	a.innerHTML+='<br>';
	for(var i=0; i<61; ++i)
		a.innerHTML+='<img class="noshow" src="egg'+String(i)+'.png">';
}
function upd(){
	t=['哈哈是我啦！', '偷偷說聖誕節會有驚喜喔！', '大家可以期待一下！'];
	b.innerHTML=t[Math.floor((cnt%183)/61)];
	s=['盛蛋', '盛誕', '聖誕'];
	c.innerHTML='祝大家'+s[Math.floor((cnt%61)/21)]+'快樂';
	a.innerHTML='<img src="egg'+String(cnt%61)+'.png">';
	cnt+=1;
}
init();
function start(){
	b.innerHTML='嘿！你吵到我睡覺了！';
	setTimeout(function(){
		b.innerHTML='只好讓你瞧瞧我的真面目了！';
		setTimeout(function(){
			setInterval(upd, 30);
		}, 3000);
	}, 3000);
}
