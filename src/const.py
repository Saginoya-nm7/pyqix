import pygame.locals as pgConst


# 画面に関する定数
class Screen:
    # スクリーンサイズ
    Size = (640, 480)

    # タイトルバーに表示する文字列
    Title = "pyqix"


# ゲームに関する定数
class Game:
    class Field:
        # フィールドのサイズ
        Size = (320, 320)

        # フィールドの左上座標
        Pos = (5, 5)


# 色に関する定数
class Color:
    # 埋めたエリアを塗りつぶす色
    FillArea = (0, 200, 200)

    # 境界線の色
    Border = (255, 255, 255)

