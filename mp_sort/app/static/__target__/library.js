// Transcrypt'ed from Python, 2022-09-22 15:16:17
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var insertion_sort = function (array_list) {
	for (var outer_index = 1; outer_index < len (array_list); outer_index++) {
		var inner_index = outer_index;
		while (inner_index > 0 && array_list [inner_index] < array_list [inner_index - 1]) {
			var __left0__ = tuple ([array_list [inner_index], array_list [inner_index - 1]]);
			array_list [inner_index - 1] = __left0__ [0];
			array_list [inner_index] = __left0__ [1];
			inner_index--;
		}
	}
	return array_list;
};
export var gen_random_int = function (number, seed) {
	var array = (function () {
		var __accu0__ = [];
		for (var i = 0; i < number; i++) {
			__accu0__.append (i);
		}
		return __accu0__;
	}) ();
	random.seed (seed);
	random.shuffle (array);
	return array;
};
export var convert_list_str_to_int = function (array) {
	var array_l = (function () {
		var __accu0__ = [];
		for (var i = 0; i < len (array); i++) {
			__accu0__.append (int (array [i]));
		}
		return __accu0__;
	}) ();
	return array_l;
};
export var gen_list_of_str = function (array) {
	var array_str = ''.join ((function () {
		var __accu0__ = [];
		for (var i of array) {
			__accu0__.append ('{},'.format (str (i)));
		}
		return py_iter (__accu0__);
	}) ());
	var array_str = array_str.__getslice__ (0, -(1), 1) + '.';
	return array_str;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	var array = gen_random_int (number, seed);
	var array_str = gen_list_of_str (array);
	document.getElementById ('generate').innerHTML = array_str;
};
export var sortnumber1 = function () {
	var array = document.getElementById ('generate').innerHTML;
	var array = array.rstrip ('.');
	var array_list_str = array.py_split (',');
	var array_list_int = convert_list_str_to_int (array_list_str);
	var sorted_list = insertion_sort (array_list_int);
	var array_str = gen_list_of_str (sorted_list);
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sortnumber2 = function () {
	var value = document.getElementsByName ('numbers') [0].value;
	if (value == '') {
		window.alert ('Your textbox is empty');
		// pass;
	}
	else {
		var array_list_str = value.py_split (',');
		var array_list_int = convert_list_str_to_int (array_list_str);
		var sorted_list = insertion_sort (array_list_int);
		var array_str = gen_list_of_str (sorted_list);
	}
	document.getElementById ('sorted').innerHTML = array_str;
};

//# sourceMappingURL=library.map