# 阅读pytest源代码

## 1.pytest.mark.raise

```
Using pytest.raises() is likely to be better for cases where you are testing exceptions your own code is deliberately 
raising, whereas using @pytest.mark.xfail with a check function is probably better for something like
documenting unfixed bugs (where the test describes what “should” happen) or bugs in dependencies.
```

## 2.pytest.mark.warns

- 可以通过实现pytest_assertrepr_compare钩子来添加您自己的详细解释

```
pytest_assertrepr_compare(config, op, left, right)
```

## 3. fixture
- 在测试中，fixture为测试提供了定义好的、可靠的和一致的上下文。这可能包括环境(例如配置了已知参数的数据库)或内容(例如数据集)。
- 