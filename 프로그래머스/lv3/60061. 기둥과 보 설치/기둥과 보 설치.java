import java.util.*;

class Solution {
    public static class Position {
        boolean stick = false;
        boolean floor = false;
    }

    private Position getPositionFromData(HashMap<String, Position> data, int x, int y) {
        String key = x + "," + y;
        return data.computeIfAbsent(key, k -> new Position());
    }

    private boolean checkStickAble(HashMap<String, Position> data, int x, int y) {
        return (y == 0) || getPositionFromData(data, x, y - 1).stick || getPositionFromData(data, x - 1, y).floor || getPositionFromData(data, x, y).floor;
    }

    private boolean checkFloorAble(HashMap<String, Position> data, int x, int y) {
        return getPositionFromData(data, x, y - 1).stick || getPositionFromData(data, x + 1, y - 1).stick || (getPositionFromData(data, x - 1, y).floor && getPositionFromData(data, x + 1, y).floor);
    }

    public int[][] solution(int n, int[][] build_frame) {
        HashMap<String, Position> data = new HashMap<>();
        ArrayList<int[]> result = new ArrayList<>();

        for (int[] command: build_frame) {
            int x = command[0], y = command[1], type = command[2], action = command[3];
            String key = x + "," + y;

            if (type == 0) { // 기둥
                if (action == 1) { // 설치
                    if (checkStickAble(data, x, y)) {
                        getPositionFromData(data, x, y).stick = true;
                        result.add(new int[]{x, y, type});
                    }
                } else { // 삭제
                    getPositionFromData(data, x, y).stick = false;
                    boolean canDelete = true;
                    for (int[] item : result) {
                        if (item[2] == 0 && !checkStickAble(data, item[0], item[1])) {
                            canDelete = false;
                            break;
                        }
                        if (item[2] == 1 && !checkFloorAble(data, item[0], item[1])) {
                            canDelete = false;
                            break;
                        }
                    }
                    if (canDelete) {
                        result.removeIf(item -> Arrays.equals(item, new int[]{x, y, type}));
                    } else {
                        getPositionFromData(data, x, y).stick = true;
                    }
                }
            } else { // 보
                if (action == 1) { // 설치
                    if (checkFloorAble(data, x, y)) {
                        getPositionFromData(data, x, y).floor = true;
                        result.add(new int[]{x, y, type});
                    }
                } else { // 삭제
                    getPositionFromData(data, x, y).floor = false;
                    boolean canDelete = true;
                    for (int[] item : result) {
                        if (item[2] == 0 && !checkStickAble(data, item[0], item[1])) {
                            canDelete = false;
                            break;
                        }
                        if (item[2] == 1 && !checkFloorAble(data, item[0], item[1])) {
                            canDelete = false;
                            break;
                        }
                    }
                    if (canDelete) {
                        result.removeIf(item -> Arrays.equals(item, new int[]{x, y, type}));
                    } else {
                        getPositionFromData(data, x, y).floor = true;
                    }
                }
            }
        }

        Collections.sort(result, (o1, o2) -> {
            if (o1[0] != o2[0]) {
                return Integer.compare(o1[0], o2[0]);
            }
            if (o1[1] != o2[1]) {
                return Integer.compare(o1[1], o2[1]);
            }
            return Integer.compare(o1[2], o2[2]);
        });

        return result.toArray(new int[result.size()][3]);
    }
}