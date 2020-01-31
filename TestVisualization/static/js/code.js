// code是前台程序，它调用cytoscape.min.js在前台生成网络关系图
$(function()//注意js的格式
{
    $.get('/graph', function (result) { //用jQuery的$.get('/graph', function(result) {}, 'json')方法从网站后端的’/graph’路径获得JSON数据存在result中
        var style = [
            {
                selector:"node",
                css:{'background-color':'#6FB1FC', "content":'data(AccountId)'} // content管理显示的内容
            },
        ];

        var cy = cytoscape({
            container:document.getElementById('cy'),
            style:style,
            layout:{
                name:'cose',
                fit:false,
            }, // layout 网络布局
            elements:result.elements
        });
    }, 'json');// 注意分号
});

//数据格式
//              elements: {
//                 nodes: [
//                   {data: {id: '172', name: 'Tom Cruise', label: 'Person'}},
//                   {data: {id: '183', title: 'Top Gun', label: 'Movie'}}
//                 ],
//                 edges: [{data: {source: '172', target: '183', relationship: 'Acted_In'}}]
//               },

