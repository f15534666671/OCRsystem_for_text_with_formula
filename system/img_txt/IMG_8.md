注意到 …愉 先影响到第 立 个输出层神经元的愉入值 庸 1…更JL姜茎薯)翼蓼‖向至U其熹渝出值壹j ,
ERROR
$$
\frac { \partial E _ { k } } { \partial w _ { h j } } = \frac { \partial E _ { k } } { \partial \hat { y } _ { j } ^ { k } } \cdot \frac { \partial \hat { y } _ { j } ^ { k } } { \partial \beta _ { j } } \cdot \frac { \partial \beta _ { j } } { \partial w _ { h j } }
$$
根据 姥 的定义， 显然有
$$
\frac { \partial \beta _ { j } } { \partial w _ { h j } } = b _ { h }
$$
图 5.2 中的 Sigm0id 函数有一个很好的性质:
$$
f ^ { \prime } ( x ) = f ( x ) ( 1 - f ( x ) )
$$
于是根据式恤缈和侣蹦 有
$$
g _ { j } = - \frac { \partial E _ { k } } { \partial \hat { y } _ { j } ^ { k } } \cdot \frac { \partial \hat { y } _ { j } ^ { k } } { \partial \beta _ { j } }
$$
$$
= - ( \hat { y } _ { j } ^ { k } - y _ { j } ^ { k } ) f ^ { \prime } ( \beta _ { j } - \theta _ { j } )
$$
$$
= \hat { y } _ { j } ^ { k } ( 1 - \hat { y } _ { j } ^ { k } ) ( y _ { j } ^ { k } - \hat { y } _ { j } ^ { k } )
$$
将式(5.10)禾口(5.8〉代入式〈5.7)， 再代入式(5.6〉， 就得到了BP 算法中关于
刨脯 的更新公式
$$
\Delta w _ { h j } = \eta g _ { j } b _ { h }
$$

$$
\Delta \theta _ { j } = - \eta g _ { j }
$$
$$
\Delta v _ { i h } = \eta e _ { h } v
$$
$$
\Delta \gamma _ { h } = - \eta e _ { h }
$$
式(5′13)和(5'14)中
$$
e _ { h } = - \frac { \partial E _ { k } } { \partial b _ { h } } \cdot \frac { \partial b _ { h } } { \partial \alpha _ { h } }
$$
$$
= - \sum _ { j = 1 } ^ { l } \frac { \partial E _ { k } } { \partial \beta _ { j } } \cdot \frac { \partial \beta _ { j } } { \partial b _ { h } } f ^ { \prime } ( \alpha _ { h } - \gamma _ { h } )
$$
