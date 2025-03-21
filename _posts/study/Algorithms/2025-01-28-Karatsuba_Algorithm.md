---
title: Karatsuba Algorithm
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Karatsuba Algorithm

### Before Gettign Into Karatsuba Algorithm

When I was a graduate student, I worked on a project related to Addition, Subtraction, Division, and Multiplication operations. The focus was on how to perform each operation more efficiently, primarily from a hardware perspective (including topics like adding multiplexers).

Let's first examine example code for Addition, Subtraction, and Multiplication. These are implemented in C++, with the assumption that the first digit is always larger than the second digit. The key characteristic is that all operations are handled as strings.

Addition
```c++
string Add(string str1, string str2)
{
	if (!str1.size() && !str2.size())
		return "0";

	int N = max(str1.size(), str2.size());
	str1 = string(N - str1.size(), '0') + str1;
	str2 = string(N - str2.size(), '0') + str2;

	string result(N, '0');
	int carry = 0;
	for (int i = N - 1; i >= 0; i--)
	{
		int n1 = str1[i] - '0';
		int n2 = str2[i] - '0';

		int sum = n1 + n2 + carry;

		carry = sum / 10;
		result[i] = char(sum % 10 + '0');
	}

	if (carry > 0)
	{
		result.insert(0, string(1, carry + '0')); // carry insert '1'
	}

	return result;
}
```

I have performance metrics for this code based on N. Considering the time complexity, it's approximately T(N) ≈ N. Of course, when an insert occurs, there might be a constant factor multiplied.

Subtraction
```c++
string Subtract(string str1, string str2)
{
	if (!str1.size() && !str2.size())
		return "0";

	int N = max(str1.size(), str2.size());
	str1 = string(N - str1.size(), '0') + str1;
	str2 = string(N - str2.size(), '0') + str2;

	string result(N, '0');
	int carry = 0;
	for (int i = N - 1; i >= 0; i--)
	{
		int n1 = str1[i] - '0';
		int n2 = str2[i] - '0';

		int sum = n1 - n2 + carry + 10;
		carry = sum / 10;
		result[i] = char(sum % 10 + '0');
		carry -= 1;
	}

	if (result[0] == '0')
	{
		result.replace(0, 1, "");
	}

	return result;
}
```

Similarly, I have performance metrics for this code based on N. The time complexity is approximately T(N) ≈ N. 

Multiplication
```c++
string Multiply(string str1, string str2)
{
	if (!str1.size() && !str2.size())
		return "0";


	int N = max(str1.size(), str2.size());
	str1 = string(N - str1.size(), '0') + str1;
	str2 = string(N - str2.size(), '0') + str2;

	string result(2 * N, '0');

	for (int i = N - 1; i >= 0; i--)
	{ 
		int carry = 0;
		int n1 = str1[i] - '0';
		int k = N + i;
		for (int j = N - 1; j >= 0; j--)
		{
			int n2 = str2[j] - '0';
			int sum = n1 * n2 + int(result[k] - '0') + carry;
			carry = sum / 10;
			result[k] = char(sum % 10 + '0');
			k -= 1;
			std::cout << n1 << " " << n2 << " " << carry << " " << result << endl;
		}

		result[k] = char(carry + '0');
	}

	int i = 0;
	while (result[i] == '0') i += 1;
	result = result.substr(i, 2 * N - i);

	return result;
}
```

This case might be a bit different. Since there are two loops, we can express the complexity as (N-1) * (N-1) = N². In the process of finding the index of '0', it can be expressed as constant * N². Of course, we might not always discuss the constant factor, but the main point here is to identify what has a major impact.

## Karatsuba Algorithm

The Karatsuba algorithm is an efficient multiplication algorithm that uses a divide-and-conquer approach to multiply large numbers. Developed by Anatoly Karatsuba in 1960, it reduces the complexity from O(n²) in the standard multiplication algorithm to approximately O(n^(log₂3)) ≈ O(n^1.585).

Let's analyze the implementation:

```c++
string KaratsubaHelper(string str1, string str2, int level) // level은 디버깅용
{
	cout << "Level " << level << " : " << str1 << " x " << str2 << endl;

	int N = max(str1.size(), str2.size());
	str1.insert(0, string(N - str1.size(), '0'));
	str2.insert(0, string(N - str2.size(), '0'));

	if (N == 1)
	{
		string result = to_string(stoi(str1) * stoi(str2));
		return result;
	}

	int mid = N / 2;

	string a = str1.substr(0, mid);
	string b = str1.substr(mid, N - mid);

	string c = str2.substr(0, mid);
	string d = str2.substr(mid, N - mid);

	string ac = KaratsubaHelper(a, c, level + 1);
	ac.append(string((N - mid) * 2, '0'));

	return string("0");
}

string Karatsuba(string str1, string str2)
{
	if (!str1.size() || !str2.size()) return "0";
	string result = KaratsubaHelper(str1, str2, 0); 
	int i = 0;
	while (result[i] == '0') i += 1;
	result = result.substr(i, result.size() - i);
	return result;
}
```

### Key Insights
The implementation above is incomplete but demonstrates the core concept of the Karatsuba algorithm. Here's how it works:
1. Padding: First, we ensure both numbers have the same number of digits by padding with leading zeros.
2. Base Case: If we're down to single-digit numbers, we perform a direct multiplication.
3. Divide: For larger numbers, we split each number into two parts:
   - If we represent the numbers as X = a·10^(n/2) + b and Y = c·10^(n/2) + d Where a, b, c, and d are n/2-digit numbers

4. Recursive Multiplication: The complete algorithm would compute:
   - ac = a × c
   - bd = b × d
   - (a+b)(c+d) = ac + ad + bc + bd
   - ad + bc = (a+b)(c+d) - ac - bd

5. Combine: The result is ac·10^n + (ad+bc)·10^(n/2) + bd
   - The current implementation only calculates ac and appends the appropriate number of zeros, but is missing the calculations for bd and (ad+bc).

### Optimizations
The key insight of Karatsuba is that we can compute the product of two n-digit numbers with only three recursive multiplications instead of four:
* ac
* bd
* (a+b)(c+d)

From these, we derive ad+bc = (a+b)(c+d) - ac - bd, reducing the number of recursive calls and improving efficiency.

### Time Complexity
The time complexity is O(n^(log₂3)) ≈ O(n^1.585), which is significantly better than the O(n²) complexity of the standard multiplication algorithm for large numbers.

To complete this implementation, we would need to:
1. Calculate bd = b × d
2. Calculate (a+b)(c+d)
3. Derive ad+bc
4. Combine all terms with appropriate powers of 10

This algorithm is particularly useful for multiplying very large integers that exceed the capacity of built-in numeric types.

## Resource
* [Karatsuba Algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm)