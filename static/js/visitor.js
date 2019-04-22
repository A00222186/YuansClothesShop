    var addvisitor = function(){
        console.log("start to add visitor") ;
        $.ajax({
                type:'POST',
                url:'/Websitetraffic/update',
                success:function(){
                     alert("update visitor successful")
                }
        });
    };

    var readvisitor = function(){
        console.log("start to read visitor");
        $.ajax({
                type:'GET',
                url:'/Websitetraffic/read',
				dataType:'json',
                success:function(data){
                    alert("read one week visitors success");
                    showBarchart(data);
                },
                error:function(data) {
					alert("read visitor error");
					alert(data);
				}
        });
    };

    var malevisitor = function(){
        console.log("start to read male visitor");
        $.ajax({
                type:'GET',
                url:'/maleLogin/read',
				dataType:'json',
                success:function(data){
                    alert("read yestarday male visitors success");
                    drawmalepie(data);
                    //malepiechart(data);
                },
                error:function(data) {
					alert("read male visitor error");
					alert(data);
				}
        });
    };
    var femalevisitor = function(){
        console.log("start to read female visitor");
        $.ajax({
                type:'GET',
                url:'/femaleLogin/read',
				dataType:'json',
                success:function(data){
                    alert("read yestarday female visitors success");
                    drawpie(data);
                    //femalepiechart(data);
                },
                error:function(data) {
					alert("read male visitor error");
					alert(data);
				}
        });
    };

    function getColor(){
	//分别随机r g b的值
	    var r = parseInt(Math.random()*256);
	    var g = parseInt(Math.random()*256);
	    var b = parseInt(Math.random()*256);
	    return "#"+r.toString(16)+g.toString(16)+b.toString(16);
}

    function getmaxVisitor(jsonArr){
	let max = jsonArr[0].visitor;
	for(let i=1;i<jsonArr.length;i++){
		if(jsonArr[i].visitor>max){
			max = jsonArr[i].visitor;
		}
	}
	return max;
}
    function showBarchart(data){
	//1、明确最大高度和最大金额
	let maxWidth = 800;
	let maxHeight = 450;
	let maxVisitor = getmaxVisitor(data);
	//2、计算比例(一万元多少像素)
	percent = maxHeight/maxVisitor;

	//3、柱子之间的间隔和柱子的宽度(假定柱子的间隔和宽度是一样的)
	let space = maxWidth/(data.length*2+1);
	let width = space;

	//循环所有的数据产生柱状图
	for(let i=0;i<data.length;i++){
		//1、创建大div（包着金额，颜色柱子，年份）
		let bigPillarDom = document.createElement("div");
		let left = (i+1)*space+i*width;
		bigPillarDom.style.cssText = "position:absolute;left:"+left+"px;bottom:-20px;width:50px;";
		$("#box").append(bigPillarDom);
		//2、创建年份，颜色柱子，金额对应dom元素。
		//1）、创建金额的span
		let spanMoneyDom = $create("span");
		spanMoneyDom.style.cssText = "text-align:center;width:"+width+"px;display:block;";
		spanMoneyDom.innerHTML = data[i].visitor+"";
		bigPillarDom.append(spanMoneyDom);
		//2)、创建颜色柱子的div
		let divColorDom = $create("div");
		divColorDom.style.width=width+"px";
		divColorDom.style.height=(data[i].visitor*percent)+"px";
		divColorDom.style.backgroundColor = getColor();
		bigPillarDom.append(divColorDom);
		//3)、创建年份的p
		let pYearDom = $create("p");
		pYearDom.innerHTML = data[i].day+"/"+data[i].month;
		pYearDom.style.cssText ="height:20px;text-align:center;";
		bigPillarDom.append(pYearDom);
	}
}

function getsum(data){
    	var sum = 0;
	for(var i=0;i<data.length;i++){
		sum+=data[i].num;
	};
	return sum;
}
	function lastSum(data,i){
	var lastsum = 0;//重置为0
	for (var j = 0; j < i; j++) {
		lastsum+=data[j].num;
	};
	return lastsum;
}

function drawpie(data) {
	var c = document.getElementById("female");
	var ctx = c.getContext("2d");
	var radius = c.height / 2 - 20; //半径
	var ox = radius + 20, oy = radius + 20; //圆心

	var colors=["#cb3f35","#fee535","#57b8ff"];

	var width = 30, height = 10; //图例宽和高
	var posX = ox * 2 + 20, posY = 30;   //
	var textX = posX + width + 5, textY = posY + 10;

	var startAngle = 0; //起始弧度
	var endAngle = 0;   //结束弧度
	var sum = getsum(data);//统计全部数据用以计算比例

	for (var i = 0; i < data.length; i++) {
		//绘制饼图
		endAngle = endAngle + (data[i].num/sum) * Math.PI * 2; //结束弧度
		ctx.fillStyle = colors[i];
		ctx.beginPath();
		ctx.moveTo(ox, oy); //移动到到圆心
		ctx.arc(ox, oy, radius, startAngle, endAngle, false);
		ctx.closePath();
		ctx.fill();
		startAngle = endAngle; //设置起始弧度

		//绘制比例图及文字
		ctx.fillStyle = colors[i];
		ctx.fillRect(posX, posY + 20 * i, width, height);
		ctx.moveTo(posX, posY + 20 * i);
		ctx.font = 'bold 12px 微软雅黑';    //斜体 30像素 微软雅黑字体
		ctx.fillStyle = colors[i]; //"#000000";
		var percent = data[i].name + "：" + parseInt((data[i].num/sum)*10000/100) + "%";
		ctx.fillText(percent, textX, textY + 20 * i);
	}

}

