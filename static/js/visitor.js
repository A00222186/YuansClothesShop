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

function $create(tagName){
	return document.createElement(tagName);
}

/*$(document).ready(
		addvisitor()
);*/

$(document).on("click","#btnGet",function(){readvisitor();
});
