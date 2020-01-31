// code是前台程序，它调用cytoscape.min.js在前台生成网络关系图
$(function()//注意js的格式
{
    $.get('/graph', function (result){
        cytoscape({
              container: document.getElementById('cy'),
              style: [
                { selector: 'node',
                  css: {'background-color': '#6FB1FC', 'content': 'data(accountId)'}
                },
                { selector: 'edge',
                  css: {'content': 'data(amount)', 'target-arrow-shape': 'triangle'}
                }
              ],
              elements:result.elements,
              layout: { name: 'cose'}
            });
    }, 'json');// 注意分号


});
// { //用jQuery的$.get('/graph', function(result) {}, 'json')方法从网站后端的’/graph’路径获得JSON数据存在result中
//         var style = [
//             {
//                 selector:"node",
//                 css:{'background-color':'#6FB1FC', "content":"data(accountId)"} // content管理显示的内容
//             },
//             {
//                 selector:'edge',
//                 css:
//                 {
//                 'curve-style': 'bezier',
//                 'target-arrow-shape': 'triangle',
//                 'width': 4,
//                 'line-color': '#ddd',
//                 'target-arrow-color': '#ddd',
//                 'content': 'data(amount)'
//                 }
//             }
//         ]
//         // window.alert(result.elements.edges[0].data.amount);
//
//
//         var cy =window.cy = cytoscape({
//             container:document.getElementById("cy"),
//             style:style,
//             layout:{name:'cose', fit:true}, // layout 网络布局
//             elements:result.elements
//         });
//     }
