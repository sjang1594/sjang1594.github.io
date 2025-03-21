---
title: Karatsuba Algorithm
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Karatsuba Algorithm

### Before Gettign Into Karatsuba Algorithm

예전에 대학원생일때, Addition, Subtraction, Division, Multiplication 에 관련되서 Project 로 작성한적이 있다. (어떻게하면 각 Operation 을 빠르게 할수 있는지에 대해서, Hardware 측면에서 더 이야기를 했던것 같아. Multiplexer 의 추가 등...)

그래서 일단 Addition / Subtraction / Multiplication 에 대한 예제코드를 봐보겠다. C++ 로 작성했으며, 항상 First Digit 이 Second Digit 의 길이가 크다라는 가정하에 작성을 했다. 자 특이점은 전부다 String 으로 처리한다는 점이다.

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

이 코드에서의 N 에 따른 Performance 를 가지고 있다. Time Complexity 생각을 해보면 대략 T(N) ~= N 이 나온다. 물론 insert 가 일어날때는 약간의 Constant 가 Multiplied 될수 있다. 

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

마찬가지로 코드에서의 N 에 따른 Performance 를 가지고 있다. Time Complexity 생각을 해보면 대략 T(N) ~= N 이 나온다. 

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

자 여기에서는 조금 다를수 있다. 기본적으로 Two loops 가 있으니까 (N-1) * (N-1) = N^2 로 표현할수 있는데, '0' 의 index 를 찾는데 과정에서, constant * N^2 로 표현할수 있다. 물론 상수를 이야기를 안할수도 있는데 Major 로 Impact 로 줄수 있는걸 찾는게 여기에서는 Main point 이다.

## Karatsuba Algorithm 

## Resource
* [Karatsuba Algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm)