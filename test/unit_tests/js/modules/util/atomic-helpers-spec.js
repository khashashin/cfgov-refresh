const BASE_JS_PATH = '../../../../../cfgov/unprocessed/js/';
const atomicHelpers = require( BASE_JS_PATH + 'modules/util/atomic-helpers' );

let containerDom;
let expandableDom;
const HTML_SNIPPET = `
  <div class="container">
  <div class="o-expandable"></div></div>
`;

describe( 'atomic-helpers', () => {
  beforeAll( () => {
    document.body.innerHTML = HTML_SNIPPET;
    containerDom = document.querySelector( '.container' );
    expandableDom = document.querySelector( '.o-expandable' );
  } );

  describe( '.checkDom()', () => {
    it( 'should throw an error if element DOM not found', () => {
      const errMsg = 'null is not valid. ' +
                     'Check that element is a DOM node with ' +
                     'class ".o-expandable"';
      function errFunc() {
        atomicHelpers.checkDom( null, '.o-expandable' );
      }
      expect( errFunc ).toThrow( Error, errMsg );
    } );

    it( 'should throw an error if element class not found', () => {
      const errMsg = 'mock-class not found on or in passed DOM node.';
      function errFunc() {
        atomicHelpers.checkDom( expandableDom, 'mock-class' );
      }
      expect( errFunc ).toThrow( Error, errMsg );
    } );

    it( 'should return the correct HTMLElement when direct element is searched',
      () => {
        const dom = atomicHelpers.checkDom( expandableDom, 'o-expandable' );
        expect( dom ).toEqual( expandableDom );
      }
    );

    it( 'should return the correct HTMLElement when parent element is searched',
      () => {
        const dom = atomicHelpers.checkDom( containerDom, 'o-expandable' );
        expect( dom ).toEqual( expandableDom );
      }
    );
  } );

  describe( '.instantiateAll()', () => {
    xit( 'should return an array of instances', () => {
      // TODO: Implement test.
    } );
  } );

  describe( '.setInitFlag()', () => {
    it( 'should return true when init flag is set', () => {
      expect( atomicHelpers.setInitFlag( expandableDom ) ).toBe( true );
    } );

    it( 'should return false when init flag is already set', () => {
      atomicHelpers.setInitFlag( expandableDom );
      expect( atomicHelpers.setInitFlag( expandableDom ) ).toBe( false );
    } );
  } );

  describe( '.destroyInitFlag()', () => {

    beforeEach( () => {
      atomicHelpers.setInitFlag( expandableDom );
    } );

    it( 'should return true when init flag is removed', () => {
      expect( atomicHelpers.destroyInitFlag( expandableDom ) ).toBe( true );
    } );

    it( 'should return false when init flag has already been removed', () => {
      atomicHelpers.destroyInitFlag( expandableDom );
      expect( atomicHelpers.destroyInitFlag( expandableDom ) ).toBe( false );
    } );
  } );
} );