function drawmalepie(data) {
	var c = document.getElementById("male");
	var ctx = c.getContext("2d");
	var radius = c.height / 2 - 20; //半径
	var ox = radius + 20, oy = radius + 20; //圆心

	var colors=["#74c4cb","#fef36d","#e665ff"];

	var width = 30, height = 10; //图例宽和高
	var posX = ox * 2 + 20, posY = 30;   //
	var textX = posX + width + 5, textY = posY + 10;

	var startAngle = 0; //起始弧度
	var endAngle = 0;   //结束弧度

		var sum = getsum(data);

	for (var i = 0; i < data.length; i++) {
		//绘制饼图
		endAngle = endAngle + (data[i].num/sum) * Math.PI * 2; //结束弧度
		ctx.fillStyle.colo = colors[i];
		ctx.beginPath();
		ctx.moveTo(ox, oy); //移动到到圆心
		ctx.arc(ox, oy, radius, startAngle, endAngle, false);
		ctx.closePath();
		ctx.fill();
		startAngle = endAngle; //设置起始弧度

		//绘制比例图及文字
		ctx.fillStyle = colors[i];
		ctx.fillRect(posX, posY + 20 * i, width, height);
		ctx.moveTo(posX, posY + 20 * i);
		ctx.font = 'bold 12px 微软雅黑';    //斜体 30像素 微软雅黑字体
		ctx.fillStyle = colors[i]; //"#000000";
		var percent = data[i].name + "：" + parseInt((data[i].num/sum)*10000/100) + "%";
		ctx.fillText(percent, textX, textY + 20 * i);
	}

}
function malepiechart(data){
var radius=200;
var colors=["#cb3f35","#fee535","#57b8ff"];
	var c = document.getElementById("male");
	var ctx = c.getContext("2d");
	var sum =getsum(data);

	for (var i = 0; i < data.length;i++) {
		var lastsum = lastSum(data,i);//上一个结束弧度就是下一个起始弧度
		var startAngle= (Math.PI*2)*(lastsum/sum);//起始弧度
		var llaastsum=lastSum(data,i);
		var endAngle=(Math.PI*2)*(llaastsum/sum);//结束弧度
		ctx.save();
		ctx.fillStyle=colors[i];
		ctx.beginPath();
		ctx.moveTo(400,400);
		ctx.arc(400,400,radius,startAngle,endAngle,false);
		ctx.closePath();
		ctx.fill();
		ctx.restore();
		drawText(c,radius,startAngle,endAngle,data[i].name,data[i].num/sum);
	};
}
function femalepiechart(data){
var radius=200;
var colors=["#6bcb84","#fe2f2f","#e665ff"];
	var c = document.getElementById("female");
	var ctx = c.getContext("2d");
	var sum =getsum(data);

	for (var i = 0; i < data.length;i++) {
		var lastsum = lastSum(data,i);//上一个结束弧度就是下一个起始弧度
		var startAngle= (Math.PI*2)*(lastsum/sum);//起始弧度
		var llaastsum=lastSum(data,i);
		var endAngle=(Math.PI*2)*(llaastsum/sum);//结束弧度
		ctx.save();
		ctx.fillStyle = colors[i];
		ctx.beginPath();
		ctx.moveTo(400,400);
		ctx.arc(400,400,radius,startAngle,endAngle,false);
		ctx.closePath();
		ctx.fill();
		ctx.restore();
		drawText(c,radius,startAngle,endAngle,data[i].name,data[i].num/sum);
	};
}
function drawText(c,radius,s,e,jn,jsm){
    	var ctx = c.getContext("2d");
	//文字的x，y坐标计算
		var x = Math.cos((s+e)/2)*(radius+60)+400;
		var y = Math.sin((s+e)/2)*(radius+60)+400;
		ctx.fillStyle="blue";
		ctx.fillText(jn,x,y);
		ctx.fillStyle="red";
	//百分比精确到小数后两位
		ctx.fillText((parseInt(jsm*10000)/100)+"%",x,y+20);
	//绘制由每个饼指向文字的线段
		ctx.beginPath();
	//各端点坐标由每块的起始弧度和结束弧度求平均后计算得出
		ctx.moveTo(Math.cos((s+e)/2)*radius+400,Math.sin((s+e)/2)*radius+400);
		ctx.lineTo( Math.cos((s+e)/2)*(radius+40)+400, Math.sin((s+e)/2)*(radius+40)+400);
		ctx.closePath();
		ctx.fillStyle="red";
		ctx.stroke();
}

function $create(tagName){
	return document.createElement(tagName);
}


$(document).on("click","#btnGet",function(){readvisitor();
});

    $(document).on("click","#btnGetLogin",function(){
    	malevisitor();
    	femalevisitor();
});
