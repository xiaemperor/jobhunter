# coding=utf-8
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import JobHunter.JobHunter_CX