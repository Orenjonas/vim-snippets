
def math():
    synstackids = vim.eval("synstack(line('.'), col('.') - (col('.')>=2 ? 1 : 0))")
    try:
        first = next(
            i for i in reversed(synstackids)
            if i in texIgnoreMathZoneIds or i in texMathZoneIds
        )
        return first != ignore
    except StopIteration:
        return False
def math():
	synstackids = vim.eval("synstack(line('.'), col('.') - (col('.')>=2 ? 1 : 0))")
	try:
		first = next(
            i for i in reversed(synstackids)
            if i in texIgnoreMathZoneIds or i in texMathZoneIds
        )
		return first != ignore
	except StopIteration:
		return False
