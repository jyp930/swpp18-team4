import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ArbeitPostCreateComponent } from './arbeit-post-create.component';

import { RouterTestingModule } from "@angular/router/testing";
import { FormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";

describe('ArbeitPostCreateComponent', () => {
  let component: ArbeitPostCreateComponent;
  let fixture: ComponentFixture<ArbeitPostCreateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ArbeitPostCreateComponent ],
      imports: [
        RouterTestingModule,
        FormsModule,
        HttpClientModule,
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ArbeitPostCreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    component.ngOnInit();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('test isValidInput func', () => {
    let region = component.region;
    expect(component.isValidInput(region)).toBeFalsy();
    region = '';
    expect(component.isValidInput(region)).toBeFalsy();
    region = 'Nakdae';
    expect(component.isValidInput(region)).toBeTruthy();
  });

  it('test back func when yes', () => {
    spyOn(window, 'confirm').and.returnValue(true);
    component.back();
    /* url test */
  });

  it('test back func when no', () => {
    spyOn(window, 'confirm').and.returnValue(false);
    component.back();
    /* url test */
  });

  it('test confirm func', () => {
    spyOn(window, "alert");
    component.confirm();
    expect(window.alert).toHaveBeenCalledWith("제목을 입력해 주세요.");
    component.title = '제목입니다.';
    component.confirm();
    expect(window.alert).toHaveBeenCalledWith("지역을 입력해 주세요.");
    component.region = 'Nakdae';
    component.confirm();
    expect(window.alert).toHaveBeenCalledWith("아르바이트 종류를 입력해 주세요.");
    component.arbeit_type = 'Mentoring';
    component.confirm();
    expect(window.alert).toHaveBeenCalledWith("시급을 입력해 주세요.");
    component.pay = 1000;
    component.confirm();
    expect(window.alert).toHaveBeenCalledWith("담당자 이름을 입력해 주세요.");
    component.manager_name = 'Team4';
    component.confirm();
    expect(window.alert).toHaveBeenCalledWith("담당자 전화번호를 입력해 주세요.");
    component.manager_phone = '010-0000-0000';
    component.confirm();
    expect(window.alert).toHaveBeenCalledWith("내용을 입력해 주세요.");
    component.content = '내용입니다.';
    component.confirm();
    expect(window.alert).toBeTruthy();

  });



});
