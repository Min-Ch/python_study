import re
import random


def input_timer(prompt, timeout_sec):
    import subprocess
    import sys
    import threading
    import locale

    class Local:
        # check if timeout occured
        _timeout_occured = False

        def on_timeout(self, process):
            self._timeout_occured = True
            process.kill()
            # clear stdin buffer (for linux)
            # when some keys hit and timeout occured before enter key press,
            # that input text passed to next input().
            # remove stdin buffer.
            # try:
            #     import termios
            #     termios.tcflush(sys.stdin, termios.TCIFLUSH)
            # except ImportError:
            #     # windows, just exit
            #     pass

        def input_timer_main(self, prompt_in, timeout_sec_in):
            # print with no new line
            print(prompt_in, end="")

            # print prompt_in immediately
            sys.stdout.flush()

            # new python input process create.
            # and print it for pass stdout
            cmd = [sys.executable, '-c', 'print(input())']
            with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
                timer_proc = threading.Timer(timeout_sec_in, self.on_timeout, [proc])
                try:
                    # timer set
                    timer_proc.start()
                    stdout, stderr = proc.communicate()

                    # get stdout and trim new line character
                    result = stdout.decode(locale.getpreferredencoding()).strip("\r\n")
                finally:
                    # timeout clear
                    timer_proc.cancel()

            # timeout check
            if self._timeout_occured is True:
                # move the cursor to next line
                print("")
                raise TimeoutError
            return result

    t = Local()
    return t.input_timer_main(prompt, timeout_sec)


if __name__ == '__main__':
    with open('dict.txt', 'rt', encoding='utf-8') as f:
        s = f.read()
    pat = re.compile('^[ㄱ-ㅎ가-힣]+$')
    texts = sorted([i for i in s.split() if pat.match(i) and len(i) >= 2], key=lambda x:-len(x))

    total_count = 0
    correct_count = 0

    print('받아쓰기를 시작합니다')

    while total_count < 100:
        print(f'=============== 현재 정답 횟수 : {correct_count} (정답률 : {round(correct_count / total_count, 3) * 100 if correct_count else 0}%))===============')
        total_count += 1
        text = random.choice(texts)
        print('문제 :',text)

        try:
            b = input_timer('입력해주세요 : ', 5)
        except TimeoutError:
            print('시간초과...')
            b = None

        if b == text:
            print('정확합니다!')
            correct_count += 1
        elif b == 'q':
            total_count -= 1
            break
        else:
            print('틀렸습니다!')

    print(f'최종 결과 입니다. 정답 횟수 : {correct_count} (정답률 : {round(correct_count/total_count, 3) * 100 if correct_count else 0}%)')