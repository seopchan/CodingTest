function solution(s){
    let p = 0, y = 0;
    
    for (const c of s) {
        switch(c) {
            case 'p':
            case 'P': {
                p++;
                break;   
            }
            case 'y':
            case 'Y': {
                y++;
                break;
            }
            default:
                break;
        }
    }

    return (p == y);
}