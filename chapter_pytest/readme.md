# fixture的参数化
pytest支持在多个完整测试参数化方法：

1. pytest.fixture();在fixture级别的function处参数化
2. @pytest.mark.parametrize:允许在function或class级别的参数化，
为特定的测试函数或类提供多个argument/fixture设置。
3. _.pytest_generate_tests:可以实现自己的自定义动态参数化方案或拓展；


**展示哪些用例会被运行**
`--collect-only`

